import requests
import json
import urllib3
import re
from urllib import parse

urllib3.disable_warnings()


#pre
def save_wechattoken():
    data = {
              "X-Token": "ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SndJam9pY0RFaUxDSnNkQ0k2SW5WelpYSWlMQ0oxWkNJNk9ETTRNakE0TENKdklqcDdJbmQ0WDNoamVGOXBaQ0k2SW05T1NWSnpOVnBrTkVJdFRtRmtWemRPWlhGdlpGaExMWEV5WkhjaUxDSnRZV2x1WDJsa0lqb3hmU3dpWTNRaU9qRTNNREkwTXpnM056VjkuR2ZnOXpMNktkdld5cm0wZk9zTURkVU5tQnlfcEc3SGg5YThPOUJzMUd3VQ%3D%3D",
              "Content-Type":"application/x-www-form-urlencoded"
            }
    # with open('./tempData/appletToken.json', 'w+') as f:  #linux
    with open('../tempData/appletToken.json', 'w+') as f:   #local 3.8
        f.write(json.dumps(data))
        print('wechattoken is update!!!')
save_wechattoken()