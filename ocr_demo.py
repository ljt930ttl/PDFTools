#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/5/8 22:12
# @Author : linjinting
# @Project : pdf_tools
# @File : ocr_demo.py
# @Software: PyCharm


from aip import AipOcr

class baiduApi:
    def __init__(self, APP_ID, API_KEY, SECRET_KEY, logger=None, proxies=None):
        '''
        """ 你的 APPID AK SK """
        APP_ID = '你的 App ID'
        API_KEY = '你的 Api Key'
        SECRET_KEY = '你的 Secret Key'
        '''

        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        if proxies is None:
            self.client.setProxies(proxies)

        self.m_logger = logger
    """ 读取图片 """

    def get_file_content(self, imageFile):
        with open(imageFile, 'rb') as fp:
            return fp.read()

    def getWordFromImage(self, imageFile, callback=None):
        try:
            image = self.get_file_content(imageFile)
            result = self.client.basicGeneral(image)
            if result.get("words_result"):
                words = [words_result["words"] for words_result in result["words_result"]]
                if callback:
                    callback(words)
            else:
                self.m_logger.error("结果异常：%s" %result)
        except Exception as e:
            if self.m_logger:
                self.m_logger.error(e)
            else:
                print(e)




if __name__ == '__main__':
    def callback(msg):
        print(msg)
    APP_ID = '20457265'
    API_KEY = 'VYTH0oG4XPw8wBRcIcmD02VO'
    SECRET_KEY = 'o2IhypQcXDpPXt8lVzcyTFyuDvPMGTDG'
    obj = baiduApi(APP_ID, API_KEY, SECRET_KEY)
    imageFile = r'F:\python_project\PDFTools\image\2-20_《鸟哥的Linux私房菜-基础篇》第四版_0.png'
    obj.getWordFromImage(imageFile,callback=callback)
