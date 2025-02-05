from pdf2image import convert_from_bytes
from PIL import Image
import traceback

def convert_pdf_to_png(filename=None, content=None):
    if filename:
        with open(filename, 'rb') as file:
            content = file.read()
    try:
        images = convert_from_bytes(content, dpi=300, grayscale=True)

        return images
    except Exception as e:
        traceback.print_exc()
        print(e)
        return None


