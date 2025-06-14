import os


def check_files_in_folder(path):
    if os.path.exists(path):
        print(f"file is existed: {path}")
        all_files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file != ".DS_Store":  # Skip system files
                    file_path = os.path.join(root, file)
                    all_files.append(file_path)
                    # print(f"{file} exists.")
                    # print(f"File found: {file_path}")
        return all_files
    else:
        print(f"Path does not exist: {path}")
        return None
