import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.caseResult import CaseResult
from common.utilTool import UtilTool
from common.log import Log
from common.readConfigInfo import ReadConfigInfo

logger = Log().get_logger()
reportDir = UtilTool().get_file_dirname('report')


class SendEmail:

    def get_new_file(self):
        lists = os.listdir(reportDir)  # 获取测试报告所在目录的所有文件
        lists.sort(key=lambda fn:os.path.getmtime(reportDir + '/' + fn))  # 将所有文件正序排列
        filepath = os.path.join(reportDir,lists[-1])  # 获取最新的文件路径
        return filepath

    # 定义一个可以发送附件的发送邮件的方法
    def send_email(self,startTime,totalTime,caseResult,businessFail):
        # 设置邮箱信息
        readCon = ReadConfigInfo()
        smptserver = readCon.get_config_value('emailInfo','smptserver')  # 发送邮件的服务器地址
        user = readCon.get_config_value('emailInfo','user')  # 登录邮箱的用户名
        password = readCon.get_config_value('emailInfo','password')  # 开启smpt服务的密码
        sender = readCon.get_config_value('emailInfo','sender')  # 发件方的邮箱地址
        receiver = readCon.get_config_value('emailInfo','receiver').split(',')  # 收件方邮箱地址
        subject = readCon.get_config_value('emailInfo','subject')  # 邮件主题
        # 设置邮件正文所需信息
        appName = readCon.get_config_value('emailInfo','appName')
        venv = readCon.get_config_value('emailInfo','venv')
        report = readCon.get_config_value('emailInfo','report')
        emailContent = self.create_content(appName,venv,startTime,totalTime,caseResult,businessFail,report)  # 邮件正文
        # newFile = self.get_new_file()  # 邮件附件

        # 创建一个带附件的实例
        msg = MIMEMultipart()
        # 添加邮件头
        msg['subject'] = subject
        msg['from'] = sender
        msg['bcc'] = ';'.join(receiver)
        # 添加邮件正文信息
        partContent = MIMEText(emailContent,_subtype='html',_charset='utf-8')
        msg.attach(partContent)

        try:
            logger.info(f'正在连接邮件服务器:{smptserver}:465')
            server = smtplib.SMTP_SSL(smptserver, 465)
            server.login(user,password)
            server.sendmail(sender,receiver,msg.as_string())
            server.close()
        except Exception as msg:
            logger.error(f'邮件发送失败，失败原因:{msg}')
        else:
            logger.info(f'成功发送邮件:{report}')

    # 配置发送的内容
    def create_content(self,appName,venv,startTime,totalTime,caseResult,businessFail,report):
        businessCount = caseResult['businessPassCount'] + caseResult['businessFailCount']
        context = f"<p><strong>接口自动化测试报告</strong></p>  \
                    <p>项目名称：<font color=\"blue\">{appName}</font></p>  \
                    <p>执行人员：<font color=\"gray\">AutoJob</font></p>  \
                    <p>执行环境：<font color=\"olive\">{venv}</font></p>  \
                    <p>执行时间：<font color=\"teal\">{startTime}</font></p>    \
                    <p>执行用时：<font color=\"blue\">{totalTime}s</font></p> \
                    <p>运行用例数量：<font color=\"purple\">{caseResult['caseCount']}</font></p> \
                    <p>成功用例数量：<font color=\"green\">{caseResult['passCount']}</font></p>    \
                    <p>失败用例数量：<font color=\"red\">{caseResult['failCount']}</font></p> \
                    <p>错误用例数量：<font color=\"olive\">{caseResult['errorCount']}</font></p> \
                    <p>业务场景用例数量：<font color=\"purple\">{businessCount}</font></p> \
                    <p>业务场景成功数量：<font color=\"green\">{caseResult['businessPassCount']}</font></p>    \
                    <p>业务场景失败数量：<font color=\"red\">{caseResult['businessFailCount']}</font></p> \
                    <p>失败的业务场景：<font color=\"red\">{businessFail}</font></p> \
                    <p>详情请查看：<a href={report}>自动化测试报告</a></p>"
        return context


if __name__ == '__main__':
    appN = 'pms-api'
    venv = 'test'
    startT = '2020-05-07 10:40:36'
    totalT = '98s'
    passC = 8
    failC = 4
    report_dir = "www.jenkins.com"
    caseResult = {'caseCount': 0,
                  'skipCount': 0,
                  'passCount': 0,
                  'failCount': 0,
                  'errorCount': 0,
                  'businessCaseCount': 0,
                  'businessPassCount': 0,
                  'businessFailCount': 0
                  }
    send_email = SendEmail()
    send_email.send_email(startT,totalT,caseResult)












