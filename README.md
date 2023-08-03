# data-augmentation
Dataset and label preprocessing for tools

pip install imgaug

pip install six numpy scipy matplotlib scikit-image opencv-python imageio tqdm

# 使用方法 
 IMG_DIR = "F:\\data\\imge\\"  输入图片路径
 XML_DIR = "F:\\data\\xml\\"   输入xml路径  
 AUG_XML_DIR = "F:\\data\\aab\\xml\\"  # 存储增强后的XML文件夹路径
 AUG_IMG_DIR = "F:\\data\\aab\\img\\"  # 存储增强后的图片文件夹路径  
 AUGLOOP = 2  # 设置每张图片增强的数量  

seq = iaa.Sequential([ 
自定义内容添加！ 
    ])  

#根据imgaug 官网案例替换
 https://imgaug.readthedocs.io/en/latest/source/overview/meta.html#someof 
