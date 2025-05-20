import pathlib
import glob
import shutil
from PIL import Image

path_dir = r"E:\2222\Matting\20240407\111"
path_dir = path_dir.replace("\\", "/")
path_dir = pathlib.Path(path_dir)
Total_image = glob.glob(str(path_dir) + '/**/*.PNG', recursive=True)
#移动这些图片到固定的文件夹下面
path_dir = r"E:\E_Problems_solve\2024.03.12_楚雄晶科膜厚检测出现错误\Matting\正常"
path_dir = path_dir.replace("\\", "/")
path_dir = pathlib.Path(path_dir)
path_dir.mkdir(exist_ok=True)
for i in Total_image:

    print(i)
    shutil.move(i, path_dir)
    print("移动成功")
