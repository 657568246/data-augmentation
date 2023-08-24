import cv2
import os
import shutil

def detect_blur_fft(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

def main(input_folder, output_folder, threshold):
    os.makedirs(output_folder, exist_ok=True)
    
    image_files = [filename for filename in os.listdir(input_folder) if filename.lower().endswith(('.jpg', '.png'))]
    
    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        image_quality = detect_blur_fft(gray)
        
        if image_quality < threshold:
            output_path = os.path.join(output_folder, image_file)
            shutil.move(image_path, output_path)
            print(f"Image moved: {image_path} -> {output_path} (Quality: {image_quality:.4f})")
        else:
            print(f"Image passed: {image_path} (Quality: {image_quality:.4f})")

if __name__ == "__main__":
    input_folder = r"F:\data\archive\images"  # Replace with your input folder
    output_folder = r"F:\data\test\output"  # Path to move images that don't meet the threshold
    threshold = 300  # Adjust the threshold as needed
    
    main(input_folder, output_folder, threshold)
