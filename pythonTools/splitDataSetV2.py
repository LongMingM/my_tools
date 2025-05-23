import os
import shutil
import random
import time

from pathlib import Path
from tqdm import tqdm
from matplotlib import pyplot as plt
from collections import defaultdict



class splitDataSet():
    def __init__(self, ori_path, output_path):
        self.ori_path = ori_path
        self.output_path = output_path

    def __len__(self):
        return len(self.ori_path)
    
    def createFiles(self):
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        for split in ['train', 'val', 'test']:
            if not os.path.exists(os.path.join(self.output_path, split)):
                os.makedirs(os.path.join(self.output_path, split), exist_ok=True)


    def splitFullDataset(self, train_ratio, val_ratio, test_ratio):
        self.createFiles()
        # 用于存储每个类在不同 split 中的数量
        class_counts = defaultdict(lambda: {'train': 0, 'val': 0, 'test': 0})

        for class_name in tqdm(os.listdir(self.ori_path)):
            class_path = os.path.join(self.ori_path, class_name)
            if not os.path.isdir(class_path):
                continue
                # 创建目标子文件夹
            for split in ['train', 'val', 'test']:
                os.makedirs(os.path.join(self.output_path, split, class_name), exist_ok=True)
            # 获取该类所有图片路径并打乱
            images = [f for f in os.listdir(class_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]
            random.shuffle(images)
            # 计算数量
            total = len(images)
            train_end = int(train_ratio * total)
            val_end = train_end + int(val_ratio * total)
            # 分配图片
            train_images = images[:train_end]
            val_images = images[train_end:val_end]
            test_images = images[val_end:]
            class_counts[class_name]['train'] = len(train_ratio * total)
            class_counts[class_name]['val'] = len(val_ratio * total)
            class_counts[class_name]['test'] = (total -  (train_ratio + val_ratio)* total)
            # 复制文件到相应目录
            for img_name in train_images:
                shutil.copy(os.path.join(class_path, img_name), os.path.join(self.output_path, 'train', class_name, img_name))
            for img_name in val_images:
                shutil.copy(os.path.join(class_path, img_name), os.path.join(self.output_path, 'val', class_name, img_name))
            for img_name in test_images:
                shutil.copy(os.path.join(class_path, img_name), os.path.join(self.output_path, 'test', class_name, img_name))

        print("数据集划分完成 ✅")

    def splitOneFile(self, splitFile = 'train', otherFile = 'val', split_ratio = 0.5):
        self.createFiles()

        if(splitFile == 'train'):
            train_path = os.path.join(self.ori_path, 'train')
            if not os.path.exists(train_path):
                return
            for class_name in tqdm(train_path):
                class_path = os.path.join(train_path, class_name)
                if not os.path.isdir(class_path):
                    continue
                # 获取该类所有图片路径并打乱
                images = [f for f in os.listdir(class_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]
                random.shuffle(images)
                # 计算数量
                total = len(images)
                train_end = int((1 - split_ratio) * total)
                train_images = images[:train_end]
                other_images = images[train_end:]
                # 复制文件到相应目录
                for img_name in train_images:
                    shutil.copy(os.path.join(class_path, img_name), os.path.join(self.output_path, 'train', class_name, img_name))
                for img_name in other_images:
                    shutil.copy(os.path.join(class_path, img_name), os.path.join(self.output_path, otherFile, class_name, img_name))



if  __name__ == '__main__':

    ori_path = r'D:\code_study\ML_CODE\dataSets\Classification\chinese-medicine-image'
    todayTime = time.strftime("%Y-%m-%d-%H", time.localtime())
    output_path = 'dataset' + todayTime
    train_ratio = 0.8
    val_ratio = 0.1
    test_ratio = 0.1
    random.seed(42)
    splitDataSet = splitDataSet(ori_path, output_path)
    splitDataSet.splitOneFile('train', 'val', 0.2)