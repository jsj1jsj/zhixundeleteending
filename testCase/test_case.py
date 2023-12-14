import time
from configFile import confPath
import pytest
import allure
from datetime import datetime
from base.requestsMethod import RequestsMethod
from common.weWorkMessage import WeWorkMessage
from dataHandle.dataRely import DataRely
from dataHandle.getData import GetData
from common.initLogin import InitLogin
from common.operateAllure import OperateAllure
from common.sendEmail import SendEmail
from common.operateDB import OperateMysql
from common.log import Log
from common.utilTool import UtilTool
from common.wechattoken import save_wechattoken
import warnings


log = Log()
logger = log.get_logger()

# 忽略警告
warnings.simplefilter('ignore', ResourceWarning)

# 统计执行用例的情况
caseResult = {'caseCount': 0,
              'skipCount': 0,
              'passCount': 0,
              'failCount': 0,
              'errorCount': 0,
              'businessCaseCount': 0,
              'businessPassCount': 0,
              'businessFailCount': 0
              }

# 统计业务场景用例
businessPass = []
businessFail = []

# 定义一个全局变量用于存放依赖的数据
relyData = {}
# 获取用例集
testData = GetData().get_excel_data()


class TestCase(object):

    @classmethod
    def setup_class(cls):
        global relyData
        # 获取开始时间
        cls.caseStart = datetime.now()
        cls.data = GetData()
        cls.rely = DataRely()
        cls.sendRequest = RequestsMethod()
        cls.oa = OperateAllure()
        # cls.sql = OperateMysql()
        # 初始化依赖的数据
        relyData = cls.rely.get_init_rely_data()
        # 删除历史用于生成allure报告的数据和日志
        ut = UtilTool()
        ut.delete_files()
        # ut.delete_files(confPath.LOG_FILE_PATH)
        # 判断token是否失效
        # login = InitLogin()
        # login.init_login()
        # save_wechattoken()

    def teardown_class(cls):
        # 生成测试报告
        cls.oa.execute_command()
        # 关闭日志流对象
        log.close_handle()
        # 获取结束时间
        caseEnd = datetime.now()
        # totalTime = (caseEnd - cls.caseStart).seconds
        totalTime = str(caseEnd - cls.caseStart).split('.')[0]
        startTime = cls.caseStart.strftime('%Y-%m-%d %H:%M:%S')
        ##发送安骑星公众号

        # 发送邮件
        startTime = cls.caseStart.strftime('%Y-%m-%d %H:%M:%S')
        SendEmail().send_email(startTime, totalTime, caseResult,businessFail)
        # 发送企信
        logger.info(f'测试完成，正在将测试结果发送到企信')
        WeWorkMessage().send_test_result(startTime, totalTime, caseResult,businessFail)
        logger.info('测试结果已成功发送到企信')

    @pytest.mark.parametrize('case', testData)
    def test_case(self, case):
        global caseResult
        global businessPass
        global businessFail
        caseResult['caseCount'] += 1
        caseId = self.data.get_case_id(case)
        caseName = self.data.get_case_name(case)
        logger.info(f'开始执行第{caseId}条用例:{caseName}')

        # 判断是否需要跳过用例
        isRun = self.data.get_is_run(case)
        if isRun != True:
            pytest.mark.skip()
            print("跳过执行case:",caseName)
            return "函数已被我调用"
        # 获取接口请求所需参数
        logger.info('正在读取单个用例的各种数据')
        url = self.data.get_request_url(case)
        requestData = self.data.get_request_data(case)
        headers = self.data.get_headers(case,relyData)
        method = self.data.get_request_way(case)
        expectCode = self.data.get_expect_code(case)
        expectValueList = self.rely.get_all_expect_value(case,relyData)
        # fieldRely = self.data.get_field_rely(case)
        dataRely = self.data.get_data_rely(case)
        paramsRely = self.data.get_params_rely(case)
        businessName = self.data.get_business_name(case)
        platform = self.data.get_platform(case)
        # if businessName:
        #     caseResult['businessCaseCount'] += 1

        # 判断是否存在case依赖
        if paramsRely:
            # 拼接请求参数
            logger.info(f'存在数据依赖,正在拼接依赖的请求参数')
            requestData = self.rely.regroup_request_data(case, relyData)

        # 发送请求
        logger.info(f'请求传入数据，method={method},url={url},data={requestData},headers={headers}')
        # result = self.sendRequest.send_request(method, url, requestData, headers)
        if 'channelOrder' in case['caseId']:
            time.sleep(2)
        result = self.sendRequest.send_http_request(method, url, requestData, headers)
        if '下单' in case['caseName']:
            time.sleep(2)
        # logger.info(f'获取接口返回数据:{result}')

        # 断言：预期结果与实际结果对比
        try:
            assert expectCode in result, f'expectCode断言失败，用例不通过预期值:{expectCode},实际值:{result}'
            logger.info(f'code码断言成功,用例通过,预期值:{expectCode},实际值:{result}')
            if expectValueList:
                for expectValue in expectValueList:
                    assert expectValue in result, f'expectValue断言失败，用例不通过,预期值:{expectValue},实际值:{result}'
                logger.info(f'关键字断言成功,用例通过,预期值:{expectValueList},实际值:{result}')
            caseResult['passCount'] += 1
            if businessName not in businessPass:
                caseResult['businessPassCount'] += 1
                businessPass.append(businessName)
        except AssertionError as msg:
            logger.info(f'执行用例失败:{msg}')
            caseResult['failCount'] += 1
            if businessName not in businessFail:
                caseResult['businessFailCount'] += 1
                businessFail.append(businessName)
            raise
        except Exception as msg:
            caseResult['errorCount'] += 1
            logger.error(f'执行用例报错，详细原因:{msg}')
            raise
        else:
            # 判断是否需要写入关联参数
            if dataRely:
                self.rely.save_rely_value(case, result, relyData)
            # 判断是否需要mock（更新数据库）
            sqlRely = self.data.get_rely_sql_params(case)
            if sqlRely:
                self.rely.execute_sql_sentence(case,relyData)

        # 自定义allure报告
        self.oa.defined_allure_html(case,result,relyData)
        # 定时任务执行完毕设置等待时间
        if platform == 'task':
            time.sleep(5)


if __name__ == '__main__':
    # pytest.main()
    # testData = GetData().get_excel_data()[244:247] #02 小程序
    # testData = GetData().get_excel_data()[257:307] #02 美团
    # testData = GetData().get_excel_data()[306:307] #03 飞猪
    # testData = GetData().get_excel_data()[309:379]  # 03 分销商
    testData = GetData().get_excel_data()[0:9]
    TestCase().setup_class()
    for i in range(0, 9):
        TestCase().test_case(testData[i])
    TestCase().teardown_class()
