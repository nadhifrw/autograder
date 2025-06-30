import os

from checking_folder.checking_files import check_files_in_folder


def find_pptx(path):
    # If path is a directory, find Word documents
    files = check_files_in_folder(path)
    # docx_test = []
    if files:
        # Putting all files that end with .docx and contain "word" in the filename
        pptx_files = [
            f for f in files if f.endswith(".pptx") and "ppt" in f.lower() and "-" in f
        ]
        for file in pptx_files:
            filename = os.path.basename(file)
            print(f"file: {filename}")

        # print(f"Found {len(docx_files)} Word documents in the directory.")
        return pptx_files
    else:
        print("Invalid path or not a Word document.")
