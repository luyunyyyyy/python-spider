# -*- coding: utf-8 -*-
import os

def image_to_string(img, cleanup=True, plus=''):
    # cleanup为True则识别完成后删除生成的文本文件
    # plus参数为给tesseract的附加高级参数
    os.popen('tesseract ' + img + ' ' + img + ' ' + plus)  # 生成同名txt文件
    text = file(img + '.txt').read().strip()
    if cleanup:
        os.remove(img + '.txt')
    return text


print image_to_string("image.jpg")

