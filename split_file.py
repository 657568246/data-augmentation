import os
import shutil

def split_files_by_extension(input_path, output_txt_path, output_jpg_path):
    # if not os.path.exists(output_txt_path):
    #     os.makedirs(output_txt_path)

    # if not os.path.exists(output_jpg_path):
    #     os.makedirs(output_jpg_path)

    for filename in os.listdir(input_path):
        src_file = os.path.join(input_path, filename)
        if os.path.isfile(src_file):
            if filename.lower().endswith('.xml'):
                shutil.copy(src_file, os.path.join(output_txt_path, filename))
            elif filename.lower().endswith('.jpg'):
                shutil.copy(src_file, os.path.join(output_jpg_path, filename))

if __name__ == "__main__":
    input_path = r"F:\data\person.v1i.voc\train"        # 输入路径，包含jpg图片和txt文本的文件
    output_txt_path = r"F:\data\xml"   # 输出txt文本文件的路径
    output_jpg_path = r"F:\data\imge"   # 输出jpg图片文件的路径

    split_files_by_extension(input_path, output_txt_path, output_jpg_path)

    print("文件分割完成!")
