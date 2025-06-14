from checking_folder.checking_files import check_files_in_folder
from grading_word.accuracy_grading import find_docs, header_info


def main():
    path = "/Users/yolashaniaanggita/Documents/test_files"
    check_files_in_folder(path)
    find_docs(path)
    header_info(path)


if __name__ == "__main__":
    main()
