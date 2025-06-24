import pdfplumber
import PyPDF2
import regex as re

def extract_text_from_pdf(pdf_path):
    """
    Extract text from PDF using multiple methods for better accuracy
    """
    text = ""
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        
        if len(text.strip()) > 100:  
            return clean_extracted_text(text)
            
    except Exception as e:
        print(f"pdfplumber failed for {pdf_path}: {e}")
    
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        
        return clean_extracted_text(text)
        
    except Exception as e:
        print(f"PyPDF2 also failed for {pdf_path}: {e}")
        return ""

def clean_extracted_text(text):
    """
    Clean and normalize extracted text
    """
    if not text:
        return ""
    
    text = re.sub(r' +', ' ', text)  
    text = re.sub(r'\n\s*\n', '\n\n', text)  
    text = text.strip()
    
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)  
    text = re.sub(r'(\d)([A-Za-z])', r'\1 \2', text)
    
    return text
