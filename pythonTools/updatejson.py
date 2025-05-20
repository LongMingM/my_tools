# import json
# import datetime

# json_file = r"D:\project-solar-PE\client\algorithmVersion.json"

# # 读取json文件内容


# with open(json_file, 'r') as file:
#     data = json.load(file)

# # 获取当天日期并格式化为指定格式
# today = datetime.date.today().strftime("%Y%m%dRT")

# # 修改"Version"字段的值为当天日期
# data["算法更新日期"]["Version"] = today

# # 写入修改后的内容回json文件
# with open(json_file, 'w') as file:
#     json.dump(data, file, indent=4)

# print(f"Updated Version to {today}")

import json
import datetime
json_file = "D:/project-solar-PE/client/algorithmVersion.json"
#读取json文件
with open(json_file, 'r', encoding='utf-8') as file:
    data = json.load(file)
    #获取当天日期并格式化为指定格式
today = datetime.date.today().strftime("%Y%m%dRT")
    #修改"Version"字段的值为当天日期
data["算法更新日期"]["Version"] = today
    #写入修改后的内容回json文件
with open(json_file, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
print(f"Updated Version to {today}")


