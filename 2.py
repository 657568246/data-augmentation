import cv2
import os
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# 输入文件夹路径和输出文件夹路径
input_folder = r'F:\data\vedio\img'
output_folder = r'F:\data\vedio\out'

# 获取输入文件夹中的所有图片文件
image_files = [filename for filename in os.listdir(input_folder) if filename.endswith('.jpg') or filename.endswith('.png')]

# 设置线程池大小（根据实际情况调整）
num_threads = 8

# 处理单张图像的函数
def process_image(image_file):
    input_path = os.path.join(input_folder, image_file)
    output_path = os.path.join(output_folder, image_file)
    
    # 读取图像
    image = cv2.imread(input_path)
    
    # 高斯模糊
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    
    # 细节增强滤波
    detail_enhanced_image = cv2.addWeighted(image, 2.5, blurred_image, -1.5, 0)
    
    # 去噪
    denoised_image = cv2.fastNlMeansDenoisingColored(detail_enhanced_image, None, 10, 10, 7, 21)
    
    # 保存处理后的图像
    cv2.imwrite(output_path, denoised_image)

# 使用多线程处理图像并显示进度条
with ThreadPoolExecutor(max_workers=num_threads) as executor, tqdm(total=len(image_files)) as pbar:
    for _ in executor.map(process_image, image_files):
        pbar.update()

print("处理完成！")
