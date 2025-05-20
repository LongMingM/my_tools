import os
import pathlib
import shutil
import glob
import random

input_dir = r"F:\F_Problems_solve\2025.01.17_尖山晶科新样本集\颜色分级 - 副本"
input_dir = pathlib.Path(input_dir)
out_dir = r"F:\F_Problems_solve\2025.01.17_尖山晶科新样本集\dataSets"
out_dir = pathlib.Path(out_dir)
out_train_path = out_dir / "train"
out_test_path = out_dir / "test"

def ensure_dirExists(dirPath):
    if not os.path.exists(dirPath):
        os.mkdir(dirPath)

ensure_dirExists(out_dir)
ensure_dirExists(out_train_path)
ensure_dirExists(out_test_path)


for fileNames in os.listdir(input_dir):
    ensure_dirExists(out_train_path / fileNames)
    ensure_dirExists(out_test_path / fileNames)
    
    totalImgs = glob.glob(str(input_dir / fileNames / "*"))
    random.shuffle(totalImgs)
    test_num = int(len(totalImgs) // 10) + 1
    for img in totalImgs[:test_num]:
        shutil.copy(img, out_test_path / fileNames)
    for img in totalImgs[test_num:]:
        shutil.copy(img, out_train_path / fileNames)