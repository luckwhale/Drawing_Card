# -*- coding = utf-8 -*-
# @Time : 2021/5/24 15:10
# Author : ZYK
# @File : produce_image.py
# @Software: PyCharm
from PIL import Image


def resize(w, h, w_box, h_box, pil_image):
    f1 = 1.0 * w_box / w
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)


# 以一个PIL图像对象打开
pil_imageklee = Image.open(r'./data/chouka/youla_chouka.PNG')

# 处理图像
def produce(image):
    w, h = image.size
    pil_image_resized = resize(w, h, 600, 600, image)
    pil_image_resized.save("./data/chouka/youla_chouka.gif")
    return


if __name__ == "__main__":
    produce(pil_imageklee)
