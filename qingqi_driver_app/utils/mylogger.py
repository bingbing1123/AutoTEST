# -*-coding:utf-8-*-

import logging
import ctypes
from qingqi_driver_app.project_config import *
import os

"""定义log的颜色"""

FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x01
FOREGROUND_GREEN = 0x02
FOREGROUND_RED = 0x04
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN
STD_OUTPUT_HANDLE = -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_color(color, handle=std_out_handle):
    b = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return b


"""定义handler的输出格式formatter"""


class MyLogger(object):

    def __init__(self, name='mylogger'):
        self.logger = logging.getLogger(name)

    def init_logger(self, file_path):
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(file_path, 'a', encoding='utf-8')
        stream_handler = logging.StreamHandler()

        self.logger.removeHandler(stream_handler)
        self.logger.removeHandler(file_handler)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def debug(self, message, color=FOREGROUND_BLUE):
        set_color(color)
        self.logger.debug(message)
        set_color(FOREGROUND_WHITE)

    def info(self, message, color=FOREGROUND_GREEN):
        set_color(color)
        self.logger.info(message)
        set_color(FOREGROUND_WHITE)

    def warn(self, message, color=FOREGROUND_YELLOW):
        set_color(color)
        self.logger.warn(message)
        set_color(FOREGROUND_WHITE)

    def error(self, message, color=FOREGROUND_RED):
        set_color(color)
        self.logger.error(message)
        set_color(FOREGROUND_WHITE)

    def critical(self, message, color=FOREGROUND_RED):
        set_color(color)
        self.logger.critical(message)
        set_color(FOREGROUND_WHITE)


if __name__ == '__main__':
    mylogger = MyLogger()
    print('pro', project_path)
    print(os.getcwd())
    #log_path ='1.txt'
    log_path = 'D:\\pycharm\\AutoTEST\\qingqi_driver_app\\logs\\TestCaselog\\11.txt'
    print('目录为', log_path)
    mylogger.init_logger(log_path)
    mylogger.debug('这是debug信息')
    mylogger.info('这是info信息')
    mylogger.warn('这是warning')
    mylogger.error('这是error信息')
    mylogger.critical('这是critical信息')
    config_file_path = os.path.split(os.path.realpath(__file__))[0]
    print('conf==', config_file_path)
