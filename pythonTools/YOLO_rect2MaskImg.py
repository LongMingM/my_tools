import os
import glob
import cv2
import json
import numpy as np
import pathlib as path

json_path = r"F:\dataSet\PE\QZYD\Raodu\20250306\1"
json_files = glob.glob(json_path + "/*.json")

for json_file in json_files:
    with open(json_file, "r") as f:
        data = json.load(f)
        shapes = data.get("shapes")
        mask_img = np.zeros((data["imageHeight"], data["imageWidth"]), dtype=np.uint8)
        for shape in shapes:
            label = shape.get("label")
            points = shape.get("points", [])
 
            if not points:
                print("No points found in the JSON file:", json_file)
                continue
            # 确保点的坐标是整数
            points = np.array(points, dtype=np.int32)
            if points.shape[0] == 2 and points.shape[1] == 2:
                cv2.rectangle(mask_img, tuple(points[0]), tuple(points[1]), color=255, thickness=-1)
            else:
                cv2.fillPoly(mask_img, [np.array(points)], color=255)
        # 保存或显示图像
        output_image_path = json_file.replace(".json", "_mask.bmp")
        output_image_path = path.Path(output_image_path)
        cv2.imwrite(output_image_path, mask_img)
        print(f"Saved image to {output_image_path}")
        