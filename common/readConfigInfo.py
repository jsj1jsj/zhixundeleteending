import configparser
from common.utilTool import UtilTool
from common.log import Log
from configFile import confPath
logger = Log().get_logger()


class ReadConfigInfo(object):
    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            # self.filepath = UtilTool().get_file_dirname('configFile', 'test1Config.ini')
            self.filepath = confPath.CON_FILE_PATH
        # logger.info(f'成功获取配置文件路径：{self.filepath}')
        # 初始化配置文件对象
        # self.data = self.read_config_info()

    # 读取配置文件对象
    def read_config_info(self):
        readCon = configparser.ConfigParser()
        # 读取配置文件（此处是utf-8-sig，而不是utf-8）,这里主要解决读取配置文件中文乱码问题
        readCon.read(self.filepath, encoding='utf-8-sig')
        return readCon

    # 获取配置文件的value值
    def get_config_value(self, section, key):
        try:
            data = self.read_config_info()
            value = data.get(section, key)
            logger.info(f'成功读取到配置文件[{section}]菜单下[{key}]的值为:{value}')
        except Exception as msg:
            value = None
            logger.info(f'配置文件读取失败，给默认值None,失败原因:{msg}')
        return value


if __name__ == '__main__':
    read = ReadConfigInfo()
    values = read.get_config_value('mysql', 'charset')
    print(values)
