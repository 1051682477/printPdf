# 先全部翻转，再翻转一次字符串并添加空格
def reversed_string(a_string:str):
    str = " "
    return str.join((a_string.split(' ')[::-1]))[::-1]


def reversed_string_two(a_string:str):
    word_list = a_string.split(' ')
    for i in range(len(word_list)):
        word_list[i] = word_list[i][::-1]
    s = " ".join(word_list)
    return s


def str_nums(a_string: str):
    if len(a_string) < 1:
        return "输入错误"
    elif a_string.isalpha():
        dicts = {}
        for i in a_string:
            if i not in dicts:
                dicts[i] = 1
            else:
                dicts[i] += 1
        final_str = ''
        for i in dicts.items():
            temp = i[0] + '%d' % i[1]
            final_str += temp
        return final_str
    else:
        return "输入错误"


def one(sta):
    def two():
        return "12122"+sta
    return two()


if __name__ == '__main__':
    # print(reversed_string("Let's take LeetCode contest"))
    # # print(reversed_string_two("Let's take LeetCode contest"))
    # print(str_nums("aaaaaffd"))
    # print(str_nums("aaabbbbbbsab"))
   print(one("55"))