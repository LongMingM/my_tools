import cv2
import os
import glob
import numpy as np


img_dir = r"F:\F_Problems_solve\2025.03.21_常州时创半片工艺\卡点烧焦"
output_dir = r"D:\code_study\my_code\2024.11.29_allToolSets\output"

def imread_unicode(path):
    with open(path, 'rb') as f:
        img_array = np.asarray(bytearray(f.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return img
def safe_imwrite(path, img):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    ext = os.path.splitext(path)[1]  # 获取后缀，例如 .jpg
    success, encoded_img = cv2.imencode(ext, img)
    if success:
        encoded_img.tofile(path)
    else:
        print("Encoding failed:", path)



for root, dir, img_path in os.walk(img_dir):
    images = []
    for path in img_path:
        img = imread_unicode(os.path.join(root, path))
        if img is None:
            continue
        images.append(img)
        print(f"Read image: {os.path.join(root, path)}")
    print(f"images length: {len(images)}")

    for i in range(0, len(images), 2):
        img1 = images[i]
        img2 = images[i + 1]
        try:
            merged_img = cv2.vconcat([img1, img2])
        except:
            print(f"Error: {os.path.join(root, img_path[i])} and {os.path.join(root, img_path[i+1])} are not the same size.")
            continue
        safe_imwrite(os.path.join(output_dir, f"merged_{i}.jpg"), merged_img)
        print(f"Saved merged image to {os.path.join(output_dir, f'merged_{i}.jpg')}")