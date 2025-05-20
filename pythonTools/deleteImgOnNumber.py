import glob
import shutil
import os

input_path = r"F:\dataSet\PE\尖山晶科\new - 副本"
out_path = r"F:\dataSet\PE\尖山晶科\new_20"

if not os.path.exists(out_path):
    os.makedirs(out_path)

for files in os.listdir(input_path):
    images = glob.glob(os.path.join(input_path, files, "*.PNG"))
    if len(images) > 20:
        for img in images:
            sub_out_path = os.path.join(out_path, files)
            os.makedirs(sub_out_path, exist_ok=True)
            shutil.copy(img, sub_out_path)