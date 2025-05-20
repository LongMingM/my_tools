import os
import json
import shutil


def select_img_json(img_path, in_json_path, out_img_path, out_json_path, label_name):
    with open(in_json_path, "r", encoding='utf-8') as f:
        # json.load数据到变量json_data
        json_data = json.load(f)

    for i in json_data['shapes']:
        if i['label'] == label_name:
            shutil.copy(img_path, out_img_path)
            shutil.copy(in_json_path, out_json_path)
            continue


if __name__ == "__main__":
    images_dir = 'D:\\seafile_data\\Seafile\\0710模型误检卡点烧焦\\'  # 图片文件夹
    jsons_dir = 'D:\\seafile_data\\Seafile\\0710模型误检卡点烧焦\\'  # json文件夹
    output_dir = 'D:\\image_data\\2023.7.12卡点烧焦筛选\\img_label27\\'  # 筛选文件所在的文件夹

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for root_img, dir_img, images_dir_list in os.walk(images_dir):
        images_list = [i for i in images_dir_list if i.endswith(
            '.jpg') or i.endswith('.png') or i.endswith('.bmp')]
        print(images_list)

    for root_json, dir_json, jsons_dir_list in os.walk(jsons_dir):
        jsons_list = [i for i in jsons_dir_list if i.endswith('.json')]
        print(jsons_list)

    label_name = '27'
    for image in images_list:
        try:
            img_path = root_img +"\\"+ image
            in_json_path = root_json +"\\" + image[:-4] + '.json'
            out_img_path = output_dir + image
            out_json_path = output_dir + image[:-4] + '.json'
            select_img_json(img_path, in_json_path, out_img_path, out_json_path, label_name)
        except Exception as e:
            print(e)
