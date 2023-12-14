import ast
import re
from dataHandle.getData import GetData
import json
from jsonpath_rw import jsonpath, parse
from common.operateDB import OperateMysql
from common.readConfigInfo import ReadConfigInfo
from dataHandle.especialData import EspecialData
from common.log import Log

logger = Log().get_logger()


class DataRely(object):
    def __init__(self, filename=None):
        self.ed = EspecialData()
        self.data = GetData(filename)
        self.readCon = ReadConfigInfo()

    # 初始化依赖的数据（非接口获取的值）
    def get_init_rely_data(self, start=0, end=1):
        startDate = self.ed.get_target_date(start)
        endDate = self.ed.get_target_date(end)
        QNcheckInDate = self.ed.get_UTC_time(start)
        QNcheckOutDate = self.ed.get_UTC_time(end)
        startTime = self.ed.get_target_time(start)
        endTime = self.ed.get_target_time(end)
        arriveTime = self.ed.get_time_stamp13(startTime)
        leaveTime = self.ed.get_time_stamp13(endTime)


        zxordersn = self.readCon.get_config_value('xiaochengxuOrder', 'zxordersn')
        batterysn1 = self.readCon.get_config_value('newBattery', 'batterysn1')
        batterysn2 = self.readCon.get_config_value('newBattery', 'batterysn2')
        battery_id = self.readCon.get_config_value('newBattery', 'battery_id')
        data = self.readCon.get_config_value('login', 'data')
        user_id = self.readCon.get_config_value('newBattery', 'user_id')


        relyData = {
            'startDate': startDate,
            'endDate': endDate,
            'QNcheckInDate': QNcheckInDate,
            'QNcheckOutDate': QNcheckOutDate,
            'arriveTime': arriveTime,
            'leaveTime': leaveTime,

            'zxordersn':  zxordersn,
            'batterysn1': batterysn1,
            'batterysn2': batterysn2,
            'battery_id': battery_id,
            'data': data,
            'user_id': user_id,

        }
        return relyData

    # 根据dataRely和接口返回数据获取依赖的值
    def get_rely_response_value(self, dataRely, response):
        if dataRely == 'all':
            return response
        if '(.*)' in dataRely:
            try:
                relyValue = "".join(re.findall(dataRely, response))
            except:
                relyValue = ''
            return relyValue
        if '(.+?)' in dataRely:
            try:
                relyValue = re.findall(dataRely, response)[0]
            except:
                relyValue = ''
            return relyValue
        if not isinstance(response, dict):
            responseData = json.loads(response)
        else:
            responseData = response
        jsonExe = parse(dataRely)
        male = jsonExe.find(responseData)
        try:
            relyValue = [math.value for math in male][0]
            logger.info(f'通过依赖的数据路径:{dataRely},成功获取到依赖的值:{relyValue}')
        except Exception as msg:
            relyValue = ''
            logger.error(f'没有获取到依赖的字段{dataRely}对应的值，给默认值空字符串,原因:{msg}')
        return relyValue

    # 将依赖的值写入到全局变量中
    def save_rely_value(self, case, response, relyData):
        dataRely = self.data.get_data_rely(case)
        fieldRely = self.data.get_field_rely(case)
        if dataRely:
            for i in range(len(dataRely)):
                relyValue = self.get_rely_response_value(dataRely[i],response)
                relyData[fieldRely[i]] = relyValue
        logger.info(f'成功将所有依赖的数据写入全局变量testData中:{relyData}')


    # 从请求数据中，替换掉依赖的参数值
    def replace_params(self, paramsRely, relyValue, requestStr):
        """
        替换请求参数中依赖的值
        @param paramsRely: 需替换的变量名称
        @param relyValue: 需要替换的依赖变量对应的值（有些值从接口数据获取后需要特殊处理）
        @param requestStr: 获取到的请求参数（包括参数化的变量）
        """
        # requestStr = json.dumps(requestData)
        if '$' + paramsRely + '$' in requestStr:
            requestStr = requestStr.replace('$' + paramsRely + '$', relyValue)
            logger.info(f'成功从请求数据中，将依赖的参数值${paramsRely}$替换为具体值:{relyValue}')
        # requestDict = json.loads(requestStr)
        return requestStr

    # 替换所有的参数
    def replace_all_params(self, paramsList, relyData, requestData):
        requestStr = requestData
        if paramsList:
            for params in paramsList:
                try:
                    if params == 'randomNum' or params == 'mtOrderId':
                        relyValue = self.ed.get_random_num()
                    else:
                        relyValue = relyData[params]
                    if isinstance(relyValue, (int, float)):
                        relyValue = str(relyValue)
                    logger.info(f'成功获取到依赖参数{params}的值为{relyValue}')
                except Exception as msg:
                    relyValue = ''
                    logger.error(f'获取依赖的值{params}失败,默认赋值为空，失败原因：{msg},全局变量参数:{relyData}')
                # finally:
                #     self.replace_params(params,relyValue,requestStr)
                requestStr = self.replace_params(params, relyValue, requestStr)
            return requestStr
        else:
            return None

    # 重新组装请求参数
    def regroup_request_data(self, case, relyData):
        requestData = self.data.get_request_data(case)
        paramsList = self.data.get_params_rely(case)
        # 请求参数为json格式时替换参数
        if isinstance(requestData, dict):
            requestStr = json.dumps(requestData)
            requestStr = self.replace_all_params(paramsList, relyData, requestStr)
            requestDict = json.loads(requestStr)
            return requestDict
        # 非json格式的请求参数的参数化值的处理（字符串/xml格式等）
        elif isinstance(requestData, str):
            requestData = self.replace_all_params(paramsList, relyData, requestData)
            # 需要转码为utf-8格式
            return requestData.encode('utf-8')
        elif isinstance(requestData, list):
            requestStr = str(requestData)
            requestData = self.replace_all_params(paramsList, relyData, requestStr)
            requestData = ast.literal_eval(requestData)
            return requestData
        else:
            logger.error(f'非json/text等格式，无法转换，给默认值None')
            return None

    # 处理后置sql语句
    def get_execute_sql(self, case, relyDate):
        sqlParams = self.data.get_rely_sql_params(case)
        if sqlParams:
            sql = self.data.get_sql(case)
            for params in sqlParams:
                value = relyDate[params]
                sql = self.replace_params(params, value, sql)
            sqlList = sql.split(';')
        else:
            sqlList = None
        return sqlList

    # 执行sql语句
    def execute_sql_sentence(self, case, relyData):
        sqlList = self.get_execute_sql(case, relyData)
        if sqlList:
            db = OperateMysql()
            for sql in sqlList:
                db.execute_sql(sql)
            db.close_connect()

    # 从请求的参数中获取需要参数化的变量名
    def get_rely_params_by_str(self,requestData):
        paramsList = []
        if requestData and isinstance(requestData, str) and '$' in requestData:
            paramsList = re.findall('\$(.+?)\$', requestData)
            # paramsList = re.findall('\${(.+?)}', requestData)
        return paramsList

    # 对单个预期的值参数值进行替换或运算
    def replace_expect_value(self, expectValue,relyData):
        if expectValue and '$' in expectValue:
            # 获取依赖参数字符串表达式
            index = expectValue.find('$')
            # value1 = expectValue
            if expectValue[-1] in ["'", '"']:
                value1 = expectValue[index:-1]
            else:
                value1 = expectValue[index:]
            # 替换表达式内的参数
            relyParams = self.get_rely_params_by_str(value1)[0]
            relyValue = self.get_rely_data_value(relyData,relyParams)
            value2 = self.replace_params(relyParams,relyValue,value1)
            # 计算结果
            value3 = eval(value2)
            # 替换整个依赖的参数表达式
            newExpectValue = expectValue.replace(value1, str(value3))
            return newExpectValue
        else:
            return expectValue

    # 获取全部替换后的预期值
    def get_all_expect_value(self,case,relyData):
        expectValueList = self.data.get_expect_value(case)
        newExpectValueList = []
        if expectValueList:
            for expectValue in expectValueList:
                newExpectValue = self.replace_expect_value(expectValue,relyData)
                newExpectValueList.append(newExpectValue)
            return newExpectValueList
        else:
            return expectValueList

    # 读取全局变量中的值
    def get_rely_data_value(self,relyData,key):
        try:
            relyValue = relyData[key]
        except:
            relyValue = ''
        return relyValue


'''
   对于依赖数据的处理
   1，定义一个全局变量，用于存储依赖的数据
   2，获取依赖的所有的接口返回的字段responseRely（全路径字段），转化为list
   3，获取依赖的所有的请求的参数的变量名fieldRely（全路径字段），转化为list
   4，根据请求返回的结果获取依赖的值，并把值存放到字典中dataRely
   5，根据接口所依赖的字段，在全局变量中获取对应的值keyRely
   6，根据获取到的依赖的值和请求参数的变量拼接参数（最好实现的方式就是使用字符串替换的方法，拼接完再转为字典）
   (进行拼接前还需要判断是否需要特殊处理：如日期实时获取，某个价格需要打折)

'''

if __name__ == '__main__':
    da = 'we'
    st = json.dumps(da)
    di = json.loads(st)
    print(EspecialData().get_random_num())
