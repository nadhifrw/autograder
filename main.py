from checking_folder.checking_files import check_files_in_folder

# from grading_word.accuracy_grading import body_info
# from grading_word.accuracy_grading import checking_image
# from grading_word.accuracy_grading import table_info
# from grading_word.finding_docx import find_docs
# from scoring_point import add_accuracy_scores  # If you created this file
from grading_ppt.finding_pptx import find_pptx
from grading_ppt.ppt_grading import checking_theme, find_ppsx, ppt_slides

# from grading_word.formatting_grading import calculate_total_scores_formatting
# from grading_word.formatting_grading import bold_text
# from grading_word.formatting_grading import find_pdf


# TODO: make the grading for other file types like pptx, xlsx, etc
def main():
    path = "/Users/yolashaniaanggita/Documents/test_files"
    check_files_in_folder(path)
    find_pptx(path)
    ppt_slides(path)
    checking_theme(path)
    find_ppsx(path)
    # find_docs(path)
    # # header_info(path)
    # # body_info(path)
    # # checking_image(path)
    # # bold_text(path)
    # # table_info(path)
    # # total_scores = calculate_total_scores_formatting(path)
    #
    # # find_pdf(path)
    #
    # total_scores = add_accuracy_scores(path)
    #
    # # Optional: If you want to add other scores from scoring_point.py
    # # final_scores = add_accuracy_scores(path, other_scores)
    #
    # print(f"\nFinal scoring complete for {len(total_scores)} documents.")


if __name__ == "__main__":
    main()
