#!/usr/bin/python3
# coding=utf-8
import logging
import os
import sys
# __file__ ： F:/pythonDemo/python_operation/log/logging.py   代表此文件
# os.path 代表当前文件的上级目录
# os.path.abspath 获取文件的全路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print("base_dir", BASE_DIR)
#print("sys.path ", sys.path)
#print("join", os.path.join(BASE_DIR, 'log', 'dataoperate.log'))
#print(os.path.dirname(__file__))


def public_log(level, logger_name='default.log', log_file=os.path.join(BASE_DIR, 'log','dataoperat.log')):
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # 创建控制台 handler
    ch = logging.StreamHandler()

    # 设置控制台输出时的日志等级
    ch.setLevel(logging.WARNING)

    # file Handler
    fh = logging.FileHandler(filename=log_file, encoding='utf-8')
    # set level
    fh.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s %(filename)s [line:%(lineno)d] %(name)s %(levelname)s %(message)s")

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger

log = public_log(level=logging.DEBUG)
log.info("info message")
log.debug("debug message")
log.warning("warning message")
log.error("error message")
log.critical("critical message")