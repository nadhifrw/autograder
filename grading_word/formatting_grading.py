import os

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

from grading_word.accuracy_grading import find_docs


def text_alignment(path):
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


# TODO: Implement the rest of the grading logic for text alignment
