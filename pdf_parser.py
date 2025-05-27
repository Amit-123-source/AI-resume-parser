import pdfplumber

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from the given PDF file.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text