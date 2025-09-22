"""Command-line QR generator wrapper around :mod:`qr_core`.

This file provides a small CLI to generate a PNG QR for a URL.
It auto-names the output file based on the URL host unless --out is specified.
"""

from __future__ import annotations

import re
import argparse
import sys
import subprocess
from pathlib import Path
from urllib.parse import urlparse

try:
    import validators  # optional: for stricter URL validation
except Exception:  # pragma: no cover - keep CLI resilient if validators missing
    validators = None

from qr_core import generate_qr


DEFAULT_URL = "https://www.bioxsystems.com"
DEFAULT_DIR = Path("output")


def _is_valid_url(url: str) -> bool:
    if validators is not None:
        return bool(validators.url(url))

    # Fallback lightweight check
    parts = urlparse(url)
    return bool(parts.scheme in {"http", "https"} and parts.netloc)


def _slug_from_url(url: str) -> str:
    """Generate a safe filename slug from the URL's host."""
    host = urlparse(url).netloc or "url"
    # strip common www.
    host = re.sub(r"^www\\.", "", host)
    # keep safe chars only
    slug = re.sub(r"[^a-zA-Z0-9._-]", "-", host)
    return slug or "url"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a QR code PNG for a given URL.")
    src = p.add_mutually_exclusive_group()
    src.add_argument("--url", type=str, help="URL to encode (default: %(default)s)", default=DEFAULT_URL)
    src.add_argument("--prompt", action="store_true", help="Prompt for URL interactively")

    # --out is now optional; if omitted, auto-names from URL
    p.add_argument("--out", type=Path, default=None, help="Output PNG path (default: output/qr_<host>.png)")
    p.add_argument("--ec", type=str, choices=["L", "M", "Q", "H"], default="M", help="Error correction level")
    p.add_argument("--box", type=int, default=10, help="Box size (pixel scale) for each module")
    p.add_argument("--border", type=int, default=4, help="Border width (modules)")
    p.add_argument("--fill", type=str, default="black", help="Foreground color")
    p.add_argument("--back", type=str, default="white", help="Background color")
    p.add_argument("--open", action="store_true", help="Open the generated image (macOS)")

    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if args.prompt:
        try:
            url = input("Enter the URL to encode: ").strip()
        except KeyboardInterrupt:
            print("\nCancelled.")
            return 130
    else:
        url = args.url

    if not _is_valid_url(url):
        print(f"[error] Invalid URL: {url}\nPlease provide an http(s) URL.", file=sys.stderr)
        return 2

    # Determine output filename
    out_path = args.out
    if out_path is None:
        slug = _slug_from_url(url)
        out_path = DEFAULT_DIR / f"qr_{slug}.png"

    try:
        out_path = generate_qr(
            url=url,
            out_path=out_path,
            ec=args.ec,
            box_size=args.box,
            border=args.border,
            fill_color=args.fill,
            back_color=args.back,
        )
    except Exception as e:
        print(f"[error] Failed to generate QR: {e}", file=sys.stderr)
        return 1

    print(f"[ok] QR generated: {out_path.resolve()}")

    if args.open and sys.platform == "darwin":
        # Open with macOS Preview
        try:
            subprocess.call(["open", str(out_path)])
        except Exception:
            print("[warn] Failed to open image automatically.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
