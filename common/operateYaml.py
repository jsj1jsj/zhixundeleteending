import yaml
from common.utilTool import UtilTool
from configFile import confPath
from common.log import Log

logger = Log().get_logger()


class OperateYaml(object):
    def __init__(self,filename=None):
        if filename:
            self.filename = filename
        else:
            self.filename = UtilTool().get_file_dirname('tempData','responseData.yaml')
        logger.info(f'成功获取到yaml文件目录:{self.filename}')

    # 加载文件
    def load_file(self):
        with open(self.filename, 'r', encoding='utf-8') as ft:
            data = yaml.load(ft, Loader=yaml.FullLoader)
        logger.info(f'成功加载出yaml文件数据:{data}')
        return data

    # 读取数据
    def read_yaml(self, key, port=None):
        if not port:
            value = self.load_file()[key][port]
        else:
            value = self.load_file()[key]
        logger.info(f'成功获取到yaml文件中的{key}对于的值为:{value}')
        return value

    # 写入数据（追加形式写入）
    def write_yaml(self,key,value):
        data = {key:value}
        with open(self.filename, 'a', encoding='utf-8') as fp:
            yaml.dump(data, fp)
            # fp.write(data)
        logger.info(f'成功将数据写入yaml文件中{key}:{value}')

    # 清除数据
    def clear_yaml(self):
        with open(self.filename, 'w') as ft:
            ft.truncate()
        logger.info(f'初始化数据，成功删除所有yaml文件值')


if __name__ == '__main__':
    oy = OperateYaml()
    value = {'name':'bon','age':24}
    for i in range(100):
        oy.write_yaml(i,value)
    # oy.clear_yaml()

