from types import NoneType
from PIL import Image
from google.cloud import vision
from io import BytesIO
import traceback

# Initialize the Vision client outside the function for better performance if called frequently
client = vision.ImageAnnotatorClient()
print("Authentication Successful.")

# Convert an image to text
def img_to_text(image):
    try:
        # Save image to a byte array
        byte_arr = BytesIO()
        image.save(byte_arr, format='PNG')
        print("Image saved in PNG format.")

        # Get the byte data from the array
        byte_arr = byte_arr.getvalue()

        # Create a Vision API image object
        vision_image = vision.Image(content=byte_arr)
        print("Getting Vision Image")

        # Perform text detection
        response = client.text_detection(image=vision_image)
        print("Receiving Response")

        # Handle response errors
        if response.error.message:
            print(f"Error: {response.error.message}")
        else:
            # Print detected text
            text = response.text_annotations
            if text:
                return text[0].description
            else:
                print("No text found in the image.")
                return ""
    
    except Exception as e:
        print("=============ERROR===============")
        print(f"An error occurred: {e}")
        traceback.print_exc()


