input_path = r"C:\Users\Leaper\Desktop\test\requirements_py3.9_torch2.5.1+cu118_win64.txt"
output_path = r"C:\Users\Leaper\Desktop\test\requirements_torch.txt"
label = '@'

with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
    for line in infile:
        if label not in line:
            outfile.write(line)

print(f"处理完成！已保存到{output_path}")