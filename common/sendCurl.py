import subprocess

class sendCurl:
    def send_curl(self,firstdata,k1,k2,k3,k4,k5,remark):

        url = f"http://devops.bms16.com/?r=index/index&firstData={firstdata}&k1={k1}&k2={k2}&k3={k3}&k4={k4}&k5={k5}&remark={remark}"
        # print(url)
        # 定义cURL命令
        process = subprocess.Popen(["curl", url], stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output.decode("utf-8"))


#
if __name__ == '__main__':
    # firstdata = 'api'
    # k1 = 'test'
    # k2 = '14:24:36'
    # k3 = '98s'
    # k4 = 8
    # k5 = 4
    # remark = "note"
    # send_curl = sendCurl()
    # send_curl.send_curl(firstdata,k1,k2,k3,k4,k5,remark)
