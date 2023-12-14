import pymysql.cursors
import json
from common.log import Log
from common.readConfigInfo import ReadConfigInfo
from common.utilTool import DateTimeEncode

logger = Log().get_logger()


class OperateMysql(object):
    def __init__(self):
        readCon = ReadConfigInfo()
        self.host = readCon.get_config_value('mysql','host')
        self.port = readCon.get_config_value('mysql','port')
        self.user = readCon.get_config_value('mysql','user')
        self.password = readCon.get_config_value('mysql','password')
        self.db = readCon.get_config_value('mysql','db')
        self.charset = readCon.get_config_value('mysql','charset')
        # 连接数据库
        logger.info(f'正在连接数据库:host={self.host},port={self.port},user={self.user},password={self.password}')
        self.conn = pymysql.connect(host=self.host,
                                    port=int(self.port),
                                    user=self.user,
                                    password=self.password,
                                    db=self.db,
                                    charset=self.charset,
                                    cursorclass=pymysql.cursors.DictCursor)
        # 创建游标
        self.cur = self.conn.cursor()

    # 查询一条sql数据
    def select_one_sql(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        logger.info(f'成功查询到数据{result}')
        # 将查询到的结果（字典类型）转化为字符串
        result = json.dumps(result, ensure_ascii=False,cls=DateTimeEncode)
        return result

    # 查询多条sql数据
    def select_all_sql(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        result = json.dumps(result,ensure_ascii=False,cls=DateTimeEncode)
        logger.info(f'成功查询到数据{result}')
        return result

    # 执行sql语句
    def execute_sql(self,sql):
        logger.info(f'正在执行sql语句:{sql}')
        self.cur.execute(sql)
        # 提交sql----插入，删除、更新数据都需要提交commit()
        self.conn.commit()

    # 关闭游标和连接
    def close_connect(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    op = OperateMysql()




