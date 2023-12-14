from base.requestsMethod import RequestsMethod
from common.operateHeader import OperateHeader
from common.readConfigInfo import ReadConfigInfo
from common.operateJson import OperateJson
from dataHandle.especialData import EspecialData
from configFile import confPath
import json
from common.log import Log
logger = Log().get_logger()


class InitLogin(object):
    def __init__(self):
        self.reqMethod = RequestsMethod()
        ed = EspecialData()
        readCon = ReadConfigInfo()
        self.loginUrl = readCon.get_config_value('login', 'loginUrl')
        self.assertUrl = readCon.get_config_value('login', 'assertUrl')
        self.tesseract_cmd = readCon.get_config_value('newBattery', 'tesseract_cmd')
        self.captcha_url = readCon.get_config_value('newBattery', 'captcha_url')

        self.loginheader = json.loads(readCon.get_config_value('login', 'loginheader'))
        # self.data = json.loads(readCon.get_config_value('login', 'data'))
        self.dataKey = readCon.get_config_value('login','dataKey')
        self.tokenKey = readCon.get_config_value('login','tokenKey')
        self.tokenField = readCon.get_config_value('login','tokenField')
        self.assertData = json.loads(readCon.get_config_value('login', 'assertData'))
        self.loginheader = readCon.get_config_value('login','loginheader')
        self.misData = json.loads(readCon.get_config_value('login','misData'))
        self.fmsData = json.loads(readCon.get_config_value('login','fmsData'))
        self.appId = readCon.get_config_value('login','appId')
        self.fmsId = readCon.get_config_value('login','fmsId')
        self.misId = readCon.get_config_value('login','misId')
        self.verify_code = ed.getImage(self.tesseract_cmd,self.captcha_url)
        self.data = readCon.get_config_value('login', 'data')
        self.data=json.loads(self.data)
        self.data["verify_code"] = self.verify_code

    # 定义一个方法用于初始化登录状态
    def init_login(self):
        # 定义一个变量控制循环状态，判断用户是否需要登录(控制循环次数防止进入死循环)
        # loopStatus = True
        self.login()
        # loopStatus = 0
        # while loopStatus < 10:
        #     # 检查登录状态
        #     loginStatus = self.check_login_status()
        #     if loginStatus:
        #         # loopStatus = False
        #         loopStatus = 10
        #     else:
        #         loopStatus += 1
        #         self.login()

    # 定义一个方法用于判断token是否失效
    def check_login_status(self):
        logger.info('----正在获取登录状态----')
        # 读取headers文件
        fileHeaders = self.get_file_headers()
        # misHeaders = self.get_file_headers(confPath.MIS_HEADERS_PATH)
        # fmsHeaders = self.get_file_headers(confPath.FMS_HEADERS_PATH)
        # 校验登录状态
        loginStatus = False
        # 调toApp接口往子系统注册token信息(同时校验token信息)
        res = self.reqMethod.send_request('post',self.assertUrl,data=self.assertData,headers=fileHeaders)
        print(self.assertData)
        self.assertData["xtoken"] = json.loads(res)["data"]["token"]
        print(self.assertData)
        # misRes = self.reqMethod.send_request('post',self.assertUrl,data=self.misData,headers=misHeaders)
        # fmsRes = self.reqMethod.send_request('post',self.assertUrl,data=self.misData,headers=fmsHeaders)
        print("whj111111")
        if '"code": 200' in res:
        # if '"code": 200' in res and '"code": 200' in misRes and '"code": 200' in fmsRes:
            print("whj2222")
            loginStatus = False

        logger.info(f'成功获取到登录状态为:{loginStatus}')
        # 切换酒店
        self.change_hotel()
        return loginStatus

    # 定义一个登录方法，并保存token信息
    def login(self):
        # 登录
        logger.info('----开始准备登录----')
        result = self.reqMethod.send_request('post',self.loginUrl,data=self.data,headers=None)
        # 保存token
        self.save_headers_to_file(result)
        return result

    # 保存token信息
    def save_headers_to_file(self,result):
        # 保存pms_token
        pmsHeader = OperateHeader(result)
        pmsHeader.save_token(self.dataKey,self.tokenKey,self.tokenField)
        # 保存fms_token
        fmsHeader = OperateHeader(result,confPath.FMS_HEADERS_PATH)
        fmsHeader.save_token(self.dataKey, self.tokenKey, self.tokenField)
        # 保存mis_token
        misHeader = OperateHeader(result,confPath.MIS_HEADERS_PATH)
        misHeader.save_token(self.dataKey,self.tokenKey,self.tokenField)

    # 读取文件headers信息
    def get_file_headers(self,filename=None):
        opJs = OperateJson(filename)
        fileHeaders = opJs.read_data()
        logger.info(f'读取到的headers信息为:{fileHeaders}')
        return fileHeaders

    # 切换酒店
    # def change_hotel(self):
    #     fileHeaders = self.get_file_headers()
    #     # 调changeCurrentHotelCode切换酒店id
    #     result1 = self.reqMethod.send_request('get', self.changeHotelUrl, data=self.changeHotelData, headers=fileHeaders)
    #     if '"code": "200"' in result1:
    #         logger.info(f'已切换到测试酒店:{self.changeHotelData}')
    #     else:
    #         logger.error(f'酒店切换失败,原因:{result1}')


if __name__ == '__main__':
    ls = InitLogin()
    ls.login()
    # sta = ls.check_login_status()
    # print(sta)
    # ls.init_login()











