# import numpy as np

# -*- coding:utf-8 -*-
# 模块功能：对比txt和Excel文件差值，列对比或者列表对比都可以

import os
from openpyxl import load_workbook
import random


def excel_read(area, excel_file, sheet_name="sheet1"):
    """
    读取Excel
    :param area: 文件区域例如"A1:A5"
    :param excel_file:文件路径
    :param sheet_name: sheet页
    :return: list
    """
    workbook = load_workbook(filename=excel_file)
    # 2.通过 sheet 名称获取表格
    sheet = workbook[sheet_name]
    cell = sheet[area]
    lists = []
    for i in cell:
        for j in i:
            lists.append(j.value)
    return lists


def read_txt_diff(txt_file, old_list, linage, subscript, coding='GBK'):
    """
    读取银行卡号、姓名，查找差异值，银行上传
    :param txt_file: 文件地址txt
    :param old_list: 系统下载的银行卡号列表或者名字列表字符串形式
    :param linage: 行数
    :param subscript: 所取数值下标
    :param coding: 文件编码格式默认GBK
    :return:不相符的数据值
    """
    with open(txt_file, mode='r', encoding=coding) as f:
        bank_list = []
        bank_list_old = old_list
        for a in range(int(linage)):
            bank_no = f.readline().split("|")[int(subscript)]
            bank_list.append(bank_no)
        print(set(bank_list_old))
        print(set(bank_list))
        difference = list(set(bank_list_old).difference(set(bank_list)))
        return print(difference)
        # # method1:调用numpy库,直接异或。对比数字时使用
        # arr1 = np.array(bank_list)
        # arr2 = np.array(bank_list_old)
        # result1 = list(arr1 ^ arr2)
        # print(result1)


if __name__ == "__main__":
    # old_list1 = excel_read(excel_file='./excel/129612022060808.xlsx', area='F3:F154')
    # read_txt_diff('./txt/99999999-24231600808.txt', old_list1, 152, 5)
    # # path = './excel/9945202204.xlsx'
    # # getFileNames(path)
    # print()

    with open('./txt/99999999-2432232.txt', 'r') as  f:
        for n in range(44):
            print(f.readline().split('|')[5])




