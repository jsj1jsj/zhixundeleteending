import requests
import json
import urllib3
import re
from urllib import parse

urllib3.disable_warnings()

# def save_wechattoken():
#     url = 'https://t-wechat.qinghotel.com/wechat/user/decodeUserInfo/v2'
#     data = {"unionId":"oo2kw1FoBs9IcJvyy3087DWmZzw4","openId":"odEYp4z2Xx5IkKOs0NUOZzvYZZgo"}
#     headers = {"Host":"t-wechat.qinghotel.com", "content-type":"application/json"}
#     result = requests.request('post', url, json=data, headers=headers, verify=False)
#     token = json.loads(result.text)['data']['token']
#     print(token)
#     data = {
#               "token": token,
#               "Content-Type":"application/json"
#             }
#     # with open('./tempData/appletToken.json', 'w+') as f:  #linux
#     with open('../tempData/appletToken.json', 'w+') as f:   #local 3.8
#         f.write(json.dumps(data))
#         print('wechattoken is update!!!')
#
# save_wechattoken()
#
# #test
# def save_wechattoken():
#     url = 'http://dev.bms16.com/new_energy/server/api/web/?r=user/slogin'
#     data = {"code":"0f107h0w3lbLN13SuN3w35NiYG207h0v","open_data":"3535333b303434383534332f383a3335323333333732","token":"","v":"4.1.2023112201","appid":"wxefa2810018787a41"}
#     headers = {"Host":"dev.bms16.com", "content-type":"application/x-www-form-urlencoded"}
#     result = requests.request('post', url, json=data, headers=headers, verify=False)
#     data = parse.urlencode(data)
#     token = json.loads(result.text)['data']['token']
#     print(token)
#     data = {
#               "X-Token": token,
#               "Content-Type":"application/x-www-form-urlencoded"
#             }
#     # with open('./tempData/appletToken.json', 'w+') as f:  #linux
#     with open('../tempData/appletToken.json', 'w+') as f:   #local 3.8
#         f.write(json.dumps(data))
#         print('wechattoken is update!!!')
# save_wechattoken()

#pre
def save_wechattoken():
    # url = 'http://pre.bms16.com/new_energy/server/api/web/?r=user/slogin'
    # data = {"code": "0e1ZpCGa1LDfzG01USHa1wXrOF2ZpCGy","open_data": "3535333b303434383534332f3438393b333534333732","token": "","v": "4.1.2023120801","appid": "wxefa2810018787a41"}
    # headers = {"Host":"pre.bms16.com", "content-type":"application/x-www-form-urlencoded"}
    # result = requests.request('post', url, json=data, headers=headers, verify=False)
    # data = parse.urlencode(data)
    # token = json.loads(result.text)['data']['token']
    # print(token)
    data = {
              "X-Token": "ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SndJam9pY0RFaUxDSnNkQ0k2SW5WelpYSWlMQ0oxWkNJNk9ETTRNakE0TENKdklqcDdJbmQ0WDNoamVGOXBaQ0k2SW05T1NWSnpOVnBrTkVJdFRtRmtWemRPWlhGdlpGaExMWEV5WkhjaUxDSnRZV2x1WDJsa0lqb3hmU3dpWTNRaU9qRTNNREkwTXpnM056VjkuR2ZnOXpMNktkdld5cm0wZk9zTURkVU5tQnlfcEc3SGg5YThPOUJzMUd3VQ%3D%3D",
              "Content-Type":"application/x-www-form-urlencoded"
            }
    # with open('./tempData/appletToken.json', 'w+') as f:  #linux
    with open('../tempData/appletToken.json', 'w+') as f:   #local 3.8
        f.write(json.dumps(data))
        print('wechattoken is update!!!')
save_wechattoken()