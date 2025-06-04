import json
import chardet
import os
#读取.dat文件
def read_dat(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        print(f"检测到编码为: {encoding}")

        # 用检测出的编码解码
        text_data = raw_data.decode(encoding)
        json_data = json.loads(text_data)
        return json_data

def change_dat(data, inputKeyValue):
    new_data = dict(data)
    for key, value in inputKeyValue.items():
        new_data[key] = value
    print("数据已修改")
    return new_data

def write_dat(new_data, new_dat_path):
    #保存修改后的数据
    with open(new_dat_path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    dat_path = "./input/config"
    output_dat_path = "./output/config_Intel/"
    datList = os.listdir(dat_path)
    inputKeyValue = {"obj_use_objectDL_intel": "true",
                    "obj_objmodel_device_select": "1",
                    "obj_objmodel_name_intel": "PE_TY_BM_XS_202406140143_59741_3_2048_2048_31"}
    for dat in datList:
        if dat.endswith(".dat"):
            print(dat)
            data_path = os.path.join(dat_path, dat)
            data = read_dat(data_path)
            new_data = change_dat(data, inputKeyValue)
            if not os.path.exists(output_dat_path):
                os.makedirs(output_dat_path)
            new_dat_path = os.path.join(output_dat_path, dat)
            write_dat(new_data, new_dat_path)
