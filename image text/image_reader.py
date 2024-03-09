from PIL import Image
from pytesseract import pytesseract

class ImageReader:
    def __init__(self, os):
        if os == 'Mac':
            # Tesseract is already installed via Homebrew
            print('Running on: MAC\n')
        elif os == 'Windows':
            # This should be replaced with your own path to tesseract.exe
            windows_path = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
            pytesseract.tesseract_cmd = windows_path
            print('Running on: WINDOWS\n')
        else:
            raise ValueError("Unsupported OS")

    def extract_text(self, image_path, lang):
        img = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(img, lang=lang)
        return extracted_text

if __name__ == '__main__':
    ir = ImageReader('Windows')
    text = ir.extract_text(image_path='C:/Users/hunter/Desktop/image text/images/try.png', lang='eng')

    processed_text = ' '.join(text.split())
    print(processed_text)