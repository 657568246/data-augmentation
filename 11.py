import os
import xml.etree.ElementTree as ET

# 源文件夹路径
folder1_path = r"F:\data\test2\xml-1"
folder2_path = r"F:\data\test2\xml-2"

# 目标文件夹路径
output_folder_path = r"F:\data\test2\new-xml"

# 遍历第一个文件夹
for filename in os.listdir(folder1_path):
    if filename.endswith('.xml'):
        xml_file1_path = os.path.join(folder1_path, filename)
        xml_file2_path = os.path.join(folder2_path, filename)
        
        # 读取第一个XML文件
        tree1 = ET.parse(xml_file1_path)
        root1 = tree1.getroot()
        
        # 读取第二个XML文件
        tree2 = ET.parse(xml_file2_path)
        root2 = tree2.getroot()
        
        # 创建一个新的根元素，用于合并
        merged_root = ET.Element('merged_data')
        
        # 将两个XML文件的内容添加到合并后的根元素下
        for element in root1:
            merged_root.append(element)
        
        for element in root2:
            merged_root.append(element)
        
        # 创建一个新的XML树
        merged_tree = ET.ElementTree(merged_root)
        
        # 生成合并后的XML文件名（与原文件名相同）
        merged_xml_name = filename
        
        # 合并后的XML文件的完整路径
        merged_xml_path = os.path.join(output_folder_path, merged_xml_name)
        
        # 保存合并后的XML文件
        merged_tree.write(merged_xml_path)
