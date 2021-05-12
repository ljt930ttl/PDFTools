#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2021/5/6 17:22
@Author:  linjinting
@File: main.py
@Software: PyCharm
"""

import sys
import logging
import threading
from PySide2 import QtWidgets
from UI_tools import Ui_Form_PDF_Tools
from TTLLogging import create_logger
from baidu_aip_demo import api_getWordFromImage, api_getToken
from pdf_convert import convert_to_pdf_simple, convert_to_pdf
from separatePDF import SeparatePDF
from mergePDF import MergePDF

class UIHandle(logging.StreamHandler):
    def __init__(self, widget):
        logging.StreamHandler.__init__(self, widget)
        self.formatter = logging.Formatter("[%(asctime)s] %(levelname)s in %(name)s.%(module)s at %(lineno)d: %(message)s")


class Form_PDF_Tools(QtWidgets.QFrame, Ui_Form_PDF_Tools):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bound_single()

        self.m_logger = create_logger('pdf.tools.main')
        handle = UIHandle(self)
        self.m_logger.addHandler(handle)

        # self.tabWidget.tabBar().removeTab(3)
    def test(self):
        def p():
            ww = ['如果你的主机是用来打3D游戏的,那么显示适配器的选购是非常重要喔!如果你的主机是用来做为', '网络服务器的,那么简单的入门级显示适配器对你的主机来说就非常够用了!因为网络服务器很少',
                  '用到3D与图形影像功能', '例题', '假设你的桌面使用1024×768分辨率,且使用全彩(每个像素占用3 bytes的容量),请问你的显示适配器至少需要多', '少内存才能使用这样的彩度',
                  '答', '因为1024×768分辨率中会有786432个像素,每个像素占用3 bytes,所以总共需要2.25 MBytes以上才行!但如果',
                  '考虑屏幕的更新率(每秒钟屏幕的更新次数),显示适配器的内存还是越大越好', '除了显示适配器与主板的连接接口需要知道外,那么显示适配器是透过什么格式与计算机屏幕(或电',
                  '视)连接的呢?目前主要的连接接口有', 'D-Sub(VGA端子):为较早之前的连接接口,主要为15针的连接,为模拟讯号的传输,当初设计是针对',
                  '传统映像管屏幕而来。主要的规格有标准的640x350pX@7OHz、1280x1024px@85Hz及2048x1536pX', '@85Hz等',
                  'DVI:共有四种以上的接头,不过台湾市面上比较常见的为仅提供数字讯号的DⅥI-D,以及整合数字与模',
                  '拟讯号的DⅥII两种。DⅥⅠ常见于液晶屏幕的链接,标准规格主要有:1920x1200px@6OHz', '2560X1600X@6OHz等',
                  'HDMI:相对于Dsub与DⅵI仅能传送影像数据,HDMI可以同时传送影像与声音,因此被广泛的使用', '于电视屏幕中!计算机屏幕目前也经常都有支持HDMI格式',
                  'Display port:与HDMI相似的,可以同时传输声音与影像。不过这种界面目前在台湾还是比较少屏幕的支', '持', '024硬盘与储存设备',
                  '计算机总是需要记录与读取数据的,而这些数据当然不可能每次都由用户经过键盘来打字!所以就需', '要有储存设备咯。计算杋系统上面的储存设备包括有:硬盘、软盘、MO、CD、DVD、磁带机、随',
                  '身碟(闪存)、还有新一代的蓝光光驱等,乃至于大型机器的局域网络储存设备(SAN,NAS)等等,都', '是可以用来储存数据的。而其中最常见的应该就是硬盘了吧', '硬盘的物理组成',
                  '大家应该都看过硬盘吧!硬盘依据桌上型与笔记本电脑而有分为3.5吋及2.5吋的大小。我们以3.5', '吋的桌面计算机使用硬盘来说明。在硬盘盒里面其实是由许许多多的圆形磁盘盘、机械手臂、磁盘',
                  '读取头与主轴马达所组成的,整个内部如同下图所']
            # for word in words:
            #     print(word)
            w = "\n".join(ww)
            self.textEdit_test.insertPlainText(w)
        threading.Thread(target=p).start()

    def bound_single(self):
        self.pushButton_test.clicked.connect(self.test)
        # separate
        self.pushButton_separate_source.clicked.connect(self.separate_getOpenFileName)
        self.pushButton_separate_destination.clicked.connect(self.separate_getExistingDirectory)
        self.pushButton_separate.clicked.connect(self.separate_pdf)
        # merge
        self.pushButton_merge_save.clicked.connect(self.merge_getSaveFileName)
        self.pushButton_merge_source.clicked.connect(self.merge_getExistingDirectory)
        self.pushButton_merge.clicked.connect(self.merge_pdf)
        # convert_image
        self.pushButton_convert_image_source_file.clicked.connect(self.convert_image_getOpenFileName)
        self.pushButton_convert_image_source_dir.clicked.connect(self.convert_image_source_getExistingDirectory)
        self.pushButton_convert_image_destination.clicked.connect(self.convert_image_getExistingDirectory)
        self.pushButton_convert_image.clicked.connect(self.convert_image)
        # convert_pdf
        self.pushButton_convert_pdf_source.clicked.connect(self.convert_pdf_getOpenFileName)
        self.pushButton_convert_pdf_source_dir.clicked.connect(self.convert_pdf_source_getExistingDirectory)
        self.pushButton_convert_pdf_destination_file.clicked.connect(self.convert_pdf_getSaveFileName)
        self.pushButton_convert_pdf_destination.clicked.connect(self.convert_pdf_getExistingDirectory)
        self.pushButton_convert_pdf.clicked.connect(self.convert_pdf)
        # baidu ocr
        self.pushButton_ocr_source.clicked.connect(self.ocr_source_getOpenFileName)
        self.pushButton_baidu_aip_token.clicked.connect(self.baidu_ai_get_token)
        self.pushButton_baidu_ocr.clicked.connect(self.baidu_aip_ocr)


    def separate_getOpenFileName(self):
        file_path, file_type = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', '', 'pdf(*.pdf)')
        self.lineEdit_separate_source.setText(file_path)

    def separate_getExistingDirectory(self):
        file_path = QtWidgets.QFileDialog.getExistingDirectory(self, '选择保存路径')
        self.lineEdit_separate_destination.setText(file_path)

    def merge_getExistingDirectory(self):
        source_path = QtWidgets.QFileDialog.getExistingDirectory(self, '选择保存路径')
        self.lineEdit_merge_source_dir.setText(source_path)

    def merge_getSaveFileName(self):
        file_path, file_type = QtWidgets.QFileDialog.getSaveFileName(self, '选择保存路径', 'merge.pdf', 'pdf(*.pdf)')
        # print(file_path, file_type)
        if not file_path:
            file_path = 'merge.pdf'
        self.lineEdit_merge_save.setText(file_path)

    def convert_image_getOpenFileName(self):
        file_path, file_type = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', '', 'pdf(*.pdf)')
        self.lineEdit_convert_image_source_file.setText(file_path)
        self.lineEdit_convert_image_source_dir.setText("")

    def convert_image_source_getExistingDirectory(self):
        file_path = QtWidgets.QFileDialog.getExistingDirectory(self, '选择文件夹')
        self.lineEdit_convert_image_source_dir.setText(file_path)
        self.lineEdit_convert_image_source_file.setText("")

    def convert_image_getExistingDirectory(self):
        file_path = QtWidgets.QFileDialog.getExistingDirectory(self, '选择保存路径')
        self.lineEdit_convert_image_destination.setText(file_path)

    def convert_pdf_getOpenFileName(self):
        img_type = self.comboBox_convert_pdf_img_type.currentText()
        file_path, file_type = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', '', '%s(*.%s)'% (img_type,img_type))
        self.lineEdit_convert_pdf_source.setText(file_path)
        self.lineEdit_convert_pdf_source_dir.setText("")

    def convert_pdf_source_getExistingDirectory(self):
        file_path = QtWidgets.QFileDialog.getExistingDirectory(self, '选择文件夹')
        self.lineEdit_convert_pdf_source_dir.setText(file_path)
        self.lineEdit_convert_pdf_source.setText("")

    def convert_pdf_getSaveFileName(self):
        file_path, file_type = QtWidgets.QFileDialog.getSaveFileName(self, '选择文件', '', 'pdf(*.pdf)')
        self.lineEdit_convert_pdf_destination_dir.setText("")
        self.lineEdit_convert_pdf_destination.setText(file_path)

    def convert_pdf_getExistingDirectory(self):
        file_path = QtWidgets.QFileDialog.getExistingDirectory(self, '选择保存路径')
        self.lineEdit_convert_pdf_destination_dir.setText(file_path)
        self.lineEdit_convert_pdf_destination.setText("")

    def ocr_source_getOpenFileName(self):
        file_path, file_type = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', '', 'Image files(*.bmp *.jpg *.pbm *.pgm *.png *.ppm *.xbm *.xpm);;All files (*.*)')
        self.lineEdit_ocr_source.setText(file_path)

    def separate_pdf(self):
        source_file = self.lineEdit_separate_source.text()
        output_path = self.lineEdit_separate_destination.text()

        pattern = self.lineEdit_separate_pattern.text()
        if not source_file:
            self.m_logger.error("源文件为空，退出！")
            return
        if not output_path:
            self.m_logger.error("存放目录为空，退出！")
            return
        if not pattern:
            self.m_logger.error("分割方式为空，退出！")
            return
        SPDF = SeparatePDF(self.m_logger)
        th = threading.Thread(target=SPDF.run, args=[pattern, source_file, output_path])
        th.start()
        # SPDF.run(pattern, source_file, output_path)

    def merge_pdf(self):
        source_path = self.lineEdit_merge_source_dir.text()
        save_path = self.lineEdit_merge_save.text()
        if not source_path:
            self.m_logger.error("源目录路径为空，退出！")
            return
        if not save_path:
            self.m_logger.error("保存文件路径为空，退出!")
            return
        th = threading.Thread(target=MergePDF, args=[source_path, save_path, self.m_logger])
        th.start()
        # MergePDF(source_path, save_path, self.m_logger)

    def convert_image(self):
        file_path = self.lineEdit_convert_image_source_file.text()
        dir_path = self.lineEdit_convert_image_source_dir.text()
        destination_path = self.lineEdit_convert_image_destination.text()
        img_type = self.comboBox_convert_img_img_type.currentText()
        try:
            rotate = int(self.lineEdit_convert_image_rotate.text())
            zoom_x = float(self.lineEdit_convert_image_zoomX.text())
            zoom_y = float(self.lineEdit_convert_image_zoomY.text())
            alpha = int(self.lineEdit_convert_image_alpha.text())
        except Exception as e:
            self.m_logger.error(e)
            self.m_logger.error("转换参数错误，系统使用默认值！")
            rotate = 0
            zoom_x = 2.0
            zoom_y =2.0
            alpha = 0
        kwargs = {
            "img_type": img_type,
            "rotate": rotate ,
            "zoom_x": zoom_x ,
            "zoom_y": zoom_y ,
            "alpha": alpha ,
        }
        self.m_logger.debug(kwargs)
        if not dir_path and not file_path:
            self.m_logger.error("源目录及源文件路径不能同时为空，退出！")
            return
        if not destination_path:
            self.m_logger.error("保存目录路径为空，退出!")
            return
        from pdf_convert import convert_to_image
        if not dir_path:
            source_path = file_path
        else:
            source_path = dir_path
        th = threading.Thread(target=convert_to_image,
                              args=[source_path, destination_path, self.m_logger], kwargs=kwargs)
        th.start()
        # convert_to_image(source_path, destination_path, self.m_logger, **kwargs)

    def convert_pdf(self):
        source_file_path = self.lineEdit_convert_pdf_source.text()
        source_dir_path = self.lineEdit_convert_pdf_source_dir.text()
        destination_path = self.lineEdit_convert_pdf_destination.text()
        destination_dir_path = self.lineEdit_convert_pdf_destination_dir.text()
        img_type = self.comboBox_convert_pdf_img_type.currentText()

        if source_file_path:
            source_path = source_file_path
        elif source_dir_path:
            source_path = source_dir_path
        else:
            self.m_logger.error("源文件及源目录路径不能同时为空，退出!")
            return

        if destination_path:
            th = threading.Thread(target=convert_to_pdf_simple,
                                  args=[source_path, destination_path, img_type, self.m_logger])
            th.start()
            # convert_to_pdf_simple(source_path, destination_path, img_type, self.m_logger)
        elif destination_dir_path:
            th = threading.Thread(target=convert_to_pdf,
                                  args=[source_path, destination_path, img_type, self.m_logger])
            th.start()
            # convert_to_pdf(source_path, destination_dir_path, img_type, self.m_logger)
        else :
            self.m_logger.error("保存目录及保存文件不能同时为空，退出！")
            return
    def baidu_ai_get_token(self):
        API_KEY = self.lineEdit_baiduAPI_API_KEY.text()
        SECRET_KEY = self.lineEdit_baiduAPI_SECRET_KEY.text()


        api_getToken(API_KEY, SECRET_KEY, self.m_logger)

    def baidu_aip_ocr(self):
        # APP_ID = '20457265'
        # API_KEY = 'VYTH0oG4XPw8wBRcIcmD02VO'
        # SECRET_KEY = 'o2IhypQcXDpPXt8lVzcyTFyuDvPMGTDG'
        # APP_ID = self.lineEdit_baiduAPI_APP_ID.text()
        # API_KEY = self.lineEdit_baiduAPI_API_KEY.text()
        # SECRET_KEY = self.lineEdit_baiduAPI_SECRET_KEY.text()
        token = self.lineEdit_token.text()
        source_path = self.lineEdit_ocr_source.text()
        if not source_path:
            self.m_logger.error("源目录路径为空，退出！")
            return
        self.m_logger.info("开始识别%s上的文字" %source_path)
        self.textEdit_ocr_result.setText("")

            # self.m_logger.info("识别完成")


        th = threading.Thread(target=api_getWordFromImage, args=[source_path, token, self.ocr_callback, self.m_logger])
        th.start()
        # words = client.getWordFromImage(source_path)

    def write(self, msg):
        self.textBrowser_log.insertPlainText(msg)
        self.textBrowser_log.moveCursor(self.textBrowser_log.textCursor().End)

    def ocr_callback(self, words):
        self.m_logger.info("开始回显文字")
        # ww = ['如果你的主机是用来打3D游戏的,那么显示适配器的选购是非常重要喔!如果你的主机是用来做为', '网络服务器的,那么简单的入门级显示适配器对你的主机来说就非常够用了!因为网络服务器很少', '用到3D与图形影像功能', '例题', '假设你的桌面使用1024×768分辨率,且使用全彩(每个像素占用3 bytes的容量),请问你的显示适配器至少需要多', '少内存才能使用这样的彩度', '答', '因为1024×768分辨率中会有786432个像素,每个像素占用3 bytes,所以总共需要2.25 MBytes以上才行!但如果', '考虑屏幕的更新率(每秒钟屏幕的更新次数),显示适配器的内存还是越大越好', '除了显示适配器与主板的连接接口需要知道外,那么显示适配器是透过什么格式与计算机屏幕(或电', '视)连接的呢?目前主要的连接接口有', 'D-Sub(VGA端子):为较早之前的连接接口,主要为15针的连接,为模拟讯号的传输,当初设计是针对', '传统映像管屏幕而来。主要的规格有标准的640x350pX@7OHz、1280x1024px@85Hz及2048x1536pX', '@85Hz等', 'DVI:共有四种以上的接头,不过台湾市面上比较常见的为仅提供数字讯号的DⅥI-D,以及整合数字与模', '拟讯号的DⅥII两种。DⅥⅠ常见于液晶屏幕的链接,标准规格主要有:1920x1200px@6OHz', '2560X1600X@6OHz等', 'HDMI:相对于Dsub与DⅵI仅能传送影像数据,HDMI可以同时传送影像与声音,因此被广泛的使用', '于电视屏幕中!计算机屏幕目前也经常都有支持HDMI格式', 'Display port:与HDMI相似的,可以同时传输声音与影像。不过这种界面目前在台湾还是比较少屏幕的支', '持', '024硬盘与储存设备', '计算机总是需要记录与读取数据的,而这些数据当然不可能每次都由用户经过键盘来打字!所以就需', '要有储存设备咯。计算杋系统上面的储存设备包括有:硬盘、软盘、MO、CD、DVD、磁带机、随', '身碟(闪存)、还有新一代的蓝光光驱等,乃至于大型机器的局域网络储存设备(SAN,NAS)等等,都', '是可以用来储存数据的。而其中最常见的应该就是硬盘了吧', '硬盘的物理组成', '大家应该都看过硬盘吧!硬盘依据桌上型与笔记本电脑而有分为3.5吋及2.5吋的大小。我们以3.5', '吋的桌面计算机使用硬盘来说明。在硬盘盒里面其实是由许许多多的圆形磁盘盘、机械手臂、磁盘', '读取头与主轴马达所组成的,整个内部如同下图所']
        # for word in words:
        #     print(word)
        word = "\n".join(words)
        self.textEdit_ocr_result.insertPlainText(word)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Form_PDF_Tools()
    form.show()
    sys.exit(app.exec_())
