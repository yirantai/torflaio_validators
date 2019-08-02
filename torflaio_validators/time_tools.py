# -*- coding:utf-8 -*-

import time
import datetime
from dateutil import parser


def get_cur_timestamp():
    """ 获取当前时间戳
    """
    ts = int(time.time())
    return ts


def ts_to_datetime(ts):
    """ 将时间戳转换为datetime类型
    @param ts 时间戳
    """
    if not ts:
        return '00-00-00 00:00:00'
    dt = datetime.datetime.utcfromtimestamp(int(ts)) + datetime.timedelta(hours=8)
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def datetime_to_ts(dt):
    """datetime转时间戳"""
    if not dt:
        ts = int(time.time())
    elif isinstance(dt, str):
        ts = int(time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S')))
    elif isinstance(dt, datetime.datetime):
        ts = int(time.mktime(dt.timetuple()))
    else:
        ts = int(time.time())
    return ts


def datetime_to_display(dt):
    """ """
    if not dt:
        return '00-00-00 00:00:00'
    if not isinstance(dt, datetime.datetime):
        return '00-00-00 00:00:00'

    return dt.strftime("%Y-%m-%d %H:%M:%S")


def dt_str_to_datetime(dt):
    """时间字符串转时间格式"""
    if dt:
        dt_datetime = parser.parse(dt)
    else:
        dt_datetime = datetime.datetime.now()
    return dt_datetime


def datetime_start_end(date, date_start=False, date_end=False):
    """获取一天开始或结束时间"""
    if date_start:
        dt_datetime = datetime.datetime(year=date.year, month=date.month, day=date.day,
                                        hour=0, minute=0, second=0)
    elif date_end:
        dt_datetime = datetime.datetime(year=date.year, month=date.month, day=date.day,
                                        hour=23, minute=59, second=59)
    else:
        dt_datetime = date
    return dt_datetime
