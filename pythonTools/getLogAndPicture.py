import json
import os
import shutil
json_path = 'Setting.json'
# json_path = os.path.join(os.getcwd(), json_path)
if not os.path.exists(json_path):
    print(f"Error: {json_path} does not exist.")
    exit(1)

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

log_path = data["logParam"]["savePathSoftwareLog"]
# target_file = os.path.join(os.getcwd(), 'collectCrash', 'logs')
target_file = os.path.join(os.getcwd(), 'collectCrash', 'logs')
if not os.path.exists(target_file):
    os.makedirs(target_file)
#复制日志
shutil.copytree(log_path, target_file, dirs_exist_ok=True)
print(f"复制日志到 {target_file}")


#复制图片
picture_path = data["sampleParam"]["sampleSavePath"]
picture_target_file = os.path.join(os.getcwd(), 'collectCrash', 'image')
# 存储找到的文件夹路径
found_folders = []
for root, dirs, files in os.walk(picture_path):
    if "AlgorithmCrash" in dirs:
        found_folders.append(os.path.join(root, "AlgorithmCrash"))

# 打印找到的文件夹路径
if found_folders:
    print("找到以下名为 'AlgorithmCrash' 的文件夹:")
    for folder in found_folders:
        print(folder)
        #将当前的文件夹名称与目标文件夹名称拼接
        temp_name = folder.replace(picture_path, picture_target_file)
        print(f"拼接后的路径: {temp_name}")
        #创建目标文件夹
        os.makedirs(temp_name, exist_ok=True)
        #复制图片
        shutil.copytree(folder, temp_name, dirs_exist_ok=True)
else:
    print("未找到名为 'AlgorithmCrash' 的文件夹")

