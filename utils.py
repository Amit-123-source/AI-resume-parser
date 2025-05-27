import pandas as pd

def save_to_csv(data, output_file='extracted_resume_data.csv'):
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Saved CSV to {output_file}")

def save_to_excel(data, output_file='extracted_resume_data.xlsx'):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False, engine='openpyxl')
    print(f"Saved Excel to {output_file}")
