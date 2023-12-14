import logging
import time
import json
from common.utilTool import UtilTool
import os

# 定义日志存放的文件
nowTime = UtilTool().get_now_time()
filepath = UtilTool().get_file_dirname('logs', nowTime) + '.log'
# fileName = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'


class Log(object):
    def __init__(self):
        # 初始化
        self.logger = logging.getLogger()
        self.logger.handlers.clear()
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s [%(funcName)s] %(lineno)d %(levelname)s %(message)s')

        # 控制台输出
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.INFO)
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.ch)

        # 文件输出
        self.fh = logging.FileHandler(filepath,'a',encoding='utf-8')
        self.fh.setLevel(logging.INFO)
        self.fh.setFormatter(formatter)
        self.logger.addHandler(self.fh)

    # h获取logger对象
    def get_logger(self):
        return self.logger

    # 关闭流对象
    def close_handle(self):
        self.logger.removeFilter(self.ch)
        self.logger.removeFilter(self.fh)
        self.fh.close()


        
if __name__ == '__main__':
    log = Log()
    logger = log.get_logger()
    logger.info('开始api接口测试')
    log.close_handle()