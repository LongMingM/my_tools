# import splitfolders
# import time
# data_path = r"F:\dataSet\PE\YBDC_overEtch_768\original\1226add"
# todayTime = time.strftime("%Y-%m-%d", time.localtime())
# dataNmae = "YBDC"
# output = "./output/" + dataNmae + todayTime
# splitfolders.ratio(data_path, output=output, seed=1337, ratio=(.8, 0, .2), group_prefix=None, move=False)


import splitfolders
import time
import pathlib as path
# 指定你的数据集所在的文件夹路径
dataset_path = r'F:\dataSet\PE\YBDC\刻蚀印\matting'
dataset_path = path.Path(dataset_path)
# 目标文件夹
dest_path = 'output'
todayTime = time.strftime("%Y-%m-%d-%H", time.localtime())
output = "./output/" + todayTime
# 调用 split 方法进行分割
splitfolders.ratio(dataset_path, output=output, ratio=(.8, .1, .1), group_prefix=None, move=False)