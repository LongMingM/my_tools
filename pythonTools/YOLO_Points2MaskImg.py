import os
import glob
import cv2
import json
import numpy as np
import path

json_path = r"F:\F_Problems_solve\2025.02.27_newProject\20250228"
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
            cv2.fillPoly(mask_img, [np.array(points)], color=255)

        # 保存或显示图像
        output_image_path = json_file.replace(".json", "_mask.bmp")
        output_image_path = path.Path(output_image_path)
        cv2.imwrite(output_image_path, mask_img)
        print(f"Saved image to {output_image_path}")
        