import redis

import time
import datetime


# 定义一个带参函数方法，里面设置时分秒，通过计算秒数来获取定时多久
def sleep_time(hour, min, sec):
    return hour * 3600 + min * 60 + sec


def labor_redis_select():
    r = redis.StrictRedis(host='r-m5ezi14cggvxp1082e.redis.rds.aliyuncs.com', port=6379, db=0,
                          password='mjO3EdH_NXeOxEi', decode_responses=True)
    r_dict = r.hgetall('attendance:record:risk')
    max_dict = []
    times = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    days = datetime.datetime.now().strftime('%Y_%m_%d')
    for n in r_dict:
        if int(r_dict[n]) >= 50:
            max_dict.append(n)
    if len(max_dict) != 0:
        f1 = open("./txt/labor_redis"+days+".txt", "a+", encoding='utf-8')
        f1.write('\n' + times + str(max_dict) + '\n')
        for num in range(len(max_dict)):
            rs = r.hdel('attendance:record:risk', max_dict[num])
            print("已删除：" + max_dict[num] + " " + times)
    return max_dict


if __name__ == '__main__':
    # 这是隔20分执行一次

    while 1 == 1:
        labor_redis_select()
        second = sleep_time(0, 5, 0)
        time.sleep(second)


