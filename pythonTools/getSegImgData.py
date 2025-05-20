import csv
import os
import pandas as pd
import cv2
from PIL import Image
import numpy as np

class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

def getImgSobel(img):
    sobel_X = cv2.Sobel(img, cv2.CV_16S, 1, 0)
    sobel_Y = cv2.Sobel(img, cv2.CV_16S, 0, 1)
    # 计算绝对值
    abs_sobel_X = np.absolute(sobel_X)
    abs_sobel_Y = np.absolute(sobel_Y)
    
    # 将16位有符号整型转换为8位无符号整型，并确保值在0-255范围内
    sobel_img = cv2.addWeighted(abs_sobel_X, 0.5, abs_sobel_Y, 0.5, 0)
    sobel_img = cv2.convertScaleAbs(sobel_img)
    return sobel_img
def showImg(image):
    Image.fromarray(image).show()


if __name__ =='__main__':

    image_path = r'F:\F_Problems_solve\test_Matting'

    images_list = []

    for root_img, dir_img, images_dir_list in os.walk(image_path):
        images_list = [i for i in images_dir_list if i.endswith('.jpg')
                       or i.endswith('.png') or i.endswith('.BMP') or i.endswith('.bmp')]

    print(len(images_list))

    csv_path = r'F:\F_Problems_solve\2024.12.12_胶印检膜色\20241212\test.csv'
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    if not os.path.exists(csv_path):
        print("csv file not exist, create one")
        try:
            with open(csv_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["blue", "green", "red", "hue", "sat", "value", "HLS_H", "HLS_L", "HLS_S", "label"])
        except Exception as e:
            print(f"create csv file failed at {csv_path} : {e}")
            exit()
    else:
        print("csv file existed")

    # 读取现有数据    
    exisiting_data = pd.read_csv(csv_path)
    rectWidth = 100
    rectHeight = 100
    for image_name in images_list:
        try:
            image_path = os.path.join(root_img, image_name)
            print(image_path)
            labelName = image_name[0]
            img= cv2.imread(image_path)
            height, width = img.shape[:2]
            b, g, r = cv2.split(img)

            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(img_hsv)

            img_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
            h_hls, l_hls, s_hls = cv2.split(img_hls)
            
            #get mask

            sobel_img = getImgSobel(v)

            ret, mask = cv2.threshold(sobel_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            #ret, mask = cv2.threshold(sobel_img, 10, 255, cv2.THRESH_BINARY)

            findContours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for curCon in findContours:
                cv2.drawContours(mask, [curCon], -1, (255, 255, 255), -1)
            mask = cv2.bitwise_not(mask)
            #showImg(mask)
            left = 100
            top = 500
            for i in range(left, width - 2* left, rectWidth):
                for j in range(top, height - 2 * top, rectHeight):
                    b_mean = cv2.mean(b[i:i + rectWidth, j: j + rectHeight], mask=mask[i:i + rectWidth, j: j + rectHeight])
                    g_mean = cv2.mean(g[i:i + rectWidth, j: j + rectHeight], mask=mask[i:i + rectWidth, j: j + rectHeight])
                    r_mean = cv2.mean(r[i:i + rectWidth, j: j + rectHeight], mask=mask[i:i + rectWidth, j: j + rectHeight])

                    h_mean = cv2.mean(h[i:i + rectWidth, j: j + rectHeight], mask=mask[i:i + rectWidth, j: j + rectHeight])
                    s_mean = cv2.mean(s[i:i + rectWidth, j: j + rectHeight], mask=mask[i:i + rectWidth, j: j + rectHeight])
                    v_mean = cv2.mean(v[i:i + rectWidth, j: j + rectHeight], mask=mask[i:i + rectWidth, j: j + rectHeight])

                    h_hsl_mean = cv2.mean(h_hls[i:i + rectWidth, j: j + rectHeight], mask=mask[i:i + rectWidth, j: j + rectHeight])
                    l_hsl_mean = cv2.mean(l_hls[i:i + rectWidth, j: j + rectHeight], mask=mask[i:i + rectWidth, j: j + rectHeight])
                    s_hsl_mean = cv2.mean(s_hls[i:i + rectWidth, j: j + rectHeight], mask=mask[i:i + rectWidth, j: j + rectHeight])
                    
                    color_mean = [b_mean[0], g_mean[0], r_mean[0], h_mean[0], s_mean[0], v_mean[0], 
                                  h_hsl_mean[0], l_hsl_mean[0], s_hsl_mean[0], labelName]
                    color_mean_series = pd.Series(color_mean, 
                                                  index=["blue", "green", "red", "hue", "sat", "value", "HLS_H", "HLS_L", "HLS_S", "label"])      
                    exisiting_data = exisiting_data.append(color_mean_series, ignore_index=True)
                    exisiting_data.to_csv(csv_path, index=False)

        except FileNotFoundError:
            exisiting_data = pd.DataFrame()
            exisiting_data.to_csv(csv_path, index=False)
        