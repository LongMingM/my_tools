input_path = r"D:\code_study\ML_CODE\myCode\classification\Rainbow_Classification\requirements.txt"
output_path = r"D:\code_study\ML_CODE\myCode\classification\Rainbow_Classification\requirements2.txt"
label = '@'

with open(input_path, 'r', encoding='utf-16') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
    for line in infile:
        if label not in line:
            outfile.write(line)

print(f"处理完成！已保存到{output_path}")