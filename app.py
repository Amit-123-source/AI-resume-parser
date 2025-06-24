import gradio as gr
import os
import tempfile
import shutil
from typing import List, Dict, Any, Tuple
import json

from extract_info import extract_information
from pdf_parser import extract_text_from_pdf
from utils import save_to_csv, save_to_excel

class ResumeParserApp:
    def __init__(self):
        self.processed_data = []
        self.temp_dir = None
        
    def create_temp_directory(self):
        """Create a temporary directory for processing"""
        if self.temp_dir:
            shutil.rmtree(self.temp_dir, ignore_errors=True)
        self.temp_dir = tempfile.mkdtemp()
        return self.temp_dir
    
    def process_single_file(self, file_path: str, file_name: str) -> Dict[str, Any]:
        """Process a single PDF file and return extracted data"""
        try:
            text = extract_text_from_pdf(file_path)
            
            if not text or len(text.strip()) < 50:
                return {
                    'success': False,
                    'error': f'Little or no text extracted from {file_name}',
                    'data': None
                }
            
            extracted_data = extract_information(text)
            extracted_data['Resume_File'] = file_name
            
            return {
                'success': True,
                'error': None,
                'data': extracted_data
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f'Error processing {file_name}: {str(e)}',
                'data': None
            }
    
    def process_files(self, files: List[Any], progress=gr.Progress()) -> Tuple[str, str, str]:
        """Process multiple PDF files"""
        if not files:
            return "❌ No files uploaded", "", ""
        
        temp_dir = self.create_temp_directory()
        
        self.processed_data = []
        successful_count = 0
        failed_count = 0
        error_messages = []
        
        progress(0, desc="Starting processing...")
        
        for i, file in enumerate(files):
            progress((i + 1) / len(files), desc=f"Processing file {i + 1}/{len(files)}")
            
            file_name = os.path.basename(file.name)
            
            result = self.process_single_file(file.name, file_name)
            
            if result['success']:
                self.processed_data.append(result['data'])
                successful_count += 1
            else:
                failed_count += 1
                error_messages.append(result['error'])
        
        total_files = len(files)
        success_rate = (successful_count / total_files) * 100 if total_files > 0 else 0
        
        summary = f"""
        📊 **Processing Summary**
        
        - **Total files processed:** {total_files}
        - **✅ Successful extractions:** {successful_count}
        - **❌ Failed extractions:** {failed_count}
        - **📈 Success rate:** {success_rate:.1f}%
        """
        
        preview = self.generate_preview()
        
        error_report = "\n".join(error_messages) if error_messages else "No errors occurred."
        
        return summary, preview, error_report
    
    def generate_preview(self) -> str:
        """Generate a preview of extracted data"""
        if not self.processed_data:
            return "No data available for preview."
        
        preview_text = "📋 **Extraction Preview**\n\n"
        
        for i, resume_data in enumerate(self.processed_data[:], 1):
            preview_text += f"**📄 Resume {i}: {resume_data.get('Resume_File', 'Unknown')}**\n\n"
            
            preview_fields = ['Name', 'Email', 'Phone', 'Skills', 'Work Experience']
            for field in preview_fields:
                value = resume_data.get(field, 'Not found')
                if value and len(str(value)) > 100:
                    value = str(value)[:100] + "..."
                preview_text += f"- **{field}:** {value}\n"
            
            preview_text += "\n" + "-" * 50 + "\n\n"
        return preview_text
    
    def download_results(self, format_type: str) -> str:
        """Generate download file"""
        if not self.processed_data:
            return None
        
        
        if format_type == "CSV":
            filename = f"resume_data.csv"
            filepath = os.path.join(self.temp_dir, filename)
            save_to_csv(self.processed_data, filepath)
            return filepath
        
        elif format_type == "Excel":
            filename = f"resume_data.xlsx"
            filepath = os.path.join(self.temp_dir, filename)
            save_to_excel(self.processed_data, filepath)
            return filepath
        
        elif format_type == "JSON":
            filename = f"resume_data.json"
            filepath = os.path.join(self.temp_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.processed_data, f, indent=2, ensure_ascii=False)
            return filepath
        
        return None
    
    def get_statistics(self) -> str:
        """Generate detailed statistics"""
        if not self.processed_data:
            return "No data available for statistics."
        
        stats_text = "📊 **Detailed Statistics**\n\n"
        
        fields = ['Name', 'Email', 'Phone', 'Skills', 'Work Experience', 
                 'Education', 'Projects', 'Hobbies', 'Qualities']
        
        stats_text += "**Field Completion Rates:**\n\n"
        for field in fields:
            completed = sum(1 for item in self.processed_data if item.get(field))
            percentage = (completed / len(self.processed_data)) * 100
            stats_text += f"- **{field}:** {completed}/{len(self.processed_data)} ({percentage:.1f}%)\n"
        
        all_skills = []
        for resume in self.processed_data:
            skills = resume.get('Skills', '')
            if skills:
                all_skills.extend([skill.strip() for skill in skills.split(',')])
        
        if all_skills:
            from collections import Counter
            top_skills = Counter(all_skills).most_common(10)
            stats_text += "\n**Top 10 Most Common Skills:**\n\n"
            for skill, count in top_skills:
                stats_text += f"- **{skill}:** {count} resumes\n"
        
        return stats_text

app = ResumeParserApp()

custom_css = """
.gradio-container {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.main-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 10px;
    margin-bottom: 2rem;
    text-align: center;
}

.feature-card {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    border: none;
    border-radius: 15px;
    padding: 1.8rem;
    margin: 1rem 0;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
}

.feature-card h3 {
    background: linear-gradient(45deg, #ffffff, #f0f0f0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 700;
    font-size: 1.3em;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

.feature-card ul {
    list-style: none;
    padding: 0;
}

.feature-card li {
    color: #f9f7f7;
    font-weight: 500;
    margin: 0.7rem 0;
    padding-left: 1.5rem;
    position: relative;
    font-size: 1.05em;
    line-height: 1.4;
}

.feature-card li:before {
    content: "▶";
    position: absolute;
    left: 0;
    background: linear-gradient(45deg, #ffffff, #e0e0e0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: bold;
}

.instructions-card {
    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    border: none;
    border-radius: 15px;
    padding: 1.8rem;
    margin: 1rem 0;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
}

.instructions-card h3 {
    background: linear-gradient(45deg, #2c3e50, #34495e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 700;
    font-size: 1.3em;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

.instructions-card ul {
    list-style: none;
    padding: 0;
}

.instructions-card li {
    color: #34495e;
    font-weight: 500;
    margin: 0.7rem 0;
    padding-left: 1.5rem;
    position: relative;
    font-size: 1.05em;
    line-height: 1.4;
}

.instructions-card li:before {
    content: "✓";
    position: absolute;
    left: 0;
    color: #27ae60;
    font-weight: bold;
}

.success-text {
    color: #28a745;
    font-weight: bold;
}

.error-text {
    color: #dc3545;
    font-weight: bold;
}

.info-text {
    color: #17a2b8;
    font-weight: bold;
}

.upload-area {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: 3px dashed rgba(255,255,255,0.8) !important;
    border-radius: 20px !important;
    padding: 3rem 2rem !important;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
    box-shadow: 0 15px 35px rgba(102, 126, 234, 0.3);
}

.upload-area::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
}

.upload-area:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(102, 126, 234, 0.4);
    border-color: rgba(255,255,255,1) !important;
}

.upload-area * {
    position: relative;
    z-index: 1;
    color: #ffffff !important;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
}

.upload-area label {
    font-size: 1.3em !important;
    font-weight: 700 !important;
    margin-bottom: 1rem !important;
}
"""

def create_interface():
    with gr.Blocks(css=custom_css, title="Resume Parser", theme=gr.themes.Soft()) as demo:
        
        gr.HTML("""
        <div class="main-header">
            <h1>📄 Resume Parser</h1>
            <p>Extract structured data from PDF resumes with 🤖 AI-powered parsing</p>
        </div>
        """)
        
        with gr.Tabs():
            
            with gr.TabItem("📁 Upload & Process", elem_id="upload-tab"):
                with gr.Row():
                    with gr.Column(scale=2):
                        gr.HTML("""
                        <div class="instructions-card">
                            <h3>📋 Instructions</h3>
                            <ul>
                                <li>Upload one or more PDF resume files</li>
                                <li>Click 'Process Resumes' to extract data</li>
                                <li>Review results in the preview section</li>
                                <li>Download extracted data in your preferred format</li>
                            </ul>
                        </div>
                        """)
                        
                        file_upload = gr.File(
                            label="📎 Upload PDF Resume Files",
                            file_count="multiple",
                            file_types=[".pdf"],
                            elem_classes="upload-area"
                        )
                        
                        with gr.Row():
                            process_btn = gr.Button(
                                "🚀 Process Resumes", 
                                variant="primary", 
                                size="lg"
                            )
                            clear_btn = gr.Button(
                                "🗑️ Clear All", 
                                variant="secondary"
                            )
                    
                    with gr.Column(scale=1):
                        gr.HTML("""
                        <div class="feature-card">
                            <h3>✨ Features</h3>
                            <ul>
                                <li>🔍 AI-powered text extraction</li>
                                <li>📊 Structured data output</li>
                                <li>📈 Real-time processing</li>
                                <li>💾 Multiple export formats</li>
                                <li>📋 Detailed statistics</li>
                            </ul>
                        </div>
                        """)
                
                with gr.Row():
                    with gr.Column():
                        summary_output = gr.Markdown(label="Processing Summary")
                        
            with gr.TabItem("📊 Results & Preview", elem_id="results-tab"):
                with gr.Row():
                    with gr.Column(scale=2):
                        preview_output = gr.Markdown(
                            label="Data Preview",
                            value="Upload and process files to see preview here..."
                        )
                    
                    with gr.Column(scale=1):
                        with gr.Group():
                            gr.HTML("<h3>📥 Download Results</h3>")
                            
                            format_dropdown = gr.Dropdown(
                                choices=["CSV", "Excel", "JSON"],
                                value="Excel",
                                label="Select Format"
                            )
                            
                            download_btn = gr.Button(
                                "📥 Generate Download",
                                variant="primary"
                            )
                            
                            download_file = gr.File(
                                label="Download File",
                                visible=False
                            )
            
            with gr.TabItem("📈 Statistics", elem_id="stats-tab"):
                with gr.Row():
                    with gr.Column():
                        stats_output = gr.Markdown(
                            label="Detailed Statistics",
                            value="Process some resumes to see detailed statistics..."
                        )
                        
                        refresh_stats_btn = gr.Button(
                            "🔄 Refresh Statistics",
                            variant="secondary"
                        )
            
            with gr.TabItem("⚠️ Error Log", elem_id="error-tab"):
                error_output = gr.Markdown(
                    label="Error Messages",
                    value="No errors to display."
                )
        
        gr.HTML("""
        <div style="text-align: center; margin-top: 2rem; padding: 1rem; border-top: 1px solid #eee;">
            <p>💡 <strong>Tips:</strong> For best results, ensure your PDF files contain selectable text (not scanned images)</p>
            <p>🔧 Built with Gradio • 🤖 Powered by AI</p>
        </div>
        """)
        
        process_btn.click(
            fn=app.process_files,
            inputs=[file_upload],
            outputs=[summary_output, preview_output, error_output],
            show_progress=True
        )
        
        download_btn.click(
            fn=lambda format_type: app.download_results(format_type),
            inputs=[format_dropdown],
            outputs=[download_file]
        ).then(
            fn=lambda x: gr.File(visible=True if x else False),
            inputs=[download_file],
            outputs=[download_file]
        )
        
        refresh_stats_btn.click(
            fn=app.get_statistics,
            outputs=[stats_output]
        )
        
        clear_btn.click(
            fn=lambda: (None, "", "", "", "Process some resumes to see detailed statistics..."),
            outputs=[file_upload, summary_output, preview_output, error_output, stats_output]
        )
        
        process_btn.click(
            fn=app.get_statistics,
            outputs=[stats_output]
        )
    
    return demo

if __name__ == "__main__":
    demo = create_interface()
    
    demo.launch(
        server_name="0.0.0.0",  
        server_port=7860,       
        share=True,            
        debug=True,             
        show_error=True,       
        inbrowser=True,         
        favicon_path=None,      
        ssl_verify=False        
    )