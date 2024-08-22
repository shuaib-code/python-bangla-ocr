import pytesseract
from pdf2image import convert_from_path
import os

# Path to the Tesseract-OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if necessary

# Path to the PDF file
pdf_path = 'example.pdf'

# Convert PDF to images
images = convert_from_path(pdf_path, dpi=300,poppler_path = r'poppler\bin')

# Directory to save text files
output_dir = 'text_OCR'
os.makedirs(output_dir, exist_ok=True)

# Iterate over images and extract text
for i, image in enumerate(images):
    # Perform OCR on the image
    text = pytesseract.image_to_string(image, lang='ben')  # 'ben' is the language code for Bangla

    # Save the extracted text to a file
    text_file = os.path.join(output_dir, f'page_{i+1}.txt')
    with open(text_file, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Processed page {i+1}/{len(images)}")

print("OCR process completed!")
