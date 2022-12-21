# -*- coding: utf-8 -*-
# @Time : 2021/10/15 14:24
# @Author : wangyafeng
# @FileName: all.py
# @Email : yafengwang@dingtalk.com
# @Software: PyCharm
"""
思路：
1、连接数据库  查询目标  【读数据库】
2、下载pdf保存本地  转化为多张图片   pdf2image
3、多张图片合成一张图片
4、上传oss  拿到返回的路径
5、用拿到的路径 替换原来pdf的路径 【update数据库】
6、删除原下载的pdf、生成的多张图片、合成后的图片
"""

'''
注意：如果修改其他表中的pdf 请修改下边
1、修改myselect() 的c.execute("SELECT id,admin_certificate_url from t_enterprise where chcek_status ='1'")
2、修改updata() 的sql="UPDATE t_enterprise SET admin_certificate_url =%s WHERE id =%s"
3、如果为了保险一点  将修改前的id  和url保存到文件
如果忘记2  则会一直...857  857  857 
目前尚有2个bug
1、url如果为空  未进行处理，代码会报错 未定义 
    解决方案1 if myselect() is None  再加判断 ！=null   即 SELECT id,social_credit_code_url from t_enterprise where chcek_status ='1' and social_credit_code_url != '';
    解决方案2 sql时 添加where条件 剔除url 为空   
2、下载pdf进行打开的时候,如果pdf损坏 无法打开,则pdf2image会报错   这个需要在 im = Image.open(infile) 进行判断   判断是否读取文件错误
    即添加  except FileNotFoundError:  print('无法打开指定的文件!')   pass
'''

import pymysql
from pdf2image import convert_from_path, convert_from_bytes
import requests
import os
import PIL.Image as Image
import time

# 正式
db = pymysql.connect(
    host='rm-m5e1lup6qd395y43wmo.mysql.rds.aliyuncs.com',
    user='wyf',
    password='w30svCNY)d8^FbutOaNi',
    database='rcb_pro',
    charset='utf8'
)


# 测试
# db = pymysql.connect(
#     host='192.168.0.163',
#     user='xdm',
#     password='Xdmxdm@2021',
#     database='rcb_pro',
#     charset='utf8',
#     port=3306
# )


# 第一步
def myselect():
    c = db.cursor()
    '''
    '''
    # 执行SQL命令
    # 第一个
    # c.execute("SELECT id,social_credit_code_url from t_enterprise where chcek_status ='1'")
    # 第二个
    # c.execute("SELECT id,admin_certificate_url from t_enterprise where chcek_status ='1'")
    # 第三个
    # c.execute("SELECT id,certificate_url from t_enterprise_certificate")
    c.execute("SELECT id,state_url FROM t_project WHERE state_url is not null")
    for i in range(c.rowcount):
        record = c.fetchall()
        for x in range(0, len(record)):
            if 'pdf' in record[x][1]:
                # print(str(record[x][0]) + ' ' + record[x][1] + '\n')
                with open('state_url.txt', 'a+') as f:
                    f.write(str(record[x][0]) + ' ' + record[x][1] + '\n')
                return record[x][0], record[x][1]
    c.close()
    db.close()


# 第二步：
def getFile():
    if myselect() is None:
        print("执行完成......")
        quit()
    else:
        link = myselect()[1]
        # print("下载的地址是：", myselect()[0], myselect()[1])
        r = requests.get(link)
        with open("./tmp/abc.pdf", "wb+") as code:
            code.write(r.content)


def gettopng():
    # 定义图片大小convert_from_path, convert_from_bytes
    from pdf2image import convert_from_path, convert_from_bytes

    images = convert_from_path(pdf_path='./tmp/abc.pdf', poppler_path=r'G:\poppler-0.68.0_x86\poppler-0.68.0\bin')
    for i, image in enumerate(images):
        image.save
        image.save("./tmp/png/第%d页.png" % i, "PNG")
        time.sleep(2)

    # path = r'E:\PycharmProjects\pythonProject\PDF\venv\tmp'
    path = r'./tmp'
    for files in os.listdir(path):
        if files.endswith(".pdf"):
            os.remove(os.path.join(path, files))


# 第三步骤
def resize_by_width(infile, image_size):
    """按照宽度进行所需比例缩放"""
    im = Image.open(infile)
    (x, y) = im.size
    lv = round(x / image_size, 2) + 0.01
    x_s = int(x // lv)
    y_s = int(y // lv)
    print("x_s", x_s, y_s)
    out = im.resize((x_s, y_s), Image.ANTIALIAS)
    return out


def get_new_img_xy(infile, image_size):
    """返回一个图片的宽、高像素"""
    im = Image.open(infile)
    (x, y) = im.size
    lv = round(x / image_size, 2) + 0.01
    x_s = x // lv
    y_s = y // lv
    return x_s, y_s


# 定义图像拼接函数
def image_compose(image_colnum, image_size, image_rownum, image_names, image_save_path, x_new, y_new):
    to_image = Image.new('RGB', (image_colnum * x_new, image_rownum * y_new))  # 创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    total_num = 0
    for y in range(1, image_rownum + 1):
        for x in range(1, image_colnum + 1):
            from_image = resize_by_width(image_names[image_colnum * (y - 1) + x - 1], image_size)
            # from_image = Image.open(image_names[image_colnum * (y - 1) + x - 1]).resize((image_size,image_size ), Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * x_new, (y - 1) * y_new))
            total_num += 1
            if total_num == len(image_names):
                break
    return to_image.save(image_save_path)  # 保存新图


def get_image_list_fullpath(dir_path):
    file_name_list = os.listdir(dir_path)
    image_fullpath_list = []
    for file_name_one in file_name_list:
        file_one_path = os.path.join(dir_path, file_name_one)
        if os.path.isfile(file_one_path):
            image_fullpath_list.append(file_one_path)
        else:
            img_path_list = get_image_list_fullpath(file_one_path)
            image_fullpath_list.extend(img_path_list)
    return image_fullpath_list


def merge_images(image_dir_path, image_size, image_colnum):
    # 获取图片集地址下的所有图片名称
    image_fullpath_list = get_image_list_fullpath(image_dir_path)
    # print("image_fullpath_list", len(image_fullpath_list), image_fullpath_list)
    # 转换后的图片格式和地址
    image_save_path = r'{}.png'.format(image_dir_path)  # 图片转换后的地址
    # image_rownum = 4  # 图片间隔，也就是合并成一张图后，一共有几行
    image_rownum_yu = len(image_fullpath_list) % image_colnum
    if image_rownum_yu == 0:
        image_rownum = len(image_fullpath_list) // image_colnum
    else:
        image_rownum = len(image_fullpath_list) // image_colnum + 1

    x_list = []
    y_list = []
    for img_file in image_fullpath_list:
        img_x, img_y = get_new_img_xy(img_file, image_size)
        x_list.append(img_x)
        y_list.append(img_y)

    # print("x_list", sorted(x_list))
    # print("y_list", sorted(y_list))
    x_new = int(x_list[len(x_list) // 5 * 4])
    y_new = int(y_list[len(y_list) // 5 * 4])
    # print(" x_new, y_new", x_new, y_new)
    image_compose(image_colnum, image_size, image_rownum, image_fullpath_list, image_save_path, x_new, y_new)  # 调用函数


# 第四步骤
def upload_image():
    # 测试上传  正式测试用的同一个oss
    url = 'http://47.104.156.18:9030/attendance/file/uploadPlus'
    files = {'files': ('png.png', open('./tmp/png.png', 'rb'), 'image/png')}
    try:
        upload_request = requests.request('post', url, files=files)
        # print(upload_request.json()['records'][0]['url'])
    except IOError:
        print("IOError")
    else:
        return upload_request.json()['records'][0]['url']


# 第五步骤
def updata():
    c = db.cursor()
    # sql="UPDATE t_enterprise_certificate SET certificate_url =%s WHERE id =%s"
    sql = 'UPDATE t_project SET state_url =%s WHERE id =%s'
    val = (upload_image(), str(myselect()[0]))
    c.execute(sql, val)
    print("已执行")
    db.commit()


'''
执行
'''

while True:
    getFile()

    gettopng()

    image_dir_path = r'./tmp/png'  # 图片集地址
    image_size = 1024  # 每张小图片的大小
    image_colnum = 1  # 合并成一张图后，一行有几个小图
    merge_images(image_dir_path, image_size, image_colnum)

    upload_image()
    updata()
    # 第六步 删除
    for files in os.listdir(image_dir_path):
        if files.endswith(".png"):
            os.remove(os.path.join(image_dir_path, files))

    onepath = r'./tmp/png'
    for files in os.listdir(onepath):
        if files.endswith(".png"):
            os.remove(os.path.join(onepath, files))
