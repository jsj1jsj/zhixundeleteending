import json
from common.utilTool import UtilTool
from common.operateJson import OperateJson
from common.log import Log
from common.readConfigInfo import ReadConfigInfo
from configFile import confPath

logger = Log().get_logger()


class OperateHeader(object):
    def __init__(self, response,filename=None):
        if isinstance(response,str):
            self.response = json.loads(response)
        else:
            self.response = response
        if filename:
            self.filename = filename
        else:
            self.filename = confPath.PMS_HEADERS_PATH
        self.opJson = OperateJson(self.filename)
        self.readCon = ReadConfigInfo()

    # 获取token值
    def get_token_by_response(self, dataKey,tokenKey):
        token = self.response[dataKey][tokenKey]
        logger.info(f'成功从登录接口数据中获取到token值：{token}')
        return token

    # 组装headers
    def headers_data(self, dataKey, tokenKey, fieldToken):
        token = self.get_token_by_response(dataKey,tokenKey)
        data = {'content-type': 'application/json;charset=UTF-8',
                fieldToken: token}
        logger.info(f'成功组装headers信息：{data}')
        return data

    # 将token添加到headers中并保存到文件中
    def save_token(self, dataKey, tokenKey,fieldToken):
        data = self.headers_data(dataKey,tokenKey,fieldToken)
        self.opJson.write_data(data)
        logger.info('成功将header信息保存到文件中')

    # 从文件中读取headers信息(这儿读headers需要传参response,建议从operateJson中直接读)
    # def get_headers_by_file(self):
    #     headers = self.opJson.read_data()
    #     return headers


if __name__ == '__main__':
    res = {'code': 0, 'msg': '', 'data': {'sdToken': 'tntQDVLFUYzyh3mEFN4k5owdzmeX2qV9Bqgk2wN3PGs=', 'bindMobile': True}}
    opHe = OperateHeader(res)
    token = opHe.get_token_by_response('data','sdToken')
    opHe.save_token('data','sdToken','authorizationv2')
    headers = opHe.get_headers_by_file()
    print(token)
    print(headers)