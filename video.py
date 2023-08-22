import cv2
import os
import concurrent.futures
from tqdm import tqdm

def get_unique_filename(output_folder, base_filename, extension):
    count = 1
    while True:
        filename = f'{base_filename}_{count:04d}.{extension}'
        full_path = os.path.join(output_folder, filename)
        if not os.path.exists(full_path):
            return full_path
        count += 1

def extract_frames(video_path, output_folder, frame_rate):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    fps = cap.get(cv2.CAP_PROP_FPS)
    interval_frames = int(fps * frame_rate)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    with tqdm(total=total_frames // interval_frames) as pbar:
        while True:
            ret, frame = cap.read()

            if not ret:
                break

            if frame_count % interval_frames == 0:
                unique_filename = get_unique_filename(output_folder, 'frame', 'jpg')
                cv2.imwrite(unique_filename, frame)
                pbar.update(1)

            frame_count += 1

    cap.release()

def main():
    video_path = r'F:\data\vedio\video.mp4'
    output_folder = r'F:\data\vedio\img'
    frame_rate = 3

    os.makedirs(output_folder, exist_ok=True)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(extract_frames, video_path, output_folder, frame_rate)

if __name__ == "__main__":
    main()

