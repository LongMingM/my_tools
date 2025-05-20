import os
import glob
import cv2
import numpy as np

input_dir = r"E:\样本库测试\PE\宜宾英发二期_黑色底板\pass\pass1"
target_dir = r"E:\样本库测试\PE\宜宾英发二期_黑色底板\pass\resizeImg_1024_2048"

def imread_unicode(path):
    with open(path, 'rb') as f:
        img_array = np.asarray(bytearray(f.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return img
def safe_imwrite(path, img):
    ext = os.path.splitext(path)[1]  # 获取后缀，例如 .jpg
    success, encoded_img = cv2.imencode(ext, img)
    if success:
        encoded_img.tofile(path)
    else:
        print("Encoding failed:", path)

for root, dir, files in os.walk(input_dir):
    for file in files:
        if file.lower().endswith(".bmp"):
            img_path = os.path.join(root, file)
            print(f"Processing image: {img_path}")
            img = imread_unicode(img_path)
            img = cv2.resize(img, (1024, 2048))
            safe_imwrite(os.path.join(target_dir, file), img)
            print(f"Saved image to {os.path.join(target_dir, file)}")