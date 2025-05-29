
# Resume Parser AI

🎯 An advanced AI-powered resume parser that extracts and organizes comprehensive information from PDF resumes. This tool streamlines HR processes and enhances candidate selection by converting unstructured resume data into structured, actionable insights.

## 🌟 Features

### Core Information Extraction
- **Personal Details**: Name, Email, Phone Number
- **Professional Background**: Work Experience, Skills, Education
- **Additional Information**: Projects, Hobbies, Personal Qualities
- **Smart Text Processing**: Advanced pattern recognition and NLP techniques

### Advanced Capabilities
- **Batch Processing**: Process multiple resumes simultaneously
- **Multiple Output Formats**: CSV and Excel with enhanced formatting
- **Quality Validation**: Automatic detection of missing critical information
- **Robust Error Handling**: Graceful handling of corrupted or unreadable PDFs
- **Progress Tracking**: Real-time processing status and success rates
- **Command Line Interface**: Flexible CLI with multiple options

## 📁 Project Structure
```
├── extract_info.py      # Core information extraction logic with AI patterns
├── main.py              # Main processing script with CLI interface
├── pdf_parser.py        # Multi-method PDF text extraction
├── utils.py             # Data formatting and file output utilities
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
└── sample_resumes/      # Input folder for PDF resumes
```

## 🔧 Prerequisites
- Python 3.7 or higher
- Required packages listed in `requirements.txt`

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Amit-123-source/AI-resume-parser.git
   cd resume-parser
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create input folder (optional):**
   ```bash
   python main.py --create-folder
   ```

## 💻 Usage

## Basic Usage

#### Step-1 : Keep resumes in **`sample_resumes/`** folder
#### Step-2 : Run the following command
```bash
python main.py
```
#### Process if resumes in custom folder
```bash
python main.py /path/to/your/resumes
```

## Advanced Options
#### Choose output format
```bash
python main.py --format csv           # CSV only
python main.py --format excel        # Excel only
python main.py --format both         # Both formats (default)
```
#### Specify custom output directory
```bash
python main.py --output-dir /path/to/output
```
#### Create input folder if it doesn't exist
```bash
python main.py --create-folder
```

### Command Line Options
- `folder_path`: Path to folder containing PDF resumes (default: `sample_resumes`)
- `--format, -f`: Output format (`csv`, `excel`, or `both`)
- `--output-dir, -o`: Custom output directory
- `--preview, -p`: Show preview of extracted data
- `--samples, -s`: Number of samples to preview (default: 2)
- `--create-folder`: Create input folder if it doesn't exist

## 📊 Example Output

### Enhanced CSV Output
The system now places the Resume Name at the end for better readability:

| Name          | Email               | Phone        | Skills                    | Work Experience           | Education                 | Projects                      | Hobbies         | Qualities           | Resume Name           |
|---------------|---------------------|--------------|---------------------------|---------------------------|---------------------------|-------------------------------|-----------------|---------------------|----------------------|
| John Doe      | john.doe@gmail.com  | (123) 456-7890 | Python, Java, SQL, React | Software Engineer at XYZ Corp | B.Sc. Computer Science, MIT | E-commerce Platform, AI Chatbot | Reading, Gaming | Leadership, Analytical | John_Doe_Resume.pdf   |
| Jane Smith    | jane.smith@yahoo.com | (987) 654-3210 | Machine Learning, Python | Data Scientist at ABC Inc | M.Sc. Data Science, Harvard | Recommendation System, NLP Tool | Travel, Photography | Creative, Problem-solving | Jane_Smith_Resume.pdf |

## 📈 Processing Summary

The tool provides comprehensive feedback:

```
🎯 Resume Information Extractor
============================================================
📁 Found 15 PDF files in 'sample_resumes'
🚀 Starting resume processing...

[1/15] ✅ John_Doe_Resume.pdf: Successfully extracted all key information
[2/15] ⚠️ Jane_Smith_Resume.pdf: Missing Phone
[3/15] ❌ Error processing Corrupted_File.pdf: Unable to extract text

============================================================
📊 PROCESSING SUMMARY
============================================================
Total files processed: 15
✅ Successful extractions: 13
❌ Failed extractions: 2
Success rate: 86.7%
```

## 🛠️ Advanced Features

### Smart Name Detection
- Multiple pattern recognition algorithms
- Exclusion of common false positives
- Scoring system for name candidates
- Support for various name formats and prefixes/suffixes

### Robust Skills Extraction
- Comprehensive keyword database (70+ technical and soft skills)
- Context-aware skill detection
- Section-based extraction for accuracy

### Intelligent Text Processing
- Multiple PDF extraction methods (pdfplumber + PyPDF2)
- Text cleaning and normalization
- Pattern-based information extraction

## 🚨 Error Handling & Validation

- **File Validation**: Automatic detection of corrupted PDFs
- **Data Quality Checks**: Missing field identification
- **Graceful Degradation**: Continues processing despite individual file errors
- **Detailed Logging**: Comprehensive error reporting and success tracking

## 📝 Output Files

The system generates several output files:
- `extracted_resume_data_X_resumes.csv` - CSV format data.
- `extracted_resume_data_X_resumes.xlsx` - Excel format with formatting.

## 🔍 Known Limitations

- **Image-based PDFs**: Requires OCR functionality (not included)
- **Complex Layouts**: May struggle with highly stylized resume formats
- **Non-English Resumes**: Optimized for English language resumes

## 🚀 Future Enhancements

- **OCR Integration**: Support for image-based PDFs
- **Web Interface**: Browser-based upload and processing
- **API Development**: RESTful API for integration
- **Machine Learning**: Adaptive extraction based on resume patterns
- **Multi-language Support**: International resume processing
- **Database Integration**: Direct database storage options

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.


## 🎉 Quick Start Example

### Step 1: Install dependencies
```bash
pip install -r requirements.txt
```
### Step 2: Run the Command
```bash
python main.py
```

### Expected Output Structure:
```
resume_extraction_results/
├── extracted_resume_data_X_resumes.csv
└── extracted_resume_data_X_resumes.xlsx
```
