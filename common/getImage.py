from PIL import Image
import requests
from io import BytesIO
import pytesseract


def getImage(tesseract_cmd,captcha_url):
    # 替换成你的 Tesseract 安装路径
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    # 替换成你的验证码图片的URL
    # captcha_url = 'https://api.admin.pre.bms16.com/?r=user/captcha&refresh=1&v=1702285307905&xCookie=1702261347690351331'

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
    #pre
    data = {"username": "zhixun", "password": "123456","verify_code": "666666", "xCookie": "1702362819430358548"}
    loginUrl = "https://api.admin.pre.bms16.com/?r=user/logon"
    tesseract_cmd = r'E:\software\tesseract\tesseract.exe'
    captcha_url = 'https://api.admin.pre.bms16.com/?r=user/captcha&refresh=1&v=1702366053005&xCookie=1702362819430358548'
    verify_code = getImage(tesseract_cmd,captcha_url)
    data["verify_code"] = verify_code
    # result = requests.request('post',loginUrl,json=data,headers=None,verify=False)
    result = requests.post(url=loginUrl, json=data, headers=None, verify=False)
    print(result.text)

    # test
    # data = {"username":"zhixun","password":"123456","verify_code":"666666","xCookie":"1702366907196955360"}
    # loginUrl = "http://api.admin.dev.bms16.com/?r=user/logon"
    # tesseract_cmd = r'E:\software\tesseract\tesseract.exe'
    # captcha_url = 'https://api.admin.dev.bms16.com/?r=user/captcha&refresh=1&v=1702366907196&xCookie=1702366907196955360'
    # verify_code = getImage(tesseract_cmd,captcha_url)
    # data["verify_code"] = verify_code
    # header={"content-type": "application/json;charset=UTF-8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"}
    # # result = requests.request('post',loginUrl,json=data,headers=header,verify=False)
    # result = requests.post(url=loginUrl, json=data, headers=None, verify=False)
    # print(result.text)