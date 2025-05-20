import matplotlib.pyplot as plt
from collections import Counter
import re
import pathlib

# 读取文本文件
file_path = r"D:\code_study\my_code\2024.11.29_allToolSets\dataSets\csv\\test.txt"  # 假设数据保存在 data.txt 文件中
file_path = pathlib.Path(file_path)
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read()

# 使用正则表达式提取日期
dates = re.findall(r'\d{8}', data)

# 提取月份
months = [date[4:6] for date in dates]
months = sorted(months)
print(len(months))
# 统计每个月的出现次数
month_counts = Counter(months)

# 绘制柱状图
plt.figure(figsize=(10, 6))
bars = plt.bar(month_counts.keys(), month_counts.values(), color='skyblue')
# 显示每个条形的具体数字
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, str(int(yval)), ha='center', va='bottom')
plt.xlabel('Month')
plt.ylabel('Count')
plt.title('Monthly Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()