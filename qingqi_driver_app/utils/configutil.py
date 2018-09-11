# -*-coding:utf-8-*-

from qingqi_driver_app.utils.mylogger import MyLogger
import configparser

import os,sys

"""对配置文件进行操作"""


class ConfigUtil(object):

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.logger = MyLogger()

    def read_config(self, conf_path):
        self.cf.read(conf_path, encoding='UTF-8')
        self.logger.info('读取配置文件%s' % conf_path)

    def write(self):
        filename = open(self.fpath, 'w')
        self.cf.write(filename)
        filename.close()

    """添加指定的节点"""

    def add_section(self, section):
        sections = self.cf.sections()
        if section in sections:
            return
        else:
            self.cf.add_section(section)

    """删除节点"""

    def remove_section(self, section):
        return self.cf.remove_section(section)

    """返回文件中的所有sections"""

    def sections(self):
        return self.cf.sections()

    """获取节点下option对应的value值"""

    def get(self, section, option):
        return self.cf.get(section, option)

    """在指定的section下添加option和value值"""

    def set(self, section, option, value):
        if self.cf.has_section(section):
            self.cf.set(section, option, value)

    """移除指定section点内的option"""

    def remove_option(self, section, option):
        if self.cf.has_section(section):
            resut = self.cf.remove_option(section, option)
            return resut
        return False

    """ 返回section内所有的option和value列表"""

    def items(self, section):
        return self.cf.items(section)

    """返回section所有的option"""

    def options(self, section):
        return self.cf.options(section)


if __name__ == '__main__':
    config_file = 'C:\\Users\\lenovo\\Desktop\\config1.ini'
    c = ConfigUtil()
    c.read_config(config_file)
    print('调用对象')
    print('get打印的值为=======', c.get('db_config_CD', 'host'))
    print('configutils', os.path.join(os.getcwd()))
    print('sys', sys.path[0])
