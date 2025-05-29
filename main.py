import os
import sys
import argparse
from pdf_parser import extract_text_from_pdf
from extract_info import extract_information
from utils import save_to_csv, save_to_excel, create_output_directory

def validate_folder_path(folder_path):
    """Validate if the folder path exists and contains PDF files"""
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"❌ The folder '{folder_path}' does not exist.")
    
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    if not pdf_files:
        raise ValueError(f"❌ No PDF files found in the folder '{folder_path}'.")
    
    print(f"📁 Found {len(pdf_files)} PDF files in '{folder_path}'")
    return pdf_files

def process_single_resume(pdf_path, file_name):
    """Process a single resume and return extracted data"""
    try:
        print(f"🔄 Processing: {file_name}")
        
        # Extract text from PDF
        text = extract_text_from_pdf(pdf_path)
        
        if not text or len(text.strip()) < 50:
            print(f"⚠️ Warning: Little or no text extracted from {file_name}")
            return None
        
        # Extract information
        extracted_data = extract_information(text)
        extracted_data['Resume Name'] = file_name
        
        # Validate extraction quality
        missing_fields = []
        important_fields = ['Name', 'Email', 'Skills', 'Work Experience']
        for field in important_fields:
            if not extracted_data.get(field):
                missing_fields.append(field)
        
        if missing_fields:
            print(f"⚠️ {file_name}: Missing {', '.join(missing_fields)}")
        else:
            print(f"✅ {file_name}: Successfully extracted all key information")
        
        return extracted_data
        
    except Exception as e:
        print(f"❌ Error processing {file_name}: {str(e)}")
        return None

def process_resumes(folder_path, output_format='both', output_dir=None):
    """Process all resume PDFs in a folder"""
    
    # Validate input
    pdf_files = validate_folder_path(folder_path)
    
    # Create output directory
    if output_dir is None:
        output_dir = create_output_directory()
    
    print(f"\n🚀 Starting resume processing...")
    print(f"📂 Input folder: {folder_path}")
    print(f"📤 Output directory: {output_dir}")
    print(f"📊 Output format: {output_format}")
    print("-" * 60)
    
    # Process each resume
    processed_data = []
    successful_count = 0
    failed_count = 0
    
    for i, pdf_file in enumerate(pdf_files, 1):
        print(f"\n[{i}/{len(pdf_files)}]", end=" ")
        pdf_path = os.path.join(folder_path, pdf_file)
        
        result = process_single_resume(pdf_path, pdf_file)
        
        if result:
            processed_data.append(result)
            successful_count += 1
        else:
            failed_count += 1
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 PROCESSING SUMMARY")
    print("=" * 60)
    print(f"Total files processed: {len(pdf_files)}")
    print(f"✅ Successful extractions: {successful_count}")
    print(f"❌ Failed extractions: {failed_count}")
    print(f"Success rate: {(successful_count/len(pdf_files)*100):.1f}%")
    
    if not processed_data:
        print("\n⚠️ No data extracted. Please check your PDF files.")
        return None
    
    # Save results
    print(f"\n💾 Saving results to {output_dir}...")
    
    base_filename = f"extracted_resume_data_{len(processed_data)}_resumes"
    
    if output_format in ['csv', 'both']:
        csv_path = os.path.join(output_dir, f"{base_filename}.csv")
        save_to_csv(processed_data, csv_path)
        print(f"✅ CSV saved: {csv_path}")
    
    if output_format in ['excel', 'both']:
        excel_path = os.path.join(output_dir, f"{base_filename}.xlsx")
        save_to_excel(processed_data, excel_path)
        print(f"✅ Excel saved: {excel_path}")
    
    return processed_data

def display_extraction_preview(data, num_samples=2):
    """Display a preview of extracted data"""
    if not data:
        return
    
    print(f"\n📋 EXTRACTION PREVIEW (showing {min(num_samples, len(data))} sample(s))")
    print("=" * 60)
    
    for i, resume_data in enumerate(data[:num_samples], 1):
        print(f"\n📄 Sample {i}: {resume_data.get('Resume Name', 'Unknown')}")
        print("-" * 40)
        
        preview_fields = ['Name', 'Email', 'Phone', 'Skills', 'Work Experience']
        for field in preview_fields:
            value = resume_data.get(field, 'Not found')
            if value and len(str(value)) > 100:
                value = str(value)[:100] + "..."
            print(f"{field}: {value}")

def setup_argument_parser():
    """Setup command line argument parser"""
    parser = argparse.ArgumentParser(
        description="📄 AI Resume Parser - Extract structured data from PDF resumes",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        'folder_path',
        nargs='?',
        default='sample_resumes',
        help='Path to folder containing PDF resume files'
    )
    
    parser.add_argument(
        '--format', '-f',
        choices=['csv', 'excel', 'both'],
        default='both',
        help='Output format for extracted data'
    )
    
    parser.add_argument(
        '--output-dir', '-o',
        type=str,
        help='Output directory for results (default: creates timestamped folder)'
    )
    
    parser.add_argument(
        '--preview', '-p',
        action='store_true',
        help='Show preview of extracted data'
    )
    
    parser.add_argument(
        '--samples', '-s',
        type=int,
        default=2,
        help='Number of sample extractions to preview'
    )
    
    parser.add_argument(
        '--create-folder',
        action='store_true',
        help='Create input folder if it doesn\'t exist'
    )
    
    return parser

def create_sample_folder_if_needed(folder_path, create_if_missing=False):
    """Create sample folder if needed"""
    if not os.path.exists(folder_path):
        if create_if_missing:
            os.makedirs(folder_path, exist_ok=True)
            print(f"📁 Created folder: {folder_path}")
            print("ℹ️ Please add your PDF resume files to this folder and run the script again.")
            return False
        else:
            print(f"❌ Folder '{folder_path}' does not exist.")
            print(f"💡 Use --create-folder flag to create it automatically.")
            return False
    return True

def main():
    """Main function with enhanced command line interface"""
    parser = setup_argument_parser()
    args = parser.parse_args()
    
    # Welcome message
    print("🎯 Resume Information Extractor")
    print("=" * 60)
    
    try:
        # Validate or create input folder
        if not create_sample_folder_if_needed(args.folder_path, args.create_folder):
            sys.exit(1)
        
        # Process resumes
        print(f"\n🔍 Scanning folder: {args.folder_path}")
        extracted_data = process_resumes(
            folder_path=args.folder_path,
            output_format=args.format,
            output_dir=args.output_dir
        )
        
        if extracted_data is None:
            print("\n❌ No data was extracted. Exiting.")
            sys.exit(1)
        
        # Show preview if requested
        if args.preview:
            display_extraction_preview(extracted_data, args.samples)
        
        # Final success message
        print("\n" + "=" * 60)
        print("🎉 PROCESSING COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print(f"📊 Total resumes processed: {len(extracted_data)}")
        print("💡 Check the output directory for your results.")
        
    except FileNotFoundError as e:
        print(f"\n{e}")
        print("💡 Tip: Use --create-folder to create the input folder automatically.")
        sys.exit(1)
    
    except ValueError as e:
        print(f"\n{e}")
        print("💡 Tip: Make sure your folder contains valid PDF resume files.")
        sys.exit(1)
    
    except KeyboardInterrupt:
        print("\n\n⏹️ Processing interrupted by user. Exiting gracefully...")
        sys.exit(1)
    
    except Exception as e:
        print(f"\n❌ Unexpected error occurred: {str(e)}")
        print("📧 Please report this issue if it persists.")
        sys.exit(1)

if __name__ == "__main__":
    main()
