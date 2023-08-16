
import os
import concurrent.futures
from tqdm import tqdm  # 导入tqdm

def rename_jpg_file(old_path, new_path):
    os.rename(old_path, new_path)

def process_files(target_path):
    jpg_files = [filename for filename in os.listdir(target_path) if filename.lower().endswith('.jpg')]    
    with concurrent.futures.ThreadPoolExecutor() as executor, tqdm(total=len(jpg_files), desc="Renaming files", unit="file") as pbar:  
    # 它可以并行地处理多个文件重命名任务。executor.submit方法会将每个任务提交给线程池，并且线程池会自动管理并发执行。这样可以提高效率，特别是当处理大量文件时。
    # 请注意，多线程并发处理会使用更多的系统资源，所以请根据实际情况调整线程数量和资源限制。
        for i, filename in enumerate(jpg_files):
            old_path = os.path.join(target_path, filename)
            new_filename = "partA" + str(i) + ".jpg"
            new_path = os.path.join(target_path, new_filename)
            executor.submit(rename_jpg_file, old_path, new_path)
            pbar.update(1)  # 更新进度条
    #我添加了一个名为 pbar 的 tqdm 进度条对象，并在循环内使用 pbar.update(1) 来更新进度条。这将会在处理每个文件后更新进度条的状态。

if __name__ == "__main__":
    target_path = r"F:\data\pic"
    process_files(target_path)
    print("批量重命名完成!")
