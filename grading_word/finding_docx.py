import os

from checking_folder.checking_files import check_files_in_folder


def find_docs(path):
    # If path is a directory, find Word documents
    files = check_files_in_folder(path)
    # docx_test = []
    if files:
        # Putting all files that end with .docx and contain "word" in the filename
        docx_files = [
            f for f in files if f.endswith(".docx") and "word" in f.lower() and "-" in f
        ]
        for file in docx_files:
            filename = os.path.basename(file)
            print(f"file: {filename}")

        print(f"Found {len(docx_files)} Word documents in the directory.")
        return docx_files
    else:
        print("Invalid path or not a Word document.")
