def screen(name):
    """
    :param name: 字段名称
    :return:
    """

    f = open('../txt/test.txt', 'r', encoding='utf-8')
    list1 = []
    lines = f.readlines()
    for lines in lines:
        if name in lines:
            print(lines)
            list1.append(lines)
    with open(name + '.txt', 'a', encoding='utf-8') as month_file:  # 提取后的数据文件
        for line in list1:
            s = (line)
            month_file.write(s)


def regular(fie):
    import re
    f = open(fie, "r", encoding='utf-8')
    data = f.readlines()
    f.close()
    for line in data:
        pattern = re.compile(r'(?<=sn:).+?(?=，returnResult)')
        string = str(line)
        sn = re.findall(pattern, string)
        f1 = open(fie+"sn.txt", "a+", encoding='utf-8')
        for sns in sn:
            f1.write(sns+'\n')
        f1.close()


if __name__ == '__main__':
    regular('./考勤照片不能为空.txt')
