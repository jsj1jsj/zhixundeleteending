import requests
import json
from common.log import Log
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3

# 控制台输出移除SSL认证警告
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = Log().get_logger()


class RequestsMethod(object):
    # 重新封装requests方法，兼容post方法的两种传参格式
    def send_http_request(self,method,url,data=None,headers=None):
        if method == 'get':
            result = requests.request('get',url,params=data,headers=headers,verify=False)
        elif method == 'post':
            result = requests.request('post',url,json=data,headers=headers,verify=False)
        elif method == 'post-data':
            result = requests.request('post',url,data=data,headers=headers,verify=False)
        elif method == 'post-post':
            result = requests.post(url, data=data, headers=headers)
        else:
            result = requests.request('put',url,json=data,headers=headers,verify=False)
        # resCode = result.status_code
        try:
            jsonHeaders = result.headers['Content-Type']
        except:
            jsonHeaders = 'hotel_test'
        if 'json' in jsonHeaders:
            res = json.dumps(result.json(),ensure_ascii=False)
        else:
            res = result.text
        return res

    # 统一封装post,get,put,delete方法 返回字符串类型数据用于断言
    def send_request(self,method,url,data=None,headers=None):
        if method == 'post':
            result = self.send_post(url,data,headers)
        elif method == 'get':
            result = self.send_get(url,data,headers)
        elif method == 'put':
            result = self.send_put(url,data,headers)
        else:
            result = self.send_delete(url,data,headers)
        if not isinstance(result,str):
            return json.dumps(result,ensure_ascii=False)  # 返回中文字符串
        else:
            return result

    # 封装post方法verify=False关闭认证
    def send_post(self,url,data,headers=None):
        try:
            if headers:
                result = requests.post(url=url,json=data,headers=headers,verify=False)
            else:
                result = requests.post(url=url,json=data,verify=False)
            resCode = result.status_code
            if 'json' in result.headers['Content-Type']:
                result = result.json()
            else:
                result = result.text
            logger.info(f'成功发送post请求，请求结果code码为：{resCode}，请求结果为：{result}')
            return result
        except Exception as msg:
            logger.error(f'非json格式数据，无法转换')
            return {'code':1,'error':f'post请求失败，错误原因：{msg}'}

    # 封装get请求
    def send_get(self,url,data=None,headers=None):
        try:
            if headers:
                result = requests.get(url=url,params=data,headers=headers,verify=False)
            else:
                result = requests.get(url=url,params=data,verify=False)
            resCode = result.status_code
            res = result.json()
            logger.info(f'成功发送get请求，请求结果code码为：{resCode}，请求结果为：{res}')
            return res
        except Exception as msg:
            logger.error(f'get请求失败，出错原因：{msg}')
            return {'code':1,'error':f'get请求失败，错误原因：{msg}'}

    # 封装put方法
    def send_put(self,url,data,headers=None):
        try:
            if headers:
                result = requests.put(url=url,data=data,headers=headers,verify=False)
            else:
                result = requests.put(url=url,data=data,verify=False)
            resCode = result.status_code
            res = result.json()
            logger.info(f'成功发送put请求，请求结果code码为：{resCode}，请求结果为：{res}')
            return res
        except Exception as msg:
            logger.error(f'put请求失败，出错原因：{msg}')
            return {'code': 1, 'error': f'put请求失败，错误原因：{msg}'}

    # 封装put方法
    def send_delete(self, url, data, headers=None):
        try:
            if headers:
                result = requests.delete(url=url, params=data, headers=headers,verify=False)
            else:
                result = requests.put(url=url, params=data, verify=False)
            resCode = result.status_code
            res = result.json()
            logger.info(f'成功发送delete请求，请求结果code码为：{resCode}，请求结果为：{res}')
            return res
        except Exception as msg:
            logger.error(f'delete请求失败，出错原因：{msg}')
            return {'code': 1, 'error': f'put请求失败，错误原因：{msg}'}


if __name__ == '__main__':
    rm = RequestsMethod()


