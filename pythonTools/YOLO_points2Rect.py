import json
import os
import glob
import numpy as np
import cv2
import pathlib as path

img_path = r"F:\dataSet\PE\QZYD\Raodu\20250306\1"
json_files = glob.glob(img_path + "/*.json")


for file in json_files:
    with open(file, "r") as f:
        data = json.load(f)
        shapes = data.get("shapes")
        # 保存或显示图像
        output_txt_path = file.replace(".json", ".txt")
        output_txt_path = path.Path(output_txt_path)
        for shape in shapes:
            label = shape.get("label")
            points = shape.get("points", [])
            if not points:
                print("No points found in the JSON file:", file)
                continue
            # 确保点的坐标是整数
            points = np.array(points, dtype=np.int32)
            rect = cv2.boundingRect(points)
            x_min = min(p[0] for p in points)
            y_min = min(p[1] for p in points)
            x_max = max(p[0] for p in points)
            y_max = max(p[1] for p in points)

            # 转换为YOLO格式
            img_width = data.get("imageWidth")
            img_height = data.get("imageHeight")
            x_center = ((x_min + x_max) / 2) / img_width
            y_center = ((y_min + y_max) / 2) / img_height
            width = (x_max - x_min) / img_width
            height = (y_max - y_min) / img_height

            # 写入YOLO格式的标注文件
            with open(output_txt_path, "w") as t:
                t.write(f"{label} {x_center} {y_center} {width} {height}\n")
            print(f"Saved image to {output_txt_path}")
