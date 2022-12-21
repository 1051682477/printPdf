import random, string
import numpy as np


def verify():
    '''
    生成100个随机不重复的字符串
    :return:
    '''
    list1 = []
    new_list = []
    while 1:
        value = ''.join(random.sample(string.ascii_letters + string.digits, 6))  # 生成6位数随机验证码
        if value not in new_list:
            new_list.append(value)
            if len(new_list) == 100:
                break
        else:
            continue
    print(new_list, len(new_list))


def get_top_n(array, top_n):
    top_n_indexs = np.argsort(array)[:-top_n:-1]
    results = [array[index] for index in top_n_indexs]
    return results


def arr_test():
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([2, 4, 6, 8, 10])
    return list(a * b)


def upper_test():
    old_list = ['life', 'is', 'short', 'i', 'choose', 'python']
    new_list = list(map(str.upper, old_list))
    return new_list


if __name__ == '__main__':
    print(upper_test())
