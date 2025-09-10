import pytesseract
from PIL import Image
import os

# Path to Tesseract executable (Windows only)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path, output_file="output.txt"):
    try:
        if not os.path.exists(image_path):
            print("❌ File not found! Please provide a valid image path.")
            return

        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)

        print("\n📄 Extracted Text:\n")
        print(text)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"\n✅ Text successfully saved to {output_file}")

    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    print("🖼️ Welcome to Image-to-Text Converter")
    image_path = input("Enter image file path (e.g., images.jpeg): ").strip()
    image_to_text(image_path)
