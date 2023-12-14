import redis
from common.readConfigInfo import ReadConfigInfo
from common.log import Log

logger = Log().get_logger()

class OperateRedis(object):
    def __init__(self):
        readCon = ReadConfigInfo()
        self.host = readCon.get_config_value('redis','host')
        self.port = readCon.get_config_value('redis','port')
        self.password = readCon.get_config_value('redis','password')

        # 新建连接池
        self.pool = redis.ConnectionPool(host=self.host,
                                         port=self.port,
                                         password=self.password,
                                         decode_responses=True,  # 设置为True返回的数据格式就是时str类型
                                         max_connections=1000)

        # 建立连接
        self.conn = redis.StrictRedis(connection_pool=self.pool)
        logger.info('成功通过连接池建立Redis连接')

    # 获取Redis缓存值
    def get_redis_value(self,key):
        value = self.conn.get(key)
        logger.info(f'成功获取到Redis的key为{key}的值{value}')
        return value

    # 删除Redis缓存值
    def delete_redis_value(self,key):
        self.conn.delete(key)
        logger.info(f'成功删除Redis缓存{key}')

    # 新增或修改Redis缓存
    def set_redis_value(self,key,value):
        self.conn.set(key,value)
        logger.info(f'成功将{key}的值更改为{value}')



if __name__ == '__main__':
    con = OperateRedis()
    k1 = '1'
    k2 = '2'
    con.set_redis_value(k1,'23')
    v1 = con.get_redis_value(k1)
    v2 = con.get_redis_value(k2)
    con.delete_redis_value(k1)
    con.delete_redis_value(k2)
    print(v1)
    print(v2)