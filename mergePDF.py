#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2021/5/6 16:55
@Author:  linjinting
@File: mergePDF.py
@Software: PyCharm
"""

import os
from PyPDF2 import PdfFileReader, PdfFileWriter
# import time

# 使用os模块的walk函数，搜索出指定目录下的全部PDF文件
# 获取同一目录下的所有PDF文件的绝对路径
def getFileName(filedir):

    file_list = [os.path.join(root, filespath) \
                 for root, dirs, files in os.walk(filedir) \
                 for filespath in files \
                 if str(filespath).endswith('pdf')
                 ]
    return file_list if file_list else []

def getFileName_not_recursion(filedir):

    file_list = [os.path.join(filedir, files) \
                 for files in os.listdir(filedir) \
                 # for filespath in files
                 if str(files).endswith('pdf')
                 ]
    return file_list if file_list else []

# 合并同一目录下的所有PDF文件
def MergePDF(filepath, outfile, logger=None):

    output = PdfFileWriter()
    outputPages = 0
    pdf_fileName = getFileName(filepath)

    if pdf_fileName:
        for pdf_file in pdf_fileName:
            # 读取源PDF文件
            input = PdfFileReader(open(pdf_file, "rb"))
            # 获得源PDF文件中页面总数
            pageCount = input.getNumPages()
            outputPages += pageCount
            logger.info("路径：%s 页数：%d"%(pdf_file, pageCount))

            # 分别将page添加到输出output中
            for iPage in range(pageCount):
                output.addPage(input.getPage(iPage))

        logger.info("合并后的总页数:%d."%outputPages)
        # 写入到目标PDF文件
        outputStream = open(outfile, "wb")
        output.write(outputStream)
        outputStream.close()
        logger.info("PDF文件合并完成！")

    else:
        logger.info("没有可以合并的PDF文件！")


if __name__ == '__main__':
    # time1 = time.time()
    file_dir = r'.'  # 存放PDF的原文件夹
    print(getFileName(file_dir))
    # outfile = "Cheat_Sheets.pdf"  # 输出的PDF文件的名称
    # MergePDF(file_dir, outfile)
    # time2 = time.time()
    # print('总共耗时：%s s.' %(time2 - time1))