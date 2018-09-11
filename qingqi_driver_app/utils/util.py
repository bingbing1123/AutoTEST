# -*-coding:utf-8-*-


from qingqi_driver_app.utils.mylogger import MyLogger
from qingqi_driver_app.utils.configutil import ConfigUtil
import os
import random
import string
import time

import unittest


"""封装了有一些case共用的工具类"""


class Util(unittest.TestCase):

    """截图函数"""

    def __init__(self):
        global logger, conf
        self.logger = MyLogger()
        self.conf = ConfigUtil()

        logger = self.logger
        conf = self.conf

    def getScreenShot(self, driver, screen_path, test_name):
        logger.info('调用截图方法')
        img_dir = screen_path + test_name + '/'
        now_time = self.time_local()
        filename = self.mik_filename(img_dir, now_time,'.png')
        driver.get_screenshot_as_file(filename)

    """创建路径并返回文件夹路径"""

    @staticmethod
    def mik_director(dirname):

        logger.info('创建%s文件夹' % dirname)
        folder = os.path.exists(dirname)
        if not folder:
            os.makedirs(dirname)
        return dirname

    """创建文件名路径"""

    def mik_filename(self, dirname, filename, post):
        dirname = self.mik_director(dirname)
        path_f = dirname + filename + '.' + post
        self.logger.info('创建文件%s' % path_f)
        with open(path_f, 'w', encoding='utf-8') as f:
            f.close()
        return path_f

    """获取当前时间"""
    @staticmethod
    def time_local():
        today = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        return today

    @staticmethod
    def sleep(s):
        time.sleep(s)

    """随机生成字符"""

    @staticmethod
    def random_str(len):
        # for i in range(2):
        # 生成一个随机数
        # x = random.randint(0,9)
        # 利用sample方法生成字符串，x代表长度
        ran_str = ''.join(random.sample(string.ascii_letters, len))
        # 写入文件
        return ran_str

    """创建套件"""
    @staticmethod
    def suite(self, classname, testname):
        suite = unittest.TestSuite()
        tests = []
        for i in range(len(testname)):
            tests.append(classname(testname[i]))
        suite.addTests(tests)
        return suite

    @staticmethod
    def isElement(driver, idstr):
        flag = None
        try:
            driver.find_element_by_id(idstr)
            flag = True
        except Exception as e:
            logger.warn('find element exception')
            flag = False
        finally:
            return flag

    """获取屏幕大小"""

    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    """向上滑动"""

    @staticmethod
    def swipeUp(driver, t=2000, n=1):
        upper = driver.get_window_size()
        x1 = upper['width'] * 0.5  # x坐标
        y1 = upper['height'] * 0.75  # 起始y坐标
        y2 = upper['height'] * 0.25  # 终点y坐标
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)

    """向下滑动"""
    @staticmethod
    def swipeDown(driver, t=2000, n=1):
        lower = driver.get_window_size()
        x1 = lower['width'] * 0.5  # x坐标
        y1 = lower['height'] * 0.25  # 起始y坐标
        y2 = lower['height'] * 0.75  # 终点y坐标
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)

    """向左滑动"""
    @staticmethod
    def swipLeft(driver, t=2000, n=1):

        left = driver.get_window_size()
        x1 = left['width'] * 0.75
        y1 = left['height'] * 0.5
        x2 = left['width'] * 0.05
        for i in range(n):
            driver.swipe(x1, y1, x2, y1, t)

    """向右滑动"""
    @staticmethod
    def swipRight(driver, t=2000, n=1):

        right = driver.get_window_size()
        x1 = right['width'] * 0.05
        y1 = right['height'] * 0.5
        x2 = right['width'] * 0.75
        for i in range(n):
            driver.swipe(x1, y1, x2, y1, t)


if __name__ == '__main__':
    t = Util()
    # t.init_tool()
    # t.test()
    # D:\pycharm\AutoTEST\qingqi_driver_app\logs\test_te\20180907152312.txt
    t.mik_filename(
        'D:\\pycharm\\AutoTEST\\qingqi_driver_app\\logs\\test_te\\', '22',
        'txt')
