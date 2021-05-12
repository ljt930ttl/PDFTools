#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2021/5/10 11:12
@Author:  linjinting
@File: baidu-aip-demo.py
@Software: PyCharm
"""



from aip import AipOcr
def getWordFromImage(APP_ID, API_KEY, SECRET_KEY, imageFile):
    with open(imageFile, 'rb') as fp:
        image = fp.read()
    try:
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        result = client.basicGeneral(image)
        if result.get("words_result"):
            words = [words_result["words"] for words_result in result["words_result"]]
            return words
        else:
            print("结果异常：%s" % result)
    except Exception as e:
        print(e)
import requests
import base64
import json
def api_getToken(AK,SK, logger=None):
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' %(AK,SK)
    response = requests.get(host)
    if response:
        if logger:
            logger.info("token 有效期30天: %s" % response.json())
        else:
            print(response.json())

def api_getWordFromImage(imageFile, access_token, callback=None, logger=None):
    with open(imageFile, 'rb') as fp:
        file = fp.read()
    img = base64.b64encode(file)
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"

    params = {"image": img}
    # access_token = '[调用鉴权接口获取的token]'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    try:
        response = requests.post(request_url, data=params, headers=headers, timeout=60)
    except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout, requests.exceptions.ProxyError,) as e:
        logger.error(e)
        return

    if response:
        # print(response.json())
        if response.status_code != 200:
            if logger:
                logger.error({'error_code': response.status_code, 'error_msg': response.reason})
            else:
                print({'error_code': response.status_code, 'error_msg': response.reason})
            return

        result = json.loads(response.content.decode()) or {}
        words = [words_result["words"] for words_result in result["words_result"]]
        # text = "\n".join(words)
        if callback:
            callback(words)
        else:
            print(words)

if __name__ == '__main__':
    # APP_ID = '20457265'
    API_KEY = 'VYTH0oG4XPw8wBRcIcmD02VO'
    SECRET_KEY = 'o2IhypQcXDpPXt8lVzcyTFyuDvPMGTDG'
    imageFile = r'F:\python_project\PDFTools\image\2-20_1.png'
    # words = getWordFromImage(APP_ID, API_KEY, SECRET_KEY, imageFile)
    # print(words)
    # api_getToken(API_KEY, SECRET_KEY)
    api_getWordFromImage(imageFile,"24.160d830cf8e26ceba1f42334bec139a5.2592000.1623220220.282335-20457265")