import os
import time
import json
from datetime import date,datetime
from configFile import confPath
# from common.log import Log


# logger = Log().get_logger()


class UtilTool(object):
    # 获取当前项目下的目录及文件地址
    def get_file_dirname(self,dirname, filename=None):
        # filepath = os.path.join(os.path.dirname(os.getcwd()), dirname)
        filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), dirname)
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        if filename is None:
            filename = filepath
        else:
            filename = os.path.join(filepath,filename)
        return filename

    # 获取当前时间并格式化处理
    def get_now_time(self):
        return time.strftime('%Y-%m-%d',time.localtime())

    # 删除历史文件（用于生成allure报告的数据文件）
    def delete_files(self,filepath=None):
        if not filepath:
            filepath = confPath.ALLURE_DATA_PATH
        # 用os.walk方法取得path路径下的文件夹路径，子文件夹名，所有文件名
        for foldName, subfolder, filenames in os.walk(filepath):
            for filename in filenames:
                os.remove(os.path.join(foldName, filename))
                # logger.info("{} deleted.".format(filename))


# 重写json类，来处理特殊日期格式（dumps的原功能是将dict转化为str格式，不支持转化时间）
class DateTimeEncode(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':
    adict = {'date':datetime(2020,9,20,12,11,23)}
    bdict = json.dumps(adict,cls=DateTimeEncode)
    print(bdict)

    ut = UtilTool()
    print(ut.get_file_dirname('test','test1.py'))

