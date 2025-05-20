# from PIL import Image
# import os
# import time

# input_path = r"F:\F_Problems_solve\2025.01.07_尖山晶科分类错误\LP膜厚训练样本\rotatedImg170数据+5  180数据+10"
# output_path = r"F:\F_Problems_solve\2025.01.07_尖山晶科分类错误\LP膜厚训练样本"
# todayTime = time.strftime("%Y-%m-%d", time.localtime())
# output_path += todayTime
# for root, dir, imgs_path in os.walk(input_path):
#     for img_path in imgs_path:
#         endStr = {".png", ".bmp", ".jpeg"}
#         if img_path.lower().endswith(tuple(endStr)):
#             curImg_path = os.path.join(root, img_path)
#             try:
#                 with Image.open(curImg_path) as im:
#                 # 例如，逆时针旋转90度
#                     rotated_im = im.rotate(-90, expand=True)
#                     rel_path = os.path.relpath(root, input_path)
#                     output_dir = os.path.join(output_path, rel_path)
#                     os.makedirs(output_dir, exist_ok=True)
#                     rotated_imgName = "rotated_" + img_path
#                     img_path = os.path.join(output_dir, rotated_imgName)
#                     rotated_im.save(img_path)
#             except Exception as e:
#                 print(f"Error processing {curImg_path}: {e}")
#                 print(e)


from PIL import Image
import os
import time
from concurrent.futures import ThreadPoolExecutor

input_path = r"F:\F_Problems_solve\2025.01.07_尖山晶科分类错误\LP膜厚训练样本\rotatedImg170数据+5  180数据+10"
output_path = r"F:\F_Problems_solve\2025.01.07_尖山晶科分类错误\LP膜厚训练样本"
todayTime = time.strftime("%Y-%m-%d", time.localtime())
output_path += todayTime

# 定义处理单个图像的函数
def process_image(root, img_path):
    endStr = {".png", ".bmp", ".jpeg"}
    if img_path.lower().endswith(tuple(endStr)):
        curImg_path = os.path.join(root, img_path)
        try:
            with Image.open(curImg_path) as im:
                rotated_im = im.rotate(-90, expand=True)
                rel_path = os.path.relpath(root, input_path)
                output_dir = os.path.join(output_path, rel_path)
                os.makedirs(output_dir, exist_ok=True)
                rotated_imgName = "rotated_" + img_path
                img_path = os.path.join(output_dir, rotated_imgName)
                rotated_im.save(img_path)
        except Exception as e:
            print(f"Error processing {curImg_path}: {e}")

# 使用 ThreadPoolExecutor 来处理图像
with ThreadPoolExecutor(max_workers=7) as executor:  # 可以根据你的系统资源调整 max_workers
    for root, dirs, imgs_path in os.walk(input_path):
        for img_path in imgs_path:
            executor.submit(process_image, root, img_path)

print("All images have been processed.")