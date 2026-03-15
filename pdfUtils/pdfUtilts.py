import os
from pypdf import PdfWriter

def merge_pdfs(input_folder, output_filename):
    # Initialise the PDF writer object
    merger = PdfWriter()
    
    # Get all PDF files from the folder and sort them alphabetically
    pdf_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.pdf')])
    
    if not pdf_files:
        print("No PDF files found in the specified folder.")
        return

    print(f"Found {len(pdf_files)} PDF files. Merging...")

    for filename in pdf_files:
        file_path = os.path.join(input_folder, filename)
        # Append each PDF file to the merger object
        merger.append(file_path)
        print(f"Added: {filename}")

    # Write the combined PDF to a single document
    with open(output_filename, "wb") as output_file:
        merger.write(output_file)
    
    merger.close()
    print(f"Success! Merged document saved as: {output_filename}")


if __name__ == "__main__":

    folder_path = 'inputFolder\\expericeneLetter'  # Replace with your folder path
    output_name = folder_path +"\\" + 'merged_ExperienceLetter.pdf'

    merge_pdfs(folder_path, output_name)
