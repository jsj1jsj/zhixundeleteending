import requests
from common.readConfigInfo import ReadConfigInfo


class WeWorkMessage(object):
    def __init__(self):
        readCon = ReadConfigInfo()
        self.appName = readCon.get_config_value('emailInfo', 'appName')
        self.venv = readCon.get_config_value('emailInfo', 'venv')
        self.report = readCon.get_config_value('emailInfo', 'report')

    # 直接调用接口发送测试结果
    def send_test_result(self, startTime, totalTime, caseResult, businessFail):
        content = self.create_content(startTime, totalTime, caseResult, businessFail)
        url = 'www.baidu.com'
        data = {
            "bot": "AutoTest",
            "level": "info",
            "title": "接口自动化测试报告",
            "host": "",
            "label": {},  # {"附件信息": "附加信息"}
            "content": content,
            "notify": []
        }
        headers = {"Authorization": "11"}
        result = requests.request('post', url, json=data, headers=headers)
        # return result.json()
        print(result.text)

    # 配置发送的内容
    def create_content(self, startTime, totalTime, caseResult, businessFail):
        businessCount = caseResult['businessPassCount'] + caseResult['businessFailCount']
        bf = businessFail
        if not bf:
            bf = '暂无'
        context = f"**项目配置**    \
                    \n >项目名称：<font color=\"info\">{self.appName}</font>  \
                    \n >执行人员：<font color=\"comment\">AutoTester</font>  \
                    \n >执行环境：<font color=\"warning\">{self.venv}</font>  \
                    \n\n >\
                    \n >**运行时间**    \
                    \n >执行时间：<font color=\"comment\">{startTime}</font>    \
                    \n >执行用时：<font color=\"warning\">{totalTime}s</font> \
                    \n\n >             \
                    \n >**执行用例情况**   \
                    \n >用例数量：<font color=\"comment\">{caseResult['caseCount']}</font> \
                    \n >成功数量：<font color=\"info\">{caseResult['passCount']}</font>    \
                    \n >失败数量：<font color=\"warning\">{caseResult['failCount']}</font> \
                    \n\n >             \
                    \n >**业务场景用例**   \
                    \n >业务场景用例数量：<font color=\"comment\">{businessCount}</font> \
                    \n >业务场景成功数量：<font color=\"info\">{caseResult['businessPassCount']}</font>    \
                    \n >业务场景失败数量：<font color=\"warning\">{caseResult['businessFailCount']}</font> \
                    \n >失败的业务场景：<font color=\"warning\">{bf}</font> \
                    \n\n >    \
                    \n >**请查看详情**：[自动化测试报告]({self.report})"
        return context


if __name__ == '__main__':
    s = '2020-06-03 14:29'
    t = 200
    c = {'caseCount': 3,
         'skipCount': 0,
         'passCount': 2,
         'failCount': 1,
         'errorCount': 0,
         'businessCaseCount': 2,
         'businessPassCount': 1,
         'businessFailCount': 1
         }
    b = []
    we = WeWorkMessage()
    co = we.create_content(s,t,c,b)
    we.send_test_result(s,t,c,b)

