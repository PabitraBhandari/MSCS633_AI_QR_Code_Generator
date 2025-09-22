"""Small Tkinter GUI wrapper around :mod:'qr_core.make_qr_image'.

Provides a simple window to enter a URL and render the QR code.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox
from urllib.parse import urlparse

try:
	import validators  # optional strict URL validation
except Exception:
	validators = None

from PIL import ImageTk

from qr_core import make_qr_image


def _is_valid_url(url: str) -> bool:
	if validators is not None:
		return bool(validators.url(url))
	parts = urlparse(url)
	return bool(parts.scheme in {"http", "https"} and parts.netloc)


def on_generate(entry_url: tk.Entry, image_label: tk.Label, status: tk.StringVar, root: tk.Tk) -> None:
	url = entry_url.get().strip()
	if not url:
		messagebox.showwarning("Missing URL", "Please enter a URL.")
		return
	if not _is_valid_url(url):
		messagebox.showerror("Invalid URL", "Please provide a valid http(s) URL.")
		return
	try:
		img = make_qr_image(url, ec='M', box_size=10, border=4)
	except Exception as e:
		messagebox.showerror("Error", f"Failed to generate QR: {e}")
		return

	photo = ImageTk.PhotoImage(img)
	image_label.configure(image=photo)
	# keep a reference to avoid garbage collection
	root._qr_photo_ref = photo  # type: ignore[attr-defined]
	status.set("QR rendered below.")


def main() -> None:
	root = tk.Tk()
	root.title("AI QR Code Generator")
	root.geometry("560x520")

	frm = tk.Frame(root, padx=12, pady=12)
	frm.pack(fill=tk.BOTH, expand=True)

	# Row 0: label + entry
	tk.Label(frm, text="Enter URL:").grid(row=0, column=0, sticky="w")
	entry = tk.Entry(frm, width=60)
	entry.grid(row=0, column=1, padx=8, pady=(0, 6), sticky="we")
	entry.insert(0, "https://www.bioxsystems.com")
	frm.grid_columnconfigure(1, weight=1)

	# Row 1: button directly below the URL input on the left side
	status = tk.StringVar(value="Ready")
	# image_label will be created before the button so the command can reference it
	image_label = tk.Label(frm, bd=1, relief=tk.SUNKEN, width=480, height=480)
	btn = tk.Button(frm, text="Generate QR", command=lambda: on_generate(entry, image_label, status, root))
	btn.grid(row=1, column=1, sticky="w", pady=(0, 10))

	# Row 2: image display area
	image_label.grid(row=2, column=0, columnspan=2, sticky="nwe")

	# Row 3: status text
	tk.Label(frm, textvariable=status, fg="green").grid(row=3, column=0, columnspan=2, sticky="w", pady=(8, 0))

	root.mainloop()


if __name__ == "__main__":
	main()