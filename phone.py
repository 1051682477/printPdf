#!/user/bin/env python
# coding=utf-8
"""
@project : csdn
@author  : 剑客阿良_ALiang
@file   : cut_out_pic_tool.py
@ide    : PyCharm
@time   : 2022-01-20 10:38:53
"""
import os
import uuid
from ffmpy import FFmpeg


# 图片裁剪
def cut_out_pic(image_path: str, output_dir: str, start_pix: tuple, size: tuple):
    ext = os.path.basename(image_path).strip().split('.')[-1]
    if ext not in ['png', 'jpg']:
        raise Exception('format error')
    result = os.path.join(output_dir, '{}.{}'.format(uuid.uuid1().hex, ext))
    ff = FFmpeg(inputs={image_path: None},
                outputs={result: '-vf crop={}:{}:{}:{} -y'.format(size[0], size[1], start_pix[0], start_pix[1])})
    print(ff.cmd)
    ff.run()
    return result


if __name__ == '__main__':
    cut_out_pic(r'D:\桌面\图片\1655.jpg', r'C:\Users\huyi\Desktop', (1000, 1000), (1000, 1000))