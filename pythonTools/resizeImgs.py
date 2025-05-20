import os
from PIL import Image

def resize_images(source_dir, target_dir, output_size=(256,256)):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith(('.png', '.bmp', '.jpg', '.jpeg', '.gif')):
                with Image.open(os.path.join(root, file)) as img:
                    img = img.resize(output_size, Image.ANTIALIAS)

                    relative_path = os.path.relpath(root, source_dir)
                    target_subdir = os.path.join(target_dir, relative_path)

                    if not os.path.exists(target_subdir):
                        os.makedirs(target_subdir)

                    target_path = os.path.join(target_subdir, file)

                    img.save(target_path)


if __name__ == "__main__":
    source_path = r"F:\dataSet\PE\bigError_BM_XS_BlackGround"
    target_path = r"F:\dataSet\PE\bigError_BM_XS_BlackGround256"
    output_size = (256, 256)
    resize_images(source_path, target_path, output_size)



