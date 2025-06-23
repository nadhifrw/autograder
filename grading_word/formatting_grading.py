import os

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

from grading_word.accuracy_grading import find_docs


def text_alignment(path):
    docx_list = find_docs(path)
    text_alignment_score = {}
    for docx in docx_list:
        filename = os.path.basename(docx)
        doc = Document(docx)
        print(f"Body text in {filename}:")
        score = 0

        right_aligned_texts = ""  # Store right-aligned text as string

        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                if paragraph.alignment == WD_ALIGN_PARAGRAPH.RIGHT:
                    right_aligned_texts += paragraph.text + "\n"
                    print(f"Right-aligned text: {paragraph.text}")

        # You can now use right_aligned_texts string for further processing
        if "yogyakarta, 07 juni 2018" in right_aligned_texts.lower():
            print(f"Found right-aligned text containing the date in {filename}")
            score += 5
        else:
            print(f"Date not found in right-aligned text in {filename}")

        text_alignment_score[filename] = score

    return text_alignment_score


def bold_text(path):
    """Check for bold text in the document"""
    docx_list = find_docs(path)
    # text_alignment = {}
    bold_text_score = {}

    for docx in docx_list:
        filename = os.path.basename(docx)
        doc = Document(docx)
        print(f"Checking bold text in {filename}:")
        score = 0

        # for paragraph in doc.paragraphs:
        #     if paragraph.text.strip():
        #         for run in paragraph.runs:
        #             if run.bold:
        #                 print(f"Bold text found: {run.text}")
        #                 score += 1
        bold_texts = ""  # Store right-aligned text as string

        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                for run in paragraph.runs:
                    if run.bold:
                        bold_texts += paragraph.text + "\n"
                        print(f"Bold text found: {paragraph.text}")
                        break
        # You can now use right_aligned_texts string for further processing
        # if "yogyakarta, 07 juni 2018" in bold_texts.lower():
        #     print(f"Found right-aligned text containing the date in {filename}")
        #     score += 5
        # else:
        #     print(f"Date not found in right-aligned text in {filename}")
        if "assalamualaikum wr. wb." in bold_texts.lower():
            print(f"Found bold text containing the greeting in {filename}")
            score += 5
        if "wassalamualaikum wr. wb." in bold_texts.lower():
            print(f"Found bold text containing the closing greeting in {filename}")
            score += 5

        bold_text_score[filename] = score
        # print(f"Total bold text score for {filename}: {score}")

    return bold_text_score
    # return print(bold_texts)


# TODO: Implement the rest of the grading logic for text alignment
def calculate_total_scores_formatting(path):
    """Calculate total scores for all documents"""
    body_alignment = text_alignment(path)
    bold_scores = bold_text(path)

    total_scores = {}

    # Get all unique filenames
    all_files = set(body_alignment.keys()) | set(bold_scores.keys())

    for filename in all_files:
        total = body_alignment.get(filename, 0) + bold_scores.get(filename, 0)
        total_scores[filename] = total
        # print(f"📄 {filename} — Total Score: {total}")

    return total_scores
