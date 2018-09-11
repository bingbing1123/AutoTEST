# -*-coding:utf-8-*-

import unittest
from qingqi_driver_app.test_cases.test_sanitytests import QingqiCase
from qingqi_driver_app.test_cases.common_util import CommonUtil
from qingqi_driver_app import HTMLTestRunner2


def run_testcases():
    suite = unittest.TestSuite()
    tests = [
        QingqiCase('test_login'),
        QingqiCase('test_modifyname'),
        QingqiCase('test_aboutus')]
    suite.addTests(tests)
    report_path = CommonUtil().mikreport_path()

    #tests = unittest.getTestCaseNames(QingqiCase)

    with open(report_path, 'wb+') as fp:
        runner = HTMLTestRunner2.HTMLTestRunner(
            stream=fp,
            title='青汽自动化测试',
            description='测试人员冀~~~'
        )
        runner.run(suite)


if __name__ == '__main__':
    #unittest.main()
    run_testcases()
