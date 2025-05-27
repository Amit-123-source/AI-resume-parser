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
  - Work Experience
  - Hobbies
  - Qualities
- Supports batch processing of resumes.
- Saves extracted data in CSV or Excel format.

## Project Structure
```
├── extract_info.py      # Contains functions for extracting resume information.
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
   git clone https://github.com/Amit-123-source/resume-parser.git
   cd resume-parser
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
3. The output format (CSV or Excel) is defined in the `main.py` script via the `output_format` variable.
4. The extracted data will be saved as `extracted_resume_data.csv` or `extracted_resume_data.xlsx`.

## Example Output
### Example CSV Output (`extracted_resume_data.csv`):
| Name        | Email               | Phone        | Education                   | Skills                  | Projects                    | Work Experience             | Hobbies          | Qualities            | Resume Name           |
|-------------|---------------------|--------------|-----------------------------|--------------------------|-----------------------------|-----------------------------|------------------|-----------------------|-----------------------|
| John Doe    | john.doe@gmail.com  | +1234567890  | B.Sc. in CS, XYZ University | Python, SQL             | Developed a web app        | Interned at ABC Corp        | Reading, Sports  | Leadership, Teamwork  | John_Doe_Resume.pdf   |
| Jane Smith  | jane.smith@yahoo.com| +1987654321  | M.Sc. in Data Science, ABC | Python, Excel           | Built a recommendation sys | Employed at XYZ Ltd         | Music, Art       | Problem-solving       | Jane_Smith_Resume.pdf |

### Example Excel Output (`extracted_resume_data.xlsx`):
Same structure as CSV output, saved as an Excel spreadsheet with a single sheet.

## Error Handling
- Unreadable or malformed PDFs are skipped.
- Errors during parsing are printed with the file name.

## License
MIT License
---

### Sample Run
```bash
python main.py
```
Expected output:
- Data saved to `extracted_resume_data.csv` or `extracted_resume_data.xlsx`

### Known Issues
- PDFs with only images require OCR tools to extract text.
