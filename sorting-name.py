# -*- coding:utf8 -*-
 
import os
import re
import shutil
from pathlib2 import Path
 
 
# 批量命名图片
def renamePic(srcImgDir):
    i=1
    for item in srcImgDir.rglob("*.jpg"):
        # 获取图片名
        imgName = item.name
        newName = str(i)+".jpg"
        i=i+1
        # 重命名
        print(f"prepare to rename {imgName}")
        item.rename(newName)
 
 
if __name__ == '__main__':
    # 文件路径--跟代码同目录
    srcImgPath = Path(r"F:\data\Fire images")
    renamePic(srcImgPath)