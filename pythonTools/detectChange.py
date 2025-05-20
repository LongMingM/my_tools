def load_dat(file_path):
    """加载 .dat 文件并返回字典对象"""
    params = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 假设每行格式为 "key=value"
            if ':' in line:
                key, value = line.strip().split(':', 1)
                params[key.strip()] = value.strip()
    return params

def compare_dat(dict1, dict2):
    """比较两个字典，返回有改动的参数及其值"""
    changes = {}
    
    # 遍历第一个字典
    for key in dict1:
        if key not in dict2:
            changes[key] = (dict1[key], 'Key removed')
        elif dict1[key] != dict2[key]:
            changes[key] = (dict1[key], dict2[key])
    
    # 检查第二个字典中是否有新键
    for key in dict2:
        if key not in dict1:
            changes[key] = ('Key added', dict2[key])

    return changes

def display_changes(changes):
    """显示检测到的变化"""
    for key, value in changes.items():
        print(f"Parameter: {key}")
        print(f"Old Value: {value[1]}")
        print(f"New Value: {value[0]}\n")

if __name__ == "__main__":
    file_path1 = 'D:\\hzleaper_auto_install\\aoi\SolarCellNB\\runner17\\x64\\config\\algorithm_6.json.dat'  # 第一个 .dat 文件路径
    file_path2 = 'D:\\hzleaper_auto_install\\aoi\SolarCellNB\\runner17\\x64\\config\\algorithm_6.json - 副本.dat'  # 第二个 .dat 文件路径

    # 加载两个 .dat 文件
    dat1 = load_dat(file_path1)
    dat2 = load_dat(file_path2)

    # 比较两个 .dat 对象
    changes = compare_dat(dat1, dat2)
    print(len(changes))
    # 显示结果
    if changes:
        display_changes(changes)
    else:
        print("No changes detected.")

    print(len(changes))