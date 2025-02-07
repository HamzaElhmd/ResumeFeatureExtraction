# Resume Feature Extraction

The **Resume Feature Extraction** pipeline processes resumes in **PDF format**, extracting key **profile information** efficiently.  

## Pipeline Overview

1. **Upload a _.pdf_ file** to the feature extractor.  
2. **Convert the PDF into a _.png_ image** for processing.  
3. **Apply grayscale filtering and median blur** to enhance image quality.  
4. **Perform Optical Character Recognition (OCR)** to extract text.  
5. **Extract detected text** from the processed image.  
6. **Use Regex** to identify key details such as **name, email, phone number, and country**.  

## Tech Stack  

- **OCR:** Powered by **Google Vision**, a cloud-based **Machine Learning as a Service (MLaaS)** solution for computer vision.  
- **PDF to PNG Conversion:** Utilizes the **_pdf2image_** Python library for image extraction.  

## Running the Application  

Before executing the application, ensure that the **Python virtual environment** is activated. Then, run the program with the `-m` option.  

### Linux & macOS  
```bash
source venv/bin/activate
python -m App.py
```
