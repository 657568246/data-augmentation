# data-augmentation.py
Dataset and label preprocessing for tools:

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

# strong-name.py 
可以批量的在你给定的路径下自定义命名

# split-file  脚本可以指定路径 把一个路径下的xml和图片放到2个不同的路径
# coco2yoyo.py 
环境配置：
         
         pip install pycocotools 
         
         pip install scikit-image

         
可以将coco数据集提取自定义类和图片，然后将标签转为xml格式
