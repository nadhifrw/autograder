import os

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

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


# if u need to check headers in the Word documents, uncomment the code
# def header_count(path):
#     docx_list = find_docs(path)
#     for docx in docx_list:
#         filename = os.path.basename(docx)
#         doc = Document(docx)
#         num_sections = len(doc.sections)
#         print(f"Document {filename} has {num_sections} section(s)")


# Checking if there is header inside the docx
# def header_info(path):
#     docx_list = find_docs(path)
#     for docx in docx_list:
#         filename = os.path.basename(docx)
#         doc = Document(docx)
#         header = doc.sections[1].header
#         print(f"Header is found in the document {filename}, {header}")
#
#         header_text = ""
#         for paragraph in header.paragraphs:
#             header_text += paragraph.text
#
#         if header_text.strip():  # Check if not empty
#             print(f"Header found in {os.path.basename(docx)}: {header_text}")
#         else:
#             print(f"Header is empty in {os.path.basename(docx)}")


# Checking if there is header inside the docx
# alse making sure that the header contains the required text
def header_info(path):
    docx_list = find_docs(path)
    for docx in docx_list:
        filename = os.path.basename(docx)
        doc = Document(docx)

        # Check if document has multiple sections
        if len(doc.sections) > 1:
            header = doc.sections[1].header
            print(f"Checking section 2 header in {filename}")
            # TODO: If there are multiple sections, use only the first one, and check if the second header has anything inside. if yes then reduce the score
        else:
            header = doc.sections[0].header
            print(f"Only 1 section found, checking section 1 header in {filename}")

        # Get all text from header paragraphs
        header_text = ""
        for paragraph in header.paragraphs:
            header_text += paragraph.text

        # get all text from header tables
        for table in header.tables:
            for row in table.rows:
                for cell in row.cells:
                    header_text += cell.text + " "

        if header_text.strip():
            # print(f"Header found in {filename}: {header_text.lower()}")
            if (
                "universitas islam negeri sunan kalijaga" in header_text.lower()
                or "pusat teknologi informasi dan pangkalan data" in header_text.lower()
            ):
                print(f"Header contains required text: {header_text}")
            else:
                print(f"Header does not contain required text: {filename}")
        else:
            print(f"Header is empty in {filename}")


def body_info(path):
    docx_list = find_docs(path)
    for docx in docx_list:
        filename = os.path.basename(docx)
        doc = Document(docx)
        print(f"Body text in {filename}:")

        right_aligned_texts = ""  # Store right-aligned text as string

        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                if paragraph.alignment == WD_ALIGN_PARAGRAPH.RIGHT:
                    right_aligned_texts += paragraph.text + "\n"
                    print(f"Right-aligned text: {paragraph.text}")

        # You can now use right_aligned_texts string for further processing
        if "yogyakarta, 07 juni 2018" in right_aligned_texts.lower():
            print(f"Found right-aligned text containing the date in {filename}")
        else:
            print(f"Date not found in right-aligned text in {filename}")
