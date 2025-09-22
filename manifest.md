# Manifest — AI QR Code Generator (Hands-On Assignment 2, MSCS-633)

## Course Information
- **Course:** MSCS-633 — Advanced Artificial Intelligence  
- **Assignment:** Hands-On Assignment 2 — AI QR Code Generator  
- **Student:** Pabitra Bhandari  
- **Submission Date:** 09/21/2025 

---

## Purpose
This project implements a Python-based QR code generator application.  
It demonstrates two interfaces:
1. **Command-Line Interface (CLI):** Generates and saves QR codes as PNG images.  
   - If `--out` is omitted, filenames are **auto-named based on the URL host**.  
   - Example: `https://www.google.com` → `output/qr_google.com.png`.  
2. **Graphical User Interface (GUI):** Built with Tkinter.  
   - Renders the QR code **inline in the window** when “Generate QR” is clicked.  
   - No file is saved to disk in GUI mode.  

Default demo URL: **https://www.bioxsystems.com**

---

## Project Structure
ai-qr-generator/
├── qr_core.py # Core QR utilities (make_qr_image, generate_qr)
├── qr_generator.py # CLI wrapper (auto-names files from URL host)
├── app_gui.py # GUI app (renders QR inline, no save)
├── requirements.txt # Python dependencies
├── README.md # Setup and usage instructions
├── manifest.md # Project overview (this file)
├── .gitignore # Ignore venv, pycache, output/
└── output/ # Folder for saved QR images (created by CLI)

---

## Environment Setup
### Requirements
- Python 3.10+  
- Virtual environment recommended  
- Tested on macOS with Python 3.11  

### Installation
```bash
cd ai-qr-generator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Dependencies (requirements.txt):**
- qrcode[pil]>=7.4  
- validators>=0.22  

qrcode[pil] → QR generation + Pillow for image handling  
validators → Optional URL validation (fallback validation included)  

---

## Ways to Run

### 1. GUI (Inline Display, No Save)
```bash
python app_gui.py
```
- Enter a URL in the text box.  
- Click Generate QR.  
- QR code displays directly in the app window.  
- No file is saved to disk.  

### 2. CLI (Auto-Named Output)
```bash
python qr_generator.py --url https://www.google.com --open
# → output/qr_google.com.png

python qr_generator.py --url https://openai.com
# → output/qr_openai.com.png
```

### 3. CLI (Explicit Output File)
```bash
python qr_generator.py --url https://ucumberlands.blackboard.com --out output/blackboard.png --open
```

### 4. CLI (Interactive Prompt)
```bash
python qr_generator.py --prompt
```
- Prompts the user to enter a URL at runtime.  

### 5. CLI (Custom QR Styling)
```bash
python qr_generator.py   --url https://example.com   --ec Q   --box 12   --border 4   --fill "#003366"   --back "white"
```

**Options:**
- `--ec` → Error correction (L, M, Q, H)  
- `--box` → Pixel size per module (default 10)  
- `--border` → Border width in modules (default 4)  
- `--fill` / `--back` → Foreground & background colors  

---

## Deliverables
- Source Code (all project files listed above).  
- Manifest (`manifest.md`) — this document.  
- Word Document containing:  
  - Screenshot of the QR code output (GUI or CLI Preview).  
  - GitHub repository URL.  
  - Brief explanation of the project.  
- GitHub Repository with source code and documentation.  

---

## Coding Practices
- Modular design with separation of concerns:  
  - `qr_core.py` handles QR generation logic.  
  - `qr_generator.py` provides CLI interface.  
  - `app_gui.py` provides GUI interface.  
- Type hints and docstrings included.  
- Error handling for invalid URLs.  
- Defaults provided, with customization options for color, size, and error correction.  
