# 📄 Resume Parser

An AI-powered resume parsing application that extracts structured data from PDF resumes using natural language processing and machine learning techniques. Built with Python and Gradio for an intuitive web interface.

## 🌟 Features

- **🤖 AI-Powered Extraction**: Advanced text processing to extract key information from resume PDFs
- **📊 Structured Data Output**: Organizes extracted data into standardized fields
- **🎯 Multi-Format Export**: Export results in CSV, Excel, and JSON formats
- **📱 Web Interface**: User-friendly Gradio interface accessible via web browser
- **📈 Real-time Processing**: Live progress tracking and instant results
- **📋 Detailed Statistics**: Comprehensive analytics on extraction success rates
- **🔍 Data Preview**: Preview extracted data before downloading
- **⚡ Batch Processing**: Process multiple resume files simultaneously
- **📊 Error Reporting**: Detailed error logs for troubleshooting



*Experience the power of AI-driven resume parsing with our intuitive web interface*

## 📋 What Gets Extracted

The application intelligently extracts the following information from resumes:

| Field | Description |
|-------|-------------|
| **Name** | Full name of the candidate |
| **Email** | Email address |
| **Phone** | Phone number with formatting |
| **Skills** | Technical and soft skills |
| **Work Experience** | Employment history and positions |
| **Education** | Academic qualifications and degrees |
| **Projects** | Personal and professional projects |
| **Hobbies** | Personal interests and activities |
| **Qualities** | Professional qualities and traits |

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/resume-parser.git
cd resume-parser
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv resume_parser_env

# Activate virtual environment
# On Windows:
resume_parser_env\Scripts\activate

# On macOS/Linux:
source resume_parser_env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Requirements File

If `requirements.txt` doesn't exist, create it with:

```txt
gradio>=4.0.0
pandas>=1.5.0
openpyxl>=3.1.0
pdfplumber>=0.9.0
PyPDF2>=3.0.0
regex>=2023.0.0
```

## 🏃‍♂️ Usage

### Web Interface (Recommended)

1. **Start the Gradio App**:
   ```bash
   python app.py
   ```

2. **Access the Interface**:
   - Open your browser and go to `http://localhost:7860`
   - Or use the public sharing URL (if enabled)

3. **Upload & Process**:
   - Upload single or multiple PDF resume files
   - Click "Process Resumes" to start extraction
   - Review results in the preview section
   - Download extracted data in your preferred format

## 📁 Project Structure

```
resume-parser/
│
├── app.py                 # Gradio web application
├── main.py               # Command-line interface
├── extract_info.py       # Information extraction logic
├── pdf_parser.py         # PDF text extraction
├── utils.py              # Utility functions
├── requirements.txt      # Project dependencies
├── README.md            # Project documentation
└── sample_resumes/      # Sample resume files (Sample resumes)
```
## 📊 Sample Output
## CSV Output
```csv
Name,Email,Phone,Skills,Work Experience,Education
John Doe,john@email.com,(123) 456-7890,"Python, React, SQL","Software Engineer at Tech Corp","BS Computer Science"
Jane Smith,jane@email.com,(098) 765-4321,"Java, Spring, AWS","Senior Developer at StartupXYZ","MS Software Engineering"
```
## Excel Output

| Name          | Email               | Phone        | Skills                    | Work Experience           | Education                 | Projects                      | Hobbies         | Qualities           | Resume Name           |
|---------------|---------------------|--------------|---------------------------|---------------------------|---------------------------|-------------------------------|-----------------|---------------------|----------------------|
| John Doe      | john.doe@gmail.com  | (123) 456-7890 | Python, Java, SQL, React | Software Engineer at XYZ Corp | B.Sc. Computer Science, MIT | E-commerce Platform, AI Chatbot | Reading, Gaming | Leadership, Analytical | John_Doe_Resume.pdf   |
| Jane Smith    | jane.smith@yahoo.com | (987) 654-3210 | Machine Learning, Python | Data Scientist at ABC Inc | M.Sc. Data Science, Harvard | Recommendation System, NLP Tool | Travel, Photography | Creative, Problem-solving | Jane_Smith_Resume.pdf |

### Statistics Report
```
📊 PROCESSING SUMMARY
Total files processed: 10
✅ Successful extractions: 9
❌ Failed extractions: 1
📈 Success rate: 90.0%

Field Completion Rates:
- Name: 9/10 (90.0%)
- Email: 8/10 (80.0%)
- Skills: 9/10 (90.0%)
```
## 📈 Performance & Limitations

### Performance
- **Processing Speed**: ~1-3 seconds per resume
- **Accuracy**: 85-95% for standard resume formats
- **Supported Languages**: Primarily English
- **File Size**: Up to 10MB per PDF

### Current Limitations
- Works best with text-based PDFs (not scanned images)
- Optimized for English language resumes
- Complex layouts may affect extraction accuracy
- OCR not implemented for image-based PDFs

## 🛡️ Privacy & Security

- **No Data Storage**: Files are processed locally and not stored permanently
- **Temporary Processing**: Files are deleted after processing
- **No Network Dependencies**: Core extraction works offline
- **GDPR Compliant**: No personal data retention

## 🐛 Troubleshooting

### Common Issues

**Q: "No text extracted from PDF"**
```bash
# Solution: Ensure PDF contains selectable text
# Try converting scanned PDFs to text-searchable format
```

**Q: "Error processing file"**
```bash
# Check file permissions and PDF corruption
# Ensure PDF is not password protected
```

**Q: "Low extraction accuracy"**
```bash
# Ensure resume follows standard format
# Check if PDF has proper text encoding
```
### Python Dependencies
```txt
gradio>=4.0.0          # Web interface framework
pandas>=1.5.0          # Data manipulation
openpyxl>=3.1.0        # Excel file handling
pdfplumber>=0.9.0      # PDF text extraction
PyPDF2>=3.0.0          # Alternative PDF parser
regex>=2023.0.0        # Enhanced regex support
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Gradio Team** - For the amazing web interface framework
- **pdfplumber** - For robust PDF text extraction
- **pandas** - For efficient data manipulation
- **Open Source Community** - For inspiration and support

## 📞 Support

- 📧 **Email**: your.email@example.com
---

<div align="center">

**⭐ Star this repository if you found it helpful! ⭐**
