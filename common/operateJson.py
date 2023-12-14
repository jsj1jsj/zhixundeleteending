import json
from common.utilTool import UtilTool
from common.log import Log
from configFile import confPath

logger = Log().get_logger()


class OperateJson(object):
    def __init__(self, filename=None):
        if filename:
            self.filename = filename
        else:
            self.filename = confPath.PMS_HEADERS_PATH
        # logger.info(f'成功获取到json目录文件：{self.filename}')
        # self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        data = {}
        try:
            with open(self.filename, 'r', encoding='utf-8') as fn:
                data = json.load(fn)
        except Exception as msg:
            logger.error(f'读取文件失败,失败原因:{msg}')
        finally:
            return data

    # 读取文件内容后，通过key查询value
    def get_data(self, key):
        data = self.read_data()
        value = data[key]
        # logger.info(f'成功通过关键字[{key}]获取到value值：{value}')
        return value

    # 写入json数据，清空
    def write_data(self, data):
        with open(self.filename, 'w', encoding='utf-8') as fn:
            json.dump(data, fn)
        # logger.info(f'成功写入数据到文件中:{data}')
        # fn.write(json.dumps(data))

    # 写入json文件，追加（写入测试结果）
    def write_data_append(self, key, value):
        jsData = self.read_data()
        jsData[key] = value
        with open(self.filename, 'w', encoding='utf-8') as fn:
            json.dump(jsData, fn)
        # logger.info(f'成功写入数据:{jsData}')


if __name__ == '__main__':
    print("")



