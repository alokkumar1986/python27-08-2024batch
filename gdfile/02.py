import os
import fitz  # PyMuPDF

def search_text_in_files(folder_path, search_text, search_text1):
    # Iterate through all files in the given folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if it's a file (skip directories)
        if os.path.isfile(file_path):
            try:
                # Process .txt files normally
                if filename.endswith('.txt'):
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        if search_text in content:
                            print(f"Text found in file: {filename}")
                
                # Process .pdf files using PyMuPDF
                elif filename.endswith('.pdf'):
                    # Open the PDF file using PyMuPDF
                    doc = fitz.open(file_path)
                    pdf_text = ""
                    for page_num in range(doc.page_count):
                        page = doc.load_page(page_num)  # Get a page
                        pdf_text += page.get_text()  # Extract text from the page
                    
                    # Check if the search_text is in the extracted PDF text
                    if search_text.lower() in pdf_text.lower() and search_text1.lower() in pdf_text.lower():
                        print(f"{filename}")

            except Exception as e:
                print(f"Could not read file {filename}: {e}")

if __name__ == "__main__":
    # Specify the folder path and the search text
    folder_path = "D:/python27-08-2024batch/gdfile"  # Replace with your folder path
    search_text = "github"
    search_text1 = "leetcode"  # Replace with the text you want to search for
    
    # Call the function to search for the text in all files
    search_text_in_files(folder_path, search_text, search_text1)
