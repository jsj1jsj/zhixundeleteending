import os
import datetime

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 脚本路径
# filename = 'fmis.xls'
filename = 'zhixun.xls'

TEST_CASE_PATH = os.path.join(BASE_PATH, 'dataCase', filename)

# 配置文件路径
filepath = 'test1Config.ini'
# filepath = 'test1Config.ini'
# filepath = 'masterConfig.ini'
CON_FILE_PATH = os.path.join(BASE_PATH,'configFile',filepath)

# headers文件路径
PMSHeaders = 'headers.json'
appletHeaders = 'appletToken.json'
PMS_HEADERS_PATH = os.path.join(BASE_PATH,'tempData',PMSHeaders)
APPLET_HEADERS_PATH = os.path.join(BASE_PATH,'tempData',appletHeaders)


# 报告路径
TEST_CASE_REPORT_PATH = os.path.join(BASE_PATH, 'report', 'report.html')

# 用于生成allure报告的数据的路径
ALLURE_DATA_PATH = os.path.join(BASE_PATH,'report','result')

# 请求参数路径
REQUEST_PARAMS_PATH = os.path.join(BASE_PATH,'dataCase','jsonParams')

# sql语句路径
SQL_PATH = os.path.join(BASE_PATH,'dataCase','sqlParams','sqlExecute.json')

# ------------ allure 相关配置 -----------
resultPath = os.path.join(BASE_PATH, 'report', 'result')
allureHtmlPath = os.path.join(BASE_PATH, 'report', 'allure_html')
ALLURE_COMMAND = 'allure generate {} -o {} --clean'.format(resultPath, allureHtmlPath)

# ---------------- 日志相关 --------------------
# 日志级别
LOG_LEVEL = 'debug'
LOG_STREAM_LEVEL = 'debug'  # 屏幕输出流
LOG_FILE_LEVEL = 'info'  # 文件输出流

# 日志文件命名
LOG_FILE_NAME = os.path.join(BASE_PATH, 'logs', datetime.datetime.now().strftime('%Y-%m-%d') + '.log')

# 日志路径
LOG_FILE_PATH = os.path.join(BASE_PATH,'logs')

if __name__ == '__main__':
    print(BASE_PATH)
    print(TEST_CASE_PATH)
    print(SQL_PATH)