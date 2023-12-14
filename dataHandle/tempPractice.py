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



if __name__ == '__main__':
    tempPractice().get_tel_address()
