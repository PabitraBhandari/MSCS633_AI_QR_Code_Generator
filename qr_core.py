"""
qr_core.py
Core QR generation utilities used by both the CLI and the GUI.
- 'make_qr_image(...)' returns a PIL.Image in memory (no file I/O)
- 'generate_qr(...)' optionally saves to disk for CLI workflows
"""
from __future__ import annotations
from pathlib import Path
from typing import Literal, Optional

import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H

ErrorCorrection = Literal['L', 'M', 'Q', 'H']

_EC_MAP = {
    'L': ERROR_CORRECT_L,  # ~7% error correction
    'M': ERROR_CORRECT_M,  # ~15%
    'Q': ERROR_CORRECT_Q,  # ~25%
    'H': ERROR_CORRECT_H,  # ~30%
}


def make_qr_image(
    url: str,
    *,
    ec: ErrorCorrection = 'M',
    box_size: int = 10,
    border: int = 4,
    fill_color: str = 'black',
    back_color: str = 'white',
):


    """Create and return a PIL.Image containing the QR code for 'url'.

    No file is written—use this for GUI display or further processing.
    """
    if ec not in _EC_MAP:
        raise ValueError(f"Invalid error correction '{ec}'. Choose from L, M, Q, H.")

    qr = qrcode.QRCode(
        version=None,  # let the library pick minimal size
        error_correction=_EC_MAP[ec],
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    # ensure a standard Pillow Image (not qrcode's wrapper) for Tkinter/others
    try:
        img = img.convert("RGB")
    except Exception:
        pass
    return img


def generate_qr(
    url: str,
    out_path: Path,
    *,
    ec: ErrorCorrection = 'M',
    box_size: int = 10,
    border: int = 4,
    fill_color: str = 'black',
    back_color: str = 'white',
) -> Path:


    """
    Generate a QR code PNG for the given URL and save to 'out_path'.
    Returns the path where the PNG was written.
    """
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    img = make_qr_image(
        url,
        ec=ec,
        box_size=box_size,
        border=border,
        fill_color=fill_color,
        back_color=back_color,
    )
    img.save(out_path)
    return out_path
