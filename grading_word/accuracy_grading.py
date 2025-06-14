import os

from docx import Document

from checking_folder.checking_files import check_files_in_folder


def find_docs(path):
    # If path is a directory, find Word documents
    files = check_files_in_folder(path)
    # docx_test = []
    if files:
        docx_files = [
            f for f in files if f.endswith(".docx") and "word" in f.lower() and "-" in f
        ]
        for file in docx_files:
            filename = os.path.basename(file)
            print(f"file: {filename}")

        # for file in docx_files:
        #     print(f"Found Word document: {file}")
        # docx_test.append(docx_files)
        # print(f"Found {docx_files} Word documents in the directory.")
        print(f"Found {len(docx_files)} Word documents in the directory.")
        return docx_files
    else:
        print("Invalid path or not a Word document.")


def header_info(path):
    docx_list = find_docs(path)
    for docx in docx_list:
        filename = os.path.basename(docx)
        doc = Document(docx)
        header = doc.sections[0].header
        print(f"Header is found in the document {filename}, {header}")

        header_text = ""
        for paragraph in header.paragraphs:
            header_text += paragraph.text

        if header_text.strip():  # Check if not empty
            print(f"Header found in {os.path.basename(docx)}: {header_text}")
        else:
            print(f"Header is empty in {os.path.basename(docx)}")


def check_header_content(path, required_text="assignment"):
    docx_list = find_docs(path)
    for docx in docx_list:
        doc = Document(docx)
        header = doc.sections[0].header

        # get all text from header paragraphs
        header_text = ""
        for paragraph in header.paragraphs:
            header_text += paragraph.text + " "

        # get all text from header tables
        for table in header.tables:
            for row in table.rows:
                for cell in row.cells:
                    header_text += cell.text + " "

        filename = os.path.basename(docx)

        if not header_text.strip():
            print(f"❌ {filename}: header is empty")
        elif required_text.lower() in header_text.lower():
            print(f"✅ {filename}: header contains '{required_text}'")
        else:
            print(
                f"❌ {filename}: header missing '{required_text}'. found: {header_text.strip()}"
            )


# def header_info(path):
#     docx_list = find_docs(path)
#     for docx in docx_list:
#         doc = Document(docx)
#         header = doc.sections[0].header
#
#         # Get all text from header paragraphs
#         header_text = ""
#         for paragraph in header.paragraphs:
#             header_text += paragraph.text
#
#         # Check if header is not empty and contains specific text
#         if header_text.strip():  # Check if not empty
#             print(f"Header found in {os.path.basename(docx)}: {header_text}")
#
#             # Check for specific text (example: "Assignment" or "Student")
#             if "Assignment" in header_text or "Student" in header_text:
#                 print(f"Header contains required text: {header_text}")
#             else:
#                 print(f"Header does not contain required text: {header_text}")
#         else:
#             print(f"Header is empty in {os.path.basename(docx)}")


# def check_header_content(path, required_text="Assignment"):
#     docx_list = find_docs(path)
#     for docx in docx_list:
#         doc = Document(docx)
#         header = doc.sections[0].header
#
#         # Get all text from header paragraphs
#         header_text = ""
#         for paragraph in header.paragraphs:
#             header_text += paragraph.text
#
#         filename = os.path.basename(docx)
#
#         if not header_text.strip():
#             print(f"❌ {filename}: Header is empty")
#         elif required_text.lower() in header_text.lower():
#             print(f"✅ {filename}: Header contains '{required_text}'")
#         else:
#             print(
#                 f"❌ {filename}: Header missing '{required_text}'. Found: {header_text}"
#             )
