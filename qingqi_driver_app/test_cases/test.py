from qingqi_driver_app.test_cases.common_util import CommonUtil
import unittest

class test(unittest.TestCase):

    def test_te(self):
        #print('testcase里的测试类')
        #list_path = CommonUtil().appoint_appresourceconf()
        #print('list_path',list_path)
        direcrots = CommonUtil().mik_directors()
        #print(direcrots)
        #print('direcrots[0]==',direcrots[0])
        print('unittest.getTestCaseNames==', unittest.getTestCaseNames(test,'test')[0])
        ##d = CommonUtil().mik_filepath(direcrots[0],unittest.getTestCaseNames(test,'test')[0],'.txt')
        #CommonUtil().mik_filepath('D:\\pycharm\\AutoTEST\\qingqi_driver_app\\logs\\','test_te','txt')
        print('测试类')
