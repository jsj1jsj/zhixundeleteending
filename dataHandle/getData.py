import re

from common.operateExcel import OperateExcel
from common.operateDB import OperateMysql
from common.operateJson import OperateJson
from common.operateXml import OperateXml
from common.operateXml import OperateXml1
from common.operateXml import OperateXml2
from common.readConfigInfo import ReadConfigInfo
from common.log import Log
from common.utilTool import UtilTool
import os
from configFile import confPath
import json
from common.operateHeader import OperateHeader

logger = Log().get_logger()


class GetData(object):
    def __init__(self, filename=None):
        self.opExcel = OperateExcel(filename)
        self.readCon = ReadConfigInfo()

    # 获取所有case文件
    def get_all_case_file(self):
        ut = UtilTool()
        fileList = []
        caseDir = ut.get_file_dirname('caseData')
        filenames = os.listdir(caseDir)
        for file in filenames:
            fileList.append(os.path.join(caseDir, file))
        return fileList

    # 获取所有的case数据(单个文件)
    def get_excel_data(self):
        logger.info('------正在批量读取测试用例数据------')
        sheetNames = self.opExcel.get_sheet_names()
        print(sheetNames)
        testData = []
        for name in sheetNames:
            data = self.opExcel.get_data_by_name(name)
            titleName = data.row_values(0)
            # print(titleName)
            # rowData = dict.fromkeys(titleName,'')
            rows = data.nrows
            for row in range(1, rows):
                testData.append(dict(zip(titleName, data.row_values(row))))
        logger.info(f'成功读取到本次要执行的全部用例共计{len(testData) + 1}条')
        return testData

    # 获取用例编号
    def get_case_id(self, case):
        return case['caseId']

    # 获取业务场景case名称
    def get_business_name(self, case):
        return case['businessName']

    # 获取用例名称
    def get_case_name(self, case):
        return case['caseName']

    # 获取被测系统
    def get_platform(self, case):
        try:
            platform = case['platform']
        except:
            platform = None
        return platform

    # 获取用例请求的url
    def get_request_url(self, case):
        platform = self.get_platform(case)
        readCon = ReadConfigInfo()
        if platform == 'applet':
            baseUrl = readCon.get_config_value('baseUrl', 'appletIp')
        else:
            baseUrl = readCon.get_config_value('baseUrl', 'ip')
        url = baseUrl + case['url']
        logger.info(f'成功获取到请求接口的完整URL:{url}')
        return url

    # 获取用例的运行状态
    def get_is_run(self, case):
        try:
            isRun = case['isRun']
        except:
            isRun = None
        if isRun == 'yes':
            return True
        else:
            return False

    # 获取用例请求的方式
    def get_request_way(self, case):
        method = case['method']
        logger.info(f'成功获取用例请求的方式:{method}')
        return method

    # 获取用例运行是否携带headers
    def get_headers_type(self, case):
        return case['isHeaders']

    # 从全局变量中获取美团的token
    def get_authorization(self, relyData):
        try:
            authorization = relyData['authorization']
        except:
            authorization = None
        return authorization

    # 从全局变量中获取美团的date
    def get_date(self, relyData):
        try:
            date = relyData['date']
        except:
            date = None
        return date

    # 获取headers
    def get_headers(self, case, relyData):
        isHeaders = self.get_headers_type(case)
        if isHeaders == 'yes':
            headers = OperateJson().read_data()
        elif isHeaders == 'applet':
            filename = confPath.APPLET_HEADERS_PATH
            headers = OperateJson(filename).read_data()
        else:
            headers = None
        logger.info(f'成功获取到headers信息:{headers}')
        return headers

    # 获取数据依赖--接口返回的依赖字段的xpath路径
    def get_data_rely(self, case):
        dataRely = case['dataRely']
        if dataRely:
            dataRelyList = dataRely.split(',')
        else:
            dataRelyList = None
        logger.info(f'成功获取到接口依赖的数据路径:{dataRelyList}')
        return dataRelyList

    # 获取用于存放依赖变量的变量名称
    def get_field_rely(self, case):
        fieldRely = case['fieldRely']
        if fieldRely:
            fieldRelyList = fieldRely.split(',')
        else:
            fieldRelyList = None
        logger.info(f'成功获取用于存放依赖变量的变量名称:{fieldRelyList}')
        return fieldRelyList

    # 获取用于拼接依赖中请求参数的变量名称
    def get_params_rely(self, case):
        paramsRely = case['paramsRely']
        if paramsRely:
            paramsRelyList = paramsRely.split(',')
        else:
            paramsRelyList = None
        logger.info(f'成功获取用于拼接依赖中请求参数的变量名称:{paramsRelyList}')
        return paramsRelyList

    # 获取数据依赖中需要单独处理的字段变量
    def get_especial_rely(self, case):
        especialRely = case['especialRely']
        if especialRely:
            especialRelyList = especialRely.split(',')
        else:
            especialRelyList = None
        logger.info(f'成功获取数据依赖中需要单独处理的字段变量:{especialRelyList}')
        return especialRelyList

    # 获取请求的参数对应的key值
    def get_request_key(self, case):
        requestKey = case['requestKey']
        logger.info(f'成功获取到请求的参数对应的key值:{requestKey}')
        return requestKey

    # 获取请求的参数存放的json文件路径
    def get_json_path(self, case):
        jsonPath = case['jsonPath']
        logger.info(f'成功获取请求的参数存放的json文件路径:{jsonPath}')
        return jsonPath

    # 获取请求的参数
    def get_request_data(self, case):
        requestKey = self.get_request_key(case)
        jsonPath = self.get_json_path(case)
        filename = UtilTool().get_file_dirname('dataCase/jsonParams', jsonPath)
        logger.info(f'成功获取请求的参数存放的json文件的完整路径：{filename}')
        try:
            if requestKey == 'alitrip':
                requestData = OperateXml().get_xml_data()
            elif requestKey == 'tongcheng':
                requestData = {"Message":OperateXml1().get_xml_data()}
            elif requestKey == 'tongchengcancel':
                requestData = {"Message":OperateXml2().get_xml_data()}
            else:
                requestData = OperateJson(filename).get_data(requestKey)
            logger.info(f'成功获取请求的参数：{requestData}')
        except Exception as msg:
            requestData = {}
            logger.error(f'获取请求参数失败，给默认值空：{requestData},失败原因:{msg}')
        return requestData

    # 根据请求的参数关键字获取依赖的字段
    def get_params_rely_by_request_data(self,case):
        requestData = self.get_request_data(case)
        paramsList = []
        if isinstance(requestData,str) and '$' in requestData:
            paramsList = re.findall('\$(.+?)\$',requestData)
        return paramsList


    # 获取预期的code
    def get_expect_code(self, case):
        expectCode = case['expectCode']
        logger.info(f'成功获取预期的code码：{expectCode}')
        return expectCode

    # 获取预期的值(初始化)
    def get_expect_value(self,case):
        expectValue = case['expectValue']
        if expectValue:
            expectValueList = expectValue.split(',')
        else:
            expectValueList = None
        return expectValueList

    # 获取预期的值
    # def get_expect_value(self, case, relyData):
    #     expectValue = case['expectValue']
    #     if '$' in expectValue:
    #         try:
    #             key = expectValue.replace('$', '')
    #             expectValue = relyData[key]
    #         except:
    #             expectValue = None
    #     logger.info(f'成功获取预期的值：{expectValue}')
    #     return expectValue

    # 判断是否需要从数据库获取预期值
    def expect_sql_status(self, case):
        sql = case['expectSql']
        if sql:
            return True
        else:
            return False

    # 从数据库获取到预期结果值
    def get_expect_sql_value(self, sql):
        return OperateMysql().select_one_sql(sql)

    # 获取sql中依赖的参数
    def get_rely_sql_params(self, case):
        sqlParams = case['sqlParams']
        if sqlParams:
            sqlParams = sqlParams.split(';')
        else:
            sqlParams = None
        return sqlParams

    # 获取sql语句对于的key
    def get_sql_key(self, case):
        sqlKey = case['sqlKey']
        return sqlKey

    # 读取要执行的sql语句
    def get_sql(self, case):
        sqlKey = self.get_sql_key(case)
        if sqlKey:
            filename = confPath.SQL_PATH
            sql = OperateJson(filename).get_data(sqlKey)
        else:
            sql = None
        return sql


if __name__ == '__main__':
    filename = 'C:\\Users\\admin\\Desktop\\fz.xlsx'
    gt = GetData(filename)
    print(gt.get_excel_data())
    case = [{'caseid':21,'bissnusname':'测四','paramsRely':'orderNo'},{'id':21,'expectValue':'$orderNo$','paramsRely':'orderNo'}]

