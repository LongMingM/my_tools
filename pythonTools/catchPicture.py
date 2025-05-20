import pathlib
import glob
import shutil


path_dir = r"D:\project-solar-PE\client\polyImg\11"
path_dir = path_dir.replace("\\", "/")
path_dir = pathlib.Path(path_dir)
Total_image = glob.glob(str(path_dir) + '/**/*.BMP', recursive=True)
#移动这些图片到固定的文件夹下面
path_dir = r"E:\E_Problems_solve\2024.04.03_彩色卡点二次poly\dataImg\11"
path_dir = path_dir.replace("\\", "/")
path_dir = pathlib.Path(path_dir)
path_dir.mkdir(exist_ok=True)
for i in Total_image:
    print(i)
    shutil.copy(i, path_dir)
    print("移动成功")
