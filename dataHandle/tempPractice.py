import random
import string

import requests


class tempPractice(object):

    # 生成一个随机数(18位)
    def get_random_pyaNo(self):
        payNo = random.randint(10000000000000000, 99999999999999999)
        print(payNo)

    # 生成一个随机字符串(12位)
    def get_random_uuid(self):
        uuid = ''.join(random.sample(string.ascii_letters + string.digits, 12))
        print(uuid)

    # 查询手机号归属地
    def get_tel_address(self):
        for i in range(0, 1):
            try:
                url = "http://tcc.taobao.com/cc/json/mobile_tel_segment.htm"
                params = {
                    "tel": 13724328658
                }
                r = requests.get(url=url, params=params, verify=False, timeout=1)
                print(r.text)
                print(r.status_code)
            except:
                print("错误Test!")



if __name__ == '__main__':
    # tempPractice().get_random_pyaNo()
    # tempPractice().get_random_uuid()
    tempPractice().get_tel_address()
    # tempPractice().get_room_state()
