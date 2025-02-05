from modules.FileConversion.PdfConverter import convert_pdf_to_png
from modules.FeatureExtraction.Ocr import img_to_text

if __name__ == '__main__':
    images = []
    fileText = []
    filePath = input("Enter the path of a resume (in PDF):")
    
    if not filePath:
        raise Exception("ERROR: Empty file path submitted.")
    
    if not filePath.lower().endswith('.pdf'):
        raise Exception("ERROR: File format is not pdf.")

    with open(filePath, 'rb') as file:
        fileBytes = file.read()
        images = convert_pdf_to_png(content=fileBytes)

    if not images:
        raise Exception(f"ERROR: Failed to read from {filePath}")

    for img in images:
        text = img_to_text(img)
        if not text:
            raise Exception("ERROR: Failed to perform optical character recognition.")
        
        fileText.append(text)

    fileText = "\n".join(fileText)

    print(fileText)
