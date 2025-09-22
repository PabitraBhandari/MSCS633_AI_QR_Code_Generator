# AI QR Code Generator

Hands-On Assignment 2 for **MSCS-633-M50 Advanced Artificial Intelligence (Fall 2025)**.  
This project demonstrates how to generate QR codes using Python via both a **Command-Line Interface (CLI)** and a **Graphical User Interface (GUI)**.  

Default demo URL: [Biox Systems](https://www.bioxsystems.com)

---

## Features
- Generate QR codes from any valid URL.
- **CLI support**: customize error correction, colors, size, and save output as PNG.  
- **GUI support**: paste a URL and display QR inline without saving.  
- Auto-names output files based on domain (e.g., `qr_google.com.png`).  
- Works cross-platform (tested on macOS, Linux, Windows).

---

## Project Structure
```
ai-qr-generator/
├── qr_core.py          # Core QR generation logic
├── qr_generator.py     # CLI wrapper
├── app_gui.py          # GUI version with Tkinter
├── requirements.txt    # Dependencies
├── manifest.md         # Project manifest (submission deliverable)
├── README.md           # This file
└── output/             # Auto-generated QR codes (from CLI runs)
```

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/ai-qr-generator.git
cd ai-qr-generator
```

### 2. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows PowerShell
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### Run GUI (inline QR display, no save)
```bash
python app_gui.py
```

### Run CLI with auto-named output
```bash
python qr_generator.py --url https://www.google.com
# → output/qr_google.com.png
```

### Run CLI with explicit output path
```bash
python qr_generator.py --url https://ucumberlands.blackboard.com --out output/blackboard.png
```

### Run CLI interactively
```bash
python qr_generator.py --prompt
```

### Run CLI with custom style
```bash
python qr_generator.py \
  --url https://example.com \
  --ec Q \
  --box 12 \
  --border 4 \
  --fill "#003366" \
  --back "white"
```

---

## Screenshot
(Add your generated screenshot here for submission)

---

## Deliverables
- Source code (.py files)  
- manifest.md (technical description & instructions)  
- README.md (this file, student/GitHub facing)  
- Word document with screenshot + GitHub repo link  

---

## License
This project is submitted as part of coursework for University of the Cumberlands, MSCS-633 (Fall 2025).  
Use is permitted for educational purposes only.
