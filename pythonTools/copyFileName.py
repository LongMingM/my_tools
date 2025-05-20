import os 

input_file_path = r"F:\dataSet\PE_OIOC\PE发包测试"
output_file_path = r"F:\dataSet\PE_OIOC\PE_重构离线结果图（截图）"

folds = os.listdir(input_file_path)
for fold in folds:
    foldpath = os.path.join(output_file_path, fold)
    if not os.path.exists(foldpath):
        os.makedirs(foldpath)

