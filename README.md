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

# 根据imgaug 官网案例替换
 
 https://imgaug.readthedocs.io/en/latest/source/overview/meta.html#someof 

# strong-name.py 
可以批量的在你给定的路径下自定义命名

# split-file  脚本可以指定路径 把一个路径下的xml和图片放到2个不同的路径
# coco2yoyo.py 
环境配置：
         
         pip install pycocotools 
         
         pip install scikit-image

         
可以将coco数据集提取自定义类和图片，然后将标签转为xml格式 
# yolo2xml.py 
可以将yolo的标签改成xml格式转化 

# video.py 
可以将视频按自定义帧率提取图片到自定义路径 

# 2.py 
批量读取自定义图片路径下的文件，然后对其进行去噪和去模糊处理（高斯模糊，细节增强滤波，去噪），采用线程池提高了运行效率
# path.py 
1、保留、修改xml文件某标签内容
2、修改xml文件存放路径,文件名，照片来源等
3、本方法采用字符串方式解析打开,删除/保存xml文件
