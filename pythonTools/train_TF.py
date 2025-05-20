import numpy as np
import pandas as pd
from pathlib import Path
import os
import matplotlib.pyplot as plt
import tensorflow as tf
import seaborn as sns
from PIL import Image

from sklearn.metrics import classification_report, accuracy_score
from IPython.display import Markdown, display


os.environ["CUDA_VISIBLE_DEVICES"] = "0"
print(tf.__version__, tf.config.list_physical_devices('GPU'))

def printmd(string):
    display(Markdown(string))


if __name__ == '__main__':
    data_path = r"D:\code_study\my_code\2024.11.29_allToolSets\output"
    train_path = data_path + '\\train'
    test_path = data_path + '\\test'
    train_images_path = []
    train_dir = Path(train_path)
    for root, dirs, files in os.walk(train_path):
        for file in files:
            if file.lower().endswith(('.png', '.bmp', '.jpg')):
                img_path = os.path.join(root, file)
                train_images_path.append(img_path)