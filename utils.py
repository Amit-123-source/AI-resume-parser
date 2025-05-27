import pandas as pd

def save_to_csv(data, output_file='extracted_resume_data.csv'):
    """ Saves the extracted data into a CSV file. """
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)

def save_to_excel(data, output_file='extracted_resume_data.xlsx'):
    """ Saves the extracted data into an Excel file. """
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False, engine='openpyxl')