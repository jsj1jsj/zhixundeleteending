import logging
import os
import time


# log_path是日志存放的路径地址
current_path = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(os.path.dirname(current_path),"logs")

# 如果不存在log这个文件夹，就自动创建一个
if not os.path.exists(log_path):
    os.makedirs(log_path)


class TestLog(object):
    def __init__(self,name=None):
        # 文件的命名
        self.logname = os.path.join(log_path,"%s.log"%time.strftime("%Y-%m-%d"))
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s]-[%(filename)s]-%(levelname)s:%(message)s')

    def __console(self,level,message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname,"a",encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)  # 为logger添加的日志处理器

        # 创建一个StreamHandler，用于输出控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)  # 为logger添加的日志处理器

        if level == "info":
            self.logger.info(message)
        elif level == "debug":
            self.logger.debug(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)

        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

        # 关闭打开的文件
        fh.close()

    def info(self,message):
        self.__console("info",message)

    def debug(self,message):
        self.__console("debug",message)

    def warning(self,message):
        self.__console("warning",message)

    def error(self,message):
        self.__console("error",message)

if __name__ == '__main__':
    log = TestLog()
    log.info("-----测试开始-----")
    log.info("操作步骤")
    log.warning("测试结束")