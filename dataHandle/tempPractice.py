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

    # 查询房态图列表
    def get_room_state(self):
        url = "https://pms.qinghotel.com/pms/frontdesk/hotel/room/state?floor=-90&guestType=&roomState=&roomType=&settlement=&stayType=&defaultStatistical=&bindLock=false&hotelCode=10666431"
        headers = {
            "cookie": "t-perm_auth_login_platform_token=76e6c10065d3d1daa4e679bd7011121c; t-pms_appId=461; UM_distinctid=175936302be9c6-0999b45c6a2172-376b4502-e1000-175936302bf962; perm_auth_login_platform_token=d535a876a15e187fde45c97f4c77dea2; pms_appId=1461; d535a876a15e187fde45c97f4c77dea2_isFirst=true; JSESSIONID=4707EC3E1C1C8C632698A65248C45F28; CNZZDATA1279005589=1255829563-1604491558-https%253A%252F%252Fperm.qinghotel.com%252F%7C1604553637",
            "token": "d535a876a15e187fde45c97f4c77dea2",
            "hotelcode": "10666431"
        }
        result = requests.get(url=url, headers=headers)
        print(result.text)


if __name__ == '__main__':
    # tempPractice().get_random_pyaNo()
    # tempPractice().get_random_uuid()
    tempPractice().get_tel_address()
    # tempPractice().get_room_state()
