import gradio as gr
import cv2
import numpy as np

def splitImgChannels(img, ratio_r, ratio_g, ratio_b, ratio_h, ratio_s, ratio_v, ratio_l, ratio_a, ratio_lab_b, ratio_sobel):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    r, g, b = cv2.split(img)
    hsvImg = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsvImg)
    labImg = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
    l, a, lab_b = cv2.split(labImg)

    sobel = cv2.Sobel(b, cv2.CV_64F, 1, 1) * 255.0

    mergeImg = (r * ratio_r + g * ratio_g + b * ratio_b 
                + h * ratio_h+ s * ratio_s+ v * ratio_v
                + l * ratio_l+ a * ratio_a+ lab_b * ratio_lab_b
                + sobel * ratio_sobel)
    # 将浮点图像转为 uint8，避免 Gradio 报错
    mergeImg = np.clip(mergeImg, 0, 255).astype(np.uint8)
    return mergeImg

if __name__ == "__main__":
    # 获取 gradio 安装路径
    print(gr.__path__)
    gr.close_all()  # 清除可能的历史状态
    gr.analytics_enabled = False  # ✅ 禁用 analytics（推荐）

    gr.Interface(inputs=["image", gr.Slider(minimum=-1, maximum=1, value=0), gr.Slider(minimum=-1, maximum=1, value=0),
                        gr.Slider(minimum=-1, maximum=1, value=0), gr.Slider(minimum=-1, maximum=1, value=0),
                        gr.Slider(minimum=-1, maximum=1, value=0), gr.Slider(minimum=-1, maximum=1, value=0),
                        gr.Slider(minimum=-1, maximum=1, value=0), gr.Slider(minimum=-1, maximum=1, value=0),
                        gr.Slider(minimum=-1, maximum=1, value=0), gr.Slider(minimum=-1, maximum=1, value=0)],
                outputs="image", 
                fn=splitImgChannels,
                live=True).launch()
