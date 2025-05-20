import glob
import shutil
import os
import pathlib as path

img_path = r"F:\dataSet\PE\QZYD\Raodu\dataSet_YOLO\val"
img_path = path.Path(img_path)
target_path = r"F:\dataSet\PE\QZYD\Raodu\dataSet_YOLO\label"

labelPath = r"F:\dataSet\PE\QZYD\Raodu\dataSet_YOLO\label"
labelPath = path.Path(labelPath)
labelFiles = []
for file in labelPath.glob("*.txt"):
    curTxt = file.name.split("\\")[-1]
    labelFiles.append(curTxt)
"""拷贝后缀文件"""
# for root, dir, files in os.walk(img_path):
#     for file in files:
#         if file.lower().endswith(".txt"):
#             shutil.copy(os.path.join(root, file), target_path)
#             print(f"Copy {file} to" ,target_path)

"""拷贝文件夹中对应的label文件"""

curImgPath = os.path.join(img_path, "images")
curLabelPath = os.path.join(img_path, "labels")
if not os.path.exists(curImgPath) and not os.path.exists(curLabelPath):
    os.makedirs(curImgPath)
    print(f"Create {curImgPath}")
    os.makedirs(curLabelPath)
    print(f"Create {curLabelPath}")

for root, dir, files in os.walk(img_path):
    for file in files:
        if file.lower().endswith(('.png', '.bmp', '.jpg', '.jpeg', '.gif')):
            shutil.move(os.path.join(root, file), curImgPath)

        txtfile = file.replace(".BMP", ".txt")
        if txtfile in labelFiles:
            shutil.copy(os.path.join(labelPath, txtfile), curLabelPath)
            print(f"Copy {txtfile} to" ,curLabelPath)
