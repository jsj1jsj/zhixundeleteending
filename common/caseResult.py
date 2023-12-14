class CaseResult(object):
    '''
    获取case的通过率和失败率
    '''

    def case_result(self, passSum=None, failSum=None):
        if passSum is None or failSum is None:
            emailContent = '本次接口自动化测试已完成，测试结果见附件'
        else:
            countSum = passSum + failSum
            if countSum > 0:
                passResult = "%.2f%%" % (passSum / countSum * 100)
                failResult = "%.2f%%" % (failSum / countSum * 100)
            else:
                passResult = 0
                failResult = 0
            # emailContent = f'此次一共运行接口个数为{countSum}个，通过个数为{passSum}个，通过率为{passResult}，' \
            #                f'失败个数为{failSum}个，失败率为{failResult}'
            emailContent = self.create_content('pms-api','www.jenkins.com')
        return emailContent

    # 配置发送的内容
    def create_content(self, appName, report):
        context = f"<p>美住PMS接口自动化测试报告</p>  \
                    <p>项目名称：<font color=\"info\">{appName}</font></p>  \
                    <p>执行人员：<font color=\"comment\">曾德浩</font></p>  \
                    <p>执行环境：<font color=\"comment\">test</font></p>  \
                    <p>执行时间：<font color=\"warning\">2020-04-27 22:35</font></p>    \
                    <p>执行用时：<font color=\"comment\">78s</font></p> \
                    <p>用例数量：<font color=\"comment\">200</font></p> \
                    <p>成功数量：<font color=\"info\">190</font></p>    \
                    <p>失败数量：<font color=\"warning\">10</font></p> \
                    <p>详情请查看：<a href={report}>自动化测试报告</a></p>"
        return context








if __name__ == '__main__':
    case_result = CaseResult()
    email_content = case_result.case_result(8, 4)
    print(email_content)
