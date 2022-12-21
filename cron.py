from sched import scheduler

import radar as radar
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import os
import time
import shutil


# 删除存放30天的文件
def del_files(dir_path, before_day=30):
    """
    :param dir_path: 文件路径
    :param before_day: 需要删除的天数
    :return:
    """
    before_sec = time.time() - 3600 * 24 * before_day
    for i in os.listdir(dir_path):
        filepath = "%s%s%s" % (dir_path, os.sep, i)
        if os.path.getmtime(filepath) < before_sec:
            try:
                if os.path.isfile(filepath):
                    os.remove(filepath)
                else:
                    shutil.rmtree(filepath)
            except Exception as e:
                print(e)


def times():
    print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))


if __name__ == '__main__':
    # dir_path = r'D:\桌面\数据0815'
    # # 5位的cron是从分钟开始计算,最后一位不能使用?需要使用*代替,times与delFiles是需要调用的函数名
    # sched = BlockingScheduler()
    # sched.add_job(times, CronTrigger.from_crontab('0/10 * * * *'))
    # # 删除30天前的文件
    # # args用于函数中进行传值,可以随机命名,只需要在后面传递参数即可
    # sched.add_job(del_files, CronTrigger.from_crontab('0 0 1/30 * *'), args=(dir_path, "30"))

    while True:
        data_time = radar.random_datetime('2022-07-01 00:00:00', '2022-09-28 12:00:00')
        print("INSERT INTO `rcb_pro`.`t_user_login_logs` ( `user_id`, `platform`, `create_time`, `create_by`, `update_time`, `update_by`, `is_del`) VALUES ( 268, 1, '%s', '武杨巍', '%s', '武杨巍', 1);"%(data_time,data_time))

