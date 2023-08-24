import os

folder_a = r'F:\data\test1\images' # 替换为文件夹A的路径
folder_b = r'F:\data\test1\annotations' # 替换为文件夹B的路径

# 获取文件夹A和B中的文件名列表
files_a = os.listdir(folder_a)
files_b = os.listdir(folder_b)

# 创建文件名前缀的集合
prefixes_a = set([filename.split('.')[0] for filename in files_a])
prefixes_b = set([filename.split('.')[0] for filename in files_b])

# 获取共同的文件名前缀
common_prefixes = prefixes_a.intersection(prefixes_b)

# 遍历文件夹A，保留共同前缀的文件，删除其它文件
for filename in files_a:
    prefix = filename.split('.')[0]
    if prefix in common_prefixes:
        continue
    file_path = os.path.join(folder_a, filename)
    os.remove(file_path)

# 遍历文件夹B，保留共同前缀的文件，删除其它文件
for filename in files_b:
    prefix = filename.split('.')[0]
    if prefix in common_prefixes:
        continue
    file_path = os.path.join(folder_b, filename)
    os.remove(file_path)





