import os
import glob
import shutil

image_path = r"E:\2222\Matting\20250107\PE-1\Fail"
out_path = r"./ShiftOutput"

if not os.path.exists(out_path):
    os.makedirs(out_path)

labels = [90, 95, 105, 110, 115, 120, 125, 130, 135, 140, 145, 147, 150, 158, 165, 168, 178, 181, 183, 192, 200, 210, 215, 220, 230]
images = glob.glob(os.path.join(image_path + "/*/*.BMP"))

for image in images:
    for label in labels:
        label = str(label)
        if label in image:
            print(image)
            curLabelFile = os.path.join(out_path + "/" + label)
            if not os.path.exists(curLabelFile):
                os.makedirs(curLabelFile)
            shutil.move(image, curLabelFile)
        

print(len(images))