# -*-coding:utf-8-*-

from qingqi_driver_app.utils.configutil import ConfigUtil
from qingqi_driver_app.utils.mylogger import MyLogger
from qingqi_driver_app.utils.util import Util
from qingqi_driver_app.project_config import *

from appium import webdriver
import unittest


class CommonUtil(unittest.TestCase):
    def __init__(self):
        self.conf = ConfigUtil()
        self.logger = MyLogger()
        self.conf.read_config(app_resourceconf_path)
        self.mik_directors()
        self.mikcase_logpath()

    """创建文件夹"""

    @staticmethod
    def mik_directors():
        log_dir = Util().mik_director(log_path)
        screen_dir = Util().mik_director(screen_path)
        report_dir = Util().mik_director(report_path)
        return log_dir, screen_dir, report_dir

    def mikcase_logpath(self, testname='TestCaselog'):
        directors = self.mik_directors()
        file_path = directors[0]
        file_path = self.mik_filepath(file_path, testname, 'txt')
        self.logger.init_logger(file_path)
        #return file_path

    """
    def mikTestcase_logpath(self, classname):
        print('调用了此方法')
        tescases = unittest.getTestCaseNames(classname, prefix='test')
        for i in tescases:
            print('i的值为==', i)
            file_path = self.mikcase_logpath(i)
            return file_path
    """
    def mikreport_path(self):
        directors = self.mik_directors()
        file_path = directors[2]
        report_file_path = self.mik_filepath(file_path, 'report', 'html')
        return report_file_path

    @staticmethod
    def mik_filepath(director, testcase_name, pos):
        director_p = director + testcase_name + '\\'
        director_path = Util().mik_director(director_p)
        now_time = Util().time_local()
        file_path = Util().mik_filename(director_path, now_time, pos)
        return file_path

    """获取配置文件里ID section key对应的value值"""

    def get_id_value(self, idstr, sectionstr='ID'):
        return self.conf.get(sectionstr, idstr)

    """获取配置文件里TEXT section key对应的value值"""

    def get_text_value(self, text, sectionstr='TEXT'):
        return self.conf.get(sectionstr, text)

    """获取配置文件里ACCOUNT section key对应的value值"""

    def get_account(self, accountstr, sectionstr='ACCOUNT'):
        return self.conf.get(sectionstr, accountstr)

    """启动Appium的一些准备信息"""

    def desired_capabilities(self):

        desired_caps = {}
        desired_caps['deviceName'] = self.conf.get('CAPS', 'deviceName')
        desired_caps['platformName'] = self.conf.get('CAPS', 'platformName')
        desired_caps['platformVersion'] = self.conf.get(
            'CAPS', 'platformVersion')
        desired_caps['appPackage'] = self.conf.get('CAPS', 'appPackage')
        desired_caps['appActivity'] = self.conf.get('CAPS', 'appActivity')
        driver = webdriver.Remote(
            self.conf.get(
                'CAPS',
                'driver'),
            desired_caps)
        return driver

    def getscreenshot(self, driver, testname):
        directors = self.mik_directors()
        Util().getScreenShot(driver, directors[1], testname)

    def login(self, driver, testname):
        driver.implicitly_wait(5)

        el = driver.find_element_by_id(self.get_id_value('USERNAMEID'))

        driver.implicitly_wait(5)
        self.logger.info('已进入到登录页面')
        el.click()

        el.send_keys(self.get_account('USERNAME'))
        el2 = driver.find_element_by_id(self.get_id_value('PWDID'))
        el2.send_keys(self.get_account('PWD'))

        driver.implicitly_wait(1)
        login = driver.find_element_by_id(self.get_id_value('LOGINID'))
        login.click()
        driver.implicitly_wait(5)

        self.logger.info('已登录成功')

        driver.implicitly_wait(10)
        b = Util().isElement(
            driver, self.get_id_value('UPDATEFRAME'))
        if b:
            driver.find_element_by_id(
                self.get_id_value('UPDATEFRAME')).click()
            self.logger.info('已点击了升级弹框')
        driver.implicitly_wait(5)

        # print('登录截图前')
        #self.getscreenshot(driver, testname)
        # driver.implicitly_wait(10)
        # print('登录截图后')

        # driver.implicitly_wait(10)
        self.logger.info('点击完升级弹框已等待10ms')

    def logout(self, driver, testname):
        self.logger.info('退出登录')
        driver.find_element_by_id(self.get_id_value('LOGOUTID')).click()
        ot = driver.find_element_by_id(self.get_id_value('OUT_FRAMEID'))
        self.getscreenshot(driver, testname)

        driver.find_element_by_id(self.get_id_value('SUREID')).click()
        driver.implicitly_wait(3)
        li = driver.find_element_by_id(self.get_id_value('LOGINID'))
        self.getscreenshot(driver, testname)


if __name__ == '__main__':
    unittest.main()
    """
    c = CommonUtil()
    c.conf.read_config('C:\\Users\\lenovo\\Desktop\\config1.ini')
    n = c.conf.get('db_config_CD', 'host')
    print(n)
    """
    """
    c = CommonUtil()
    c.conf.read_config('C:\\Users\\lenovo\\Desktop\\app_resource_config.ini')#'D:\\pycharm\\AutoTEST\\qingqi_driver_app\\test_cases\\app_resource_config.ini')
    n = c.conf.get('ID', 'PWDID')
    print(n)
    #c.get_id_value('PWDID')
    #c.test()
    """
    #c = CommonUtil()
    #n = c.get_id_value('PWDID')
    # print(n)
