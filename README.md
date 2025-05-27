
# Resume Parser AI

This project is an AI-based resume parser that extracts and organizes key information from resumes in PDF format. It is designed to streamline HR processes and enhance candidate selection by providing structured data from unstructured resumes.

## Features
- Extracts key information:
  - Name
  - Email
  - Phone Number
  - Education
  - Skills
  - Projects
- Supports batch processing of resumes.
- Saves extracted data in CSV or Excel format.

## Project Structure
```
├── extract_info.py      # Contains functions for extracting information like email, phone, etc.
├── main.py              # Main script to process resumes.
├── pdf_parser.py        # Handles text extraction from PDFs.
├── utils.py             # Utility functions for saving data to files.
├── README.md            # Project documentation.
├── requirements.txt     # Python dependencies.
├── sample_resumes/      # Folder to store sample resumes for testing.
```

## Prerequisites
- Python 3.7+

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place resumes in the `sample_resumes/` folder.
2. Run the script:
   ```bash
   python main.py
   ```
3. Choose the output format (CSV or Excel) in the `main.py` script by modifying the `output_format` variable.
4. The extracted data will be saved as `extracted_resume_data.csv` or `extracted_resume_data.xlsx`.

## Example Output
### Example CSV Output (`extracted_resume_data.csv`):
| Resume Name           | Name          | Email               | Phone          | Education                | Skills                        | Projects                          |
|-----------------------|---------------|---------------------|----------------|--------------------------|-------------------------------|-----------------------------------|
| John_Doe_Resume.pdf   | John Doe      | john.doe@gmail.com  | +1234567890    | B.Sc. in Computer Science, XYZ University | Python, Java, SQL                | Developed a web scraping tool.   |
| Jane_Smith_Resume.pdf | Jane Smith    | jane.smith@yahoo.com | +1987654321    | M.Sc. in Data Science, ABC University    | Python, Machine Learning, Excel  | Built a recommendation system.   |

### Example Excel Output (`extracted_resume_data.xlsx`):
The structure will be the same as the CSV file but stored in an Excel format with sheet names like "Resume Data."

## Error Handling
The script gracefully skips any unreadable or malformed PDF files and logs their names for review.

## License
MIT License

## Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

---

### Sample Run
Place PDF resumes in the `sample_resumes/` folder and execute the command:
```bash
python main.py
```
Expected output:
- Data saved to `extracted_resume_data.csv` or `extracted_resume_data.xlsx`

### Known Issues
- PDFs with only images require OCR tools to extract text.

### Future Enhancements
- Integrate OCR functionality for image-based PDFs.
- Add a web-based UI for resume uploads and data visualization.
