# PDF to Text OCR Conversion

This project provides a Python script to convert scanned PDF files into text using Optical Character Recognition (OCR). The script utilizes the `pdf2image` and `pytesseract` libraries, along with the Poppler utility for converting PDF pages into images.

## Prerequisites

Before running the script, ensure that the following software is installed on your system:

1. **Python 3.x** - The script is written in Python. You can download Python from the [official website](https://www.python.org/downloads/).

2. **Tesseract-OCR** - Tesseract is an open-source OCR engine. Download and install it from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).

3. **Poppler** - Poppler is required for converting PDF pages to images. You can install it manually by following the instructions below.

## Installing Poppler on Windows

### Option 1: Using Winget (Recommended)

1. Open Command Prompt or PowerShell.
2. Run the following command to install Poppler:
   ```bash
   winget install poppler
   ```
3. Verify the installation by running:
   ```bash
   pdfinfo
   ```
   If Poppler is correctly installed, this command will display information about the `pdfinfo` utility.

### Option 2: Manual Installation

1. Download the latest version of Poppler for Windows from [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/).
2. Extract the contents to a folder (e.g., `C:\poppler`).
3. Add the path to the `bin` folder inside the Poppler directory to your system's PATH:

   - Right-click on `This PC` or `Computer` and select `Properties`.
   - Click `Advanced system settings`.
   - Under `System variables`, find `Path`, select it, and click `Edit`.
   - Add `C:\poppler\bin` to the list of paths.
   - Click `OK` to save the changes.

4. Verify the installation by running `pdfinfo` in Command Prompt.

## Installing Python Packages

Install the required Python libraries by running:

```bash
pip install pytesseract pdf2image
```
