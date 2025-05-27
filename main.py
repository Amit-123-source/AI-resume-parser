import os
from pdf_parser import extract_text_from_pdf
from extract_info import extract_information
from utils import save_to_csv, save_to_excel

def process_resumes(folder_path):
    """ Process all resumes in the folder and extract information. """
    data = []
    for file in os.listdir(folder_path):
        if file.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, file)
            print(f"Processing {file}...")
            text = extract_text_from_pdf(pdf_path)
            extracted_data = extract_information(text)
            extracted_data['Resume Name'] = file
            data.append(extracted_data)
    
    return data

def main():
    folder_path = 'sample_resumes'  # Folder containing the resume PDFs
    output_format = 'csv'  # Options: 'csv' or 'excel'
    
    # Process resumes and get extracted data
    resume_data = process_resumes(folder_path)
    
    # Save the data to file
    if output_format == 'csv':
        save_to_csv(resume_data)
    elif output_format == 'excel':
        save_to_excel(resume_data)
    
    print(f"Resume information extracted and saved to {output_format}.")

if __name__ == "__main__":
    main()
