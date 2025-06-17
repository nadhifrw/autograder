from checking_folder.checking_files import check_files_in_folder
from grading_word.accuracy_grading import body_info
from grading_word.finding_docx import find_docs
from scoring_point import add_accuracy_scores  # If you created this file


def main():
    path = "/Users/yolashaniaanggita/Documents/test_files"
    check_files_in_folder(path)
    find_docs(path)
    # header_info(path)
    body_info(path)

    total_scores = add_accuracy_scores(path)

    # Optional: If you want to add other scores from scoring_point.py
    # final_scores = add_accuracy_scores(path, other_scores)

    print(f"\nFinal scoring complete for {len(total_scores)} documents.")


if __name__ == "__main__":
    main()
