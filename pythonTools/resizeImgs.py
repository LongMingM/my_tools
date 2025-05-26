import os
from PIL import Image

def resize_images(source_dir, target_dir, output_size=(256,256)):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith(('.png', '.bmp', '.jpg', '.jpeg', '.gif')):
                with Image.open(os.path.join(root, file)) as img:
                    img = img.resize(output_size, Image.Resampling.LANCZOS)

                    relative_path = os.path.relpath(root, source_dir)
                    target_subdir = os.path.join(target_dir, relative_path)

                    if not os.path.exists(target_subdir):
                        os.makedirs(target_subdir)

                    target_path = os.path.join(target_subdir, file)

                    img.save(target_path)


if __name__ == "__main__":
    source_path = r"D:\code_study\my_tools\pythonTools\output\2025-05-23-17"
    target_path = r"F:\dataSet\PE\YBDC\刻蚀印\matting\data512"
    output_size = (512, 512)
    resize_images(source_path, target_path, output_size)



