#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2021/5/7 17:29
@Author:  linjinting
@File: PictureToPDF.py
@Software: PyCharm
"""
import os
import glob
import fitz

def getFileLists(file_path, file_type):
    if os.path.isfile(file_path):
        return [file_path]
    pathname = os.path.join(file_path, "*.%s" % file_type) # "D:/xxx/*.png"
    return sorted(glob.glob(pathname))

def convert_to_pdf(source_path, destination_path, file_type="png", logger=None):
    files = getFileLists(source_path, file_type)
    for img in files:  # 读取图片，确保按文件名排序
        doc = fitz.open()
        fileName = os.path.basename(img).split(".")[0]
        destination_name = os.path.join(destination_path, "%s.pdf" % fileName)
        if logger:
            logger.info("正在转换%s，到%s"%(fileName, destination_name))
        else:
            print("正在转换%s，到%s"%(fileName, destination_name))

        imgdoc = fitz.open(img)  # 打开图片
        pdfbytes = imgdoc.convertToPDF()  # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        # imgpdf.save(fileName+".pdf")
        doc.insertPDF(imgpdf)  # 将当前页插入文档
        if os.path.exists(destination_name):
            os.remove(destination_name)
        doc.save(destination_name)  # 保存pdf文件
        doc.close()

def convert_to_pdf_simple(source_path, destination_name, file_type="png", logger=None):
    files = getFileLists(source_path, file_type)
    doc = fitz.open()
    for img in files:  # 读取图片，确保按文件名排序
        imgdoc = fitz.open(img)  # 打开图片
        pdfbytes = imgdoc.convertToPDF()  # 使用图片创建单页的 PDF
        if logger:
            logger.info("正在转换%s" % img)
        else:
            print("正在转换%s" % img)

        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)  # 将当前页插入文档
        if logger:
            logger.info("正在把%s插入到%s" % (img, destination_name))
        else:
            print("正在把%s插入到%s" % (img, destination_name))

    if os.path.exists(destination_name):
        os.remove(destination_name)
    doc.save(destination_name)  # 保存pdf文件
    doc.close()

def convert_to_image(source_path, destination_path, logger=None, **kwargs):
    files = getFileLists(source_path, kwargs.get('type', "pdf"))
    logger.debug(files)
    for pdf_file in files:
        doc = fitz.open(pdf_file)
        new_fileName = os.path.basename(pdf_file).split(".")[0]

        rotate = kwargs.get('rotate', 0)  # 设置图片的旋转角度
        zoom_x = kwargs.get('zoom_x', 2.0)  # 设置图片相对于PDF文件在X轴上的缩放比例
        zoom_y = kwargs.get('zoom_y', 2.0)  # 设置图片相对于PDF文件在Y轴上的缩放比例
        alpha = kwargs.get('alpha', 0)  #
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        if logger:
            logger.info("%s开始转换...当前缩放比例为x:%d,y%d" % (new_fileName,zoom_x,zoom_y))
        else:
            print("%s开始转换...当前缩放比例为x:%d,y%d" % (new_fileName,zoom_x,zoom_y))
        for pg in range(doc.page_count):
            destination_name = os.path.join(destination_path, "%s_%s.%s" % (new_fileName, pg, kwargs.get('img_type', 'png')))
            if logger:
                logger.info("正在转换%s, 第%d页，到%s"%(new_fileName, pg, destination_name))
            else:
                print("正在转换%s, 第%d页，到%s"%(new_fileName, pg, destination_name))

            page = doc[pg]
            pm = page.getPixmap(matrix=trans, alpha=alpha)
            pm.writeImage(destination_name)


if __name__ == '__main__':
    convert_to_image("./pdf", "image")