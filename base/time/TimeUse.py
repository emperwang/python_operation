#!/usr/bin/python3
# coding=utf-8

import time
import datetime
from dateutil.relativedelta import relativedelta

def time_use():
    # 获取 epoch seconds
    secs = time.time()
    stime_stract = time.localtime()
    gm_stract = time.gmtime()
    print("secs: ", secs, " , stime_stract: ", stime_stract, ", gm_stact: ", gm_stract)

    # 格式化时间
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", stime_stract)
    print("time_str : ", time_str)
    # 解析字符串中的时间
    parse_time = time.strptime("2021-02-2415:57:00", "%Y-%m-%d%H:%M:%S")
    print("parse_time: ", parse_time)

def datatime_use():
    # get now
    today = datetime.datetime.today()
    # parse from str
    parse_time = datetime.datetime.strptime("2021-02-2415:57:00", "%Y-%m-%d%H:%M:%S")
    # convert time to str
    today_str = datetime.datetime.strftime(today, "%Y-%m-%d%H:%M:%S")
    # print("today : ", today, "today_str :", today_str, ", parse time: ", parse_time)
    # plus one day
    plus_one_day = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    # plus one year
    plus_one_year = (datetime.datetime.strptime("2021-02-2415:57:00", "%Y-%m-%d%H:%M:%S") + relativedelta(years=1)).strftime("%Y-%m-%d %H:%M:%S")
    # plus one hour
    plus_one_hour = (datetime.datetime.strptime("2021-02-2415:57:00", "%Y-%m-%d%H:%M:%S") + datetime.timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S")
    print("plus one day: ", plus_one_day, "plus one year :", plus_one_year, " , plus one hour :", plus_one_hour)
    

def main():
    # time_use()
    datatime_use()


if __name__ == '__main__':
    main()