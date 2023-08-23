import os
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

def process_xml(xmlFile, path, save_path, imgpath):
    tree = ET.ElementTree(file=os.path.join(path, xmlFile))
    root = tree.getroot()

    root[0].text = 'JPEGImages'
    root[1].text = xmlFile[:-3] + 'jpg'
    root[2].text = os.path.join(imgpath, xmlFile)

    for object in root.findall('object'):
        name = object.find('name').text
        if name == 'person':
            object.find('name').text = 'not wearing hat'
        else:
            if not (name in ["hat","person"]):
                root.remove(object)

    tree.write(os.path.join(save_path, xmlFile))

def change_xml():
    path = r"F:\data\VOC2028\VOC2028\Annotations"  # xml文件存放路径
    save_path = r"F:\data\VOC2028\VOC2028\txt"  # 修改后的xml文件存放路径
    imgpath = r"F:\data\VOC2028\VOC2028\JPEGImages"  # 新的照片path路径

    xml_files = [filename for filename in os.listdir(path) if filename.endswith('.xml')]

    with ThreadPoolExecutor() as executor:
        executor.map(lambda xmlFile: process_xml(xmlFile, path, save_path, imgpath), xml_files)

if __name__ == "__main__":
    change_xml()
