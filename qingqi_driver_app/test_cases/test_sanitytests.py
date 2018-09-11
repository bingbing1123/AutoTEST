# -*-coding:utf-8-*-


from qingqi_driver_app.test_cases.common_util import CommonUtil
from qingqi_driver_app.utils.mylogger import MyLogger
from qingqi_driver_app.utils.util import Util
import unittest

# sys.path.append("../")


class QingqiCase(unittest.TestCase):

    def setUp(self):
        global logger, driver, common_util, util, directors
        util = self.util = Util()
        common_util = self.common_util = CommonUtil()
        logger = self.logger = MyLogger()
        driver = self.driver = self.common_util.desired_capabilities()

    """轻汽司机版登录验证"""

    def test_login(self):
        logger.info(
            '**********************执行登录的测试用例***************************')
        common_util.login(driver, 'test_alogin')
        driver.implicitly_wait(5)
        print('测试方法中执行')
        home = driver.find_element_by_id(
            common_util.get_id_value('HOMETEXTID'))
        home_text = home.text
        logger.info('解放行字样有没有%s' % home_text)
        common_util.getscreenshot(driver,'test_alogin')
        driver.implicitly_wait(5)
        self.assertEqual(
            home_text,
            common_util.get_text_value('HOMETEXT'),
            '未进入到主页')
        logger.info('校验登录页面的解放行字样')

        logger.info('已完成结果截图')
        driver.implicitly_wait(10)

    #@unittest.skip
    def test_modifyname(self):
        logger.info(
            '**********************修改用户名的测试用例***************************')
        common_util.login(driver, 'test_modifyname')

        logger.info('点击我的页面')
        driver.implicitly_wait(10)
        driver.find_element_by_id(common_util.get_id_value('MYID')).click()
        driver.implicitly_wait(10)

        phone_number = driver.find_element_by_id(
            common_util.get_id_value('PHONEID'))
        common_util.getscreenshot(driver, 'test_modifyname')
        self.assertEqual(
            common_util.get_account('USERNAME'),
            phone_number.text,
            '登录的账号与显示的账号不一致')
        driver.implicitly_wait(10)

        logger.info('点击头像进入账号设置')
        driver.find_element_by_id(common_util.get_id_value('IMAGEID')).click()
        driver.implicitly_wait(10)
        common_util.getscreenshot(driver, 'test_modifyname')
        account_setting = driver.find_element_by_id(
            common_util.get_id_value('ACCOUNT_SETTINGID')).text
        self.assertEqual(
            account_setting,
            common_util.get_text_value(
                'ACCOUNT_SETTINGIDTEXT'),
            '未进入到账号设置页面')

        logger.info('点击姓名输入框进入设置姓名页面')
        ne = driver.find_element_by_id(common_util.get_id_value('NAMEID'))
        ne.click()
        driver.implicitly_wait(10)
        common_util.getscreenshot(driver, 'test_modifyname')
        setting_name = driver.find_element_by_id(
            common_util.get_id_value('SETTING_NAMEID')).text
        self.assertEqual(
            setting_name,
            common_util.get_text_value(
                'SETTING_NAMETEXT'),
            '未进入到设置界面')

        logger.info('修改姓名,清空后输入随机的4位字符')
        se = driver.find_element_by_id(
            common_util.get_id_value('SETTING_EDITEID'))
        se.click()
        se.clear()
        new_name = util.random_str(4)

        logger.info('new_name为%s' % new_name)
        se.send_keys(new_name)
        driver.implicitly_wait(10)
        common_util.getscreenshot(driver, 'test_modifyname')

        logger.info('点击保存修改后的名字')
        driver.find_element_by_id(common_util.get_id_value('SAVEID')).click()
        driver.implicitly_wait(10)
        common_util.getscreenshot(driver, 'test_modifyname')
        self.assertEqual(new_name, ne.text, '名字未修改成功')

        driver.implicitly_wait(10)
        common_util.logout(driver, 'test_modifyname')

    """用例关于我们"""

    #@unittest.skip
    def test_aboutus(self):
        logger.info('**********************关于我们用例执行***************************')
        common_util.login(driver, 'test_aboutus')
        driver.implicitly_wait(20)
        driver.find_element_by_id(common_util.get_id_value('MYID')).click()
        driver.implicitly_wait(10)

        logger.info("点击关于我们")
        util.swipeUp(driver)
        driver.implicitly_wait(10)

        util.swipeUp(driver)
        driver.find_element_by_android_uiautomator(
            'text(%s)' %
            common_util.get_text_value(
                'ABOUT_USTEXT')).click()
        common_util.getscreenshot(driver, 'test_aboutus')
        driver.implicitly_wait(10)
        au = driver.find_element_by_id(common_util.get_id_value('ABOUT_USID'))
        self.assertEqual(
            au.text,
            common_util.get_text_value(
                'ABOUT_USTEXT2'),
            '为进入到关于我们页面')

        web = driver.find_element_by_android_uiautomator(
            'text(\"www.fawjiefang.com.cn\")')
        print('web的text值为', web.text)
        self.assertEqual(
            web.text,
            common_util.get_text_value(
                'WEBTEXT2'),
            '关于我们的官方网址显示不对')

        wn = driver.find_element_by_id(common_util.get_id_value('NUMBERID'))
        self.assertEqual(
            wn.text,
            common_util.get_text_value('NUMBERTEXT'),
            '全国服务热线显示不对')

        jh6 = driver.find_element_by_id(
            common_util.get_id_value('JH_NUMBERID'))
        self.assertEqual(
            jh6.text,
            common_util.get_text_value(
                'JH_NUMBERTEXT'),
            'JH6尊享热线显示不对')

        qk = driver.find_element_by_id(common_util.get_id_value('QK_NUMBERID'))
        self.assertEqual(
            qk.text,
            common_util.get_text_value(
                'QK_NUMBERTEXT'),
            '轻卡服务专享热线显示不对')

    def tearDown(self):
        driver.quit()
