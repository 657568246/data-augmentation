import os

def delete_files_with_prefix(folder_path, prefix):
    files_to_delete = [filename for filename in os.listdir(folder_path) if filename.startswith(prefix)]
    
    for file_to_delete in files_to_delete:
        file_path = os.path.join(folder_path, file_to_delete)
        os.remove(file_path)
        print(f"Deleted: {file_path}")

if __name__ == "__main__":
    folder_path = r"F:\data\VOC2028\VOC2028\JPEGImages"
    prefix = "PartA"
    delete_files_with_prefix(folder_path, prefix)
