import os

def delete_xml_files(folder_path):
    xml_files = [filename for filename in os.listdir(folder_path) if filename.lower().endswith('.xml')]
    
    for xml_file in xml_files:
        xml_file_path = os.path.join(folder_path, xml_file)
        os.remove(xml_file_path)
        print(f"Deleted: {xml_file_path}")

if __name__ == "__main__":
    folder_path = r'F:\data\VOC2028\VOC2028\JPEGImages'
    delete_xml_files(folder_path)
