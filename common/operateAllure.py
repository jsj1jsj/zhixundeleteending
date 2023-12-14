import subprocess
from configFile import confPath
import time
import allure
from dataHandle.getData import GetData
from dataHandle.dataRely import DataRely


class OperateAllure(object):

    def execute_command(self):
        time.sleep(1)
        subprocess.call(confPath.ALLURE_COMMAND, shell=True)

    def defined_allure_html(self,case,response,relyData):
        gd = GetData()
        dr = DataRely()
        caseId = gd.get_case_id(case)
        businessName = gd.get_business_name(case)
        caseName = gd.get_case_name(case)
        url = gd.get_request_url(case)
        expectCode = gd.get_expect_code(case)
        # expectValue = gd.get_expect_value(case,relyData)
        expectValue = dr.get_all_expect_value(case,relyData)

        if len(response) > 100:
            factValue = response[0:100] + '...'
        else:
            factValue = response

        # 制作 allure 报告
        title = businessName + '-' + caseName
        allure.dynamic.title(caseId)
        allure.dynamic.description(f'<font color="red">用例名称：</font>{title}<br />'
                                   f'<font color="red">请求URL：</font>{url}<br />'
                                   f'<font color="red">期望code：</font>{expectCode}<br />'
                                   f'<font color="red">预期值：</font>{expectValue}<br />'
                                   f'<font color="red">实际值：</font>{factValue}<br />'
                                   )
        if businessName:
            allure.dynamic.feature(businessName)
        allure.dynamic.story(title)


if __name__ == '__main__':
    oa = OperateAllure()
    oa.execute_command()