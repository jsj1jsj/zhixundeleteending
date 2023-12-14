# 特殊数据处理
import time
import datetime
import pytz
from PIL import Image
import requests
from io import BytesIO
import pytesseract


class EspecialData(object):
    # 获取房间折扣价格
    def get_discounts_price(self,price, discount):
        if discount:
            roomPrice = price * (100 - int(discount)) / 100
        else:
            roomPrice = price
        newPrice = '%0.2f'%(round(roomPrice,2))
        return newPrice

    # 获取营业日
    # def get_business_day(self):
    #     return time.strftime('%Y-%m-%d', time.localtime())

    # 获取营业日期：
    def get_business_day(self):
        return datetime.datetime.now().strftime('%Y-%m-%d')

    def get_UTC_time(self,day):
        current_utc_time = datetime.datetime.now(pytz.utc)
        next_day = current_utc_time + datetime.timedelta(days=day)
        # 格式化为 ISO 8601 格式
        formatted_next_day = next_day.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        return formatted_next_day

    # 生成一个时间（生成入住、离店时间）
    def get_target_time(self,days):
        targetTime = (datetime.datetime.now() + datetime.timedelta(days=days)).strftime('%Y-%m-%d %H:%M:%S')
        return targetTime

    # 生成一个时间（YYYYMMMDDHHMMSS格式）datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    def get_order_time(self):
        orderTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return orderTime

    # 生成一个日期
    def get_target_date(self,days):
        targetDate = (datetime.datetime.now() + datetime.timedelta(days=days)).strftime('%Y-%m-%d')
        return targetDate

    # 生成一个日期6
    def get_target_date6(self,days):
        targetDate = (datetime.datetime.now() + datetime.timedelta(days=days)).strftime('%Y%m%d')
        return targetDate

    # str类型的日期转换为时间戳(10位)
    def get_time_stamp(self,timeStr):
        # 转为时间数组
        timeArray = time.strptime(timeStr,'%Y-%m-%d')
        timestamp = int(time.mktime(timeArray))
        return timestamp

    # str类型的日期转换为13位的时间戳
    def get_time_stamp13(self,timeStr):
        timeArray = datetime.datetime.strptime(timeStr,'%Y-%m-%d %H:%M:%S')
        # 10位
        timeStamp = str(int(time.mktime(timeArray.timetuple())))
        # 3位，秒
        timeMicrosecond = str('%06d'%timeArray.microsecond)[0:3]
        timeStamp = timeStamp + timeMicrosecond
        return int(timeStamp)


    # 生成一个字符串类型随机数
    def get_random_num(self):
        nowTime = time.time()*100
        return int(nowTime)
    def get_target_datetime(self, hours):
        now = datetime.datetime.now()
        #        now = datetime.datetime(2021,7,21,21,00,000)
        target_date = datetime.datetime.today().date()
        target_time = datetime.time( 22, 30, 00, 000 )
        target = datetime.datetime.combine( target_date, target_time )
        if (target - now).seconds < hours * 60 * 60:
            targetDate = target.strftime( '%Y-%m-%d %H:%M:%S' )
        else:
            targetDate = (datetime.datetime.now() + datetime.timedelta( hours=hours )).strftime( '%Y-%m-%d %H:%M:%S' )
        return targetDate
    def getImage(self,tesseract_cmd,captcha_url):
        # 替换成你的 Tesseract 安装路径
        pytesseract.pytesseract.tesseract_cmd = r'E:\software\tesseract\tesseract.exe'


        # 发送请求获取验证码图片
        response = requests.get(captcha_url)

        if response.status_code == 200:
            # 从响应中获取图片内容
            image_data = BytesIO(response.content)

            # 使用Pillow库打开图片
            image = Image.open(image_data)

            # 图片预处理，如果需要的话
            # ...

            # 使用Tesseract OCR进行文字识别
            captcha_text = pytesseract.image_to_string(image).strip()

            print("识别的验证码：", captcha_text)
        else:
            print("Failed to retrieve captcha image.")

        return captcha_text


if __name__ == '__main__':
    es = EspecialData()
    st = es.get_target_date(-1)
    # et = es.get_target_date(1)
    # at = es.get_time_stamp(st)
    # at1 = es.get_time_stamp13(st)
    # lt = es.get_time_stamp13(et)
    print(type(st),st)
    # print(type(et),et)
    # print(type(at),at)
    # print(type(at),at1)
    # print(type(lt),lt)



