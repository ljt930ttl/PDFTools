# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tools.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form_PDF_Tools(object):
    def setupUi(self, Form_PDF_Tools):
        if not Form_PDF_Tools.objectName():
            Form_PDF_Tools.setObjectName(u"Form_PDF_Tools")
        Form_PDF_Tools.setWindowModality(Qt.WindowModal)
        Form_PDF_Tools.resize(813, 626)
        self.gridLayout_3 = QGridLayout(Form_PDF_Tools)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(2, 0, 2, 0)
        self.widget = QWidget(Form_PDF_Tools)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 2)
        self.textBrowser_log = QTextBrowser(self.widget)
        self.textBrowser_log.setObjectName(u"textBrowser_log")

        self.gridLayout_5.addWidget(self.textBrowser_log, 2, 0, 1, 1)

        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabsClosable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_6 = QGridLayout(self.tab)
        self.gridLayout_6.setSpacing(4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 2, 2, 2)
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_separate_destination = QLineEdit(self.groupBox)
        self.lineEdit_separate_destination.setObjectName(u"lineEdit_separate_destination")

        self.gridLayout_2.addWidget(self.lineEdit_separate_destination, 1, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_separate_source = QLineEdit(self.groupBox)
        self.lineEdit_separate_source.setObjectName(u"lineEdit_separate_source")

        self.gridLayout_2.addWidget(self.lineEdit_separate_source, 0, 1, 1, 1)

        self.pushButton_separate_destination = QPushButton(self.groupBox)
        self.pushButton_separate_destination.setObjectName(u"pushButton_separate_destination")

        self.gridLayout_2.addWidget(self.pushButton_separate_destination, 1, 2, 1, 1)

        self.pushButton_separate_source = QPushButton(self.groupBox)
        self.pushButton_separate_source.setObjectName(u"pushButton_separate_source")

        self.gridLayout_2.addWidget(self.pushButton_separate_source, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.pushButton_separate = QPushButton(self.groupBox)
        self.pushButton_separate.setObjectName(u"pushButton_separate")

        self.gridLayout_2.addWidget(self.pushButton_separate, 2, 2, 1, 1)

        self.lineEdit_separate_pattern = QLineEdit(self.groupBox)
        self.lineEdit_separate_pattern.setObjectName(u"lineEdit_separate_pattern")

        self.gridLayout_2.addWidget(self.lineEdit_separate_pattern, 2, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.textBrowser_2 = QTextBrowser(self.groupBox)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setMinimumSize(QSize(0, 120))
        self.textBrowser_2.setMaximumSize(QSize(16777215, 120))

        self.verticalLayout_2.addWidget(self.textBrowser_2)


        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.lineEdit_merge_source_dir = QLineEdit(self.groupBox_2)
        self.lineEdit_merge_source_dir.setObjectName(u"lineEdit_merge_source_dir")

        self.gridLayout.addWidget(self.lineEdit_merge_source_dir, 0, 1, 1, 1)

        self.pushButton_merge_source = QPushButton(self.groupBox_2)
        self.pushButton_merge_source.setObjectName(u"pushButton_merge_source")

        self.gridLayout.addWidget(self.pushButton_merge_source, 0, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.lineEdit_merge_save = QLineEdit(self.groupBox_2)
        self.lineEdit_merge_save.setObjectName(u"lineEdit_merge_save")

        self.gridLayout.addWidget(self.lineEdit_merge_save, 1, 1, 1, 1)

        self.pushButton_merge_save = QPushButton(self.groupBox_2)
        self.pushButton_merge_save.setObjectName(u"pushButton_merge_save")

        self.gridLayout.addWidget(self.pushButton_merge_save, 1, 2, 1, 1)

        self.pushButton_merge = QPushButton(self.groupBox_2)
        self.pushButton_merge.setObjectName(u"pushButton_merge")

        self.gridLayout.addWidget(self.pushButton_merge, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.textBrowser = QTextBrowser(self.groupBox_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout.addWidget(self.textBrowser)


        self.gridLayout_6.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_10 = QGridLayout(self.tab_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(4)
        self.gridLayout_10.setVerticalSpacing(5)
        self.gridLayout_10.setContentsMargins(2, 2, 2, 2)
        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.gridLayout_7 = QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_convert_image_source_file = QLineEdit(self.groupBox_3)
        self.lineEdit_convert_image_source_file.setObjectName(u"lineEdit_convert_image_source_file")

        self.gridLayout_4.addWidget(self.lineEdit_convert_image_source_file, 0, 1, 1, 1)

        self.lineEdit_convert_image_destination = QLineEdit(self.groupBox_3)
        self.lineEdit_convert_image_destination.setObjectName(u"lineEdit_convert_image_destination")

        self.gridLayout_4.addWidget(self.lineEdit_convert_image_destination, 2, 1, 1, 1)

        self.pushButton_convert_image_destination = QPushButton(self.groupBox_3)
        self.pushButton_convert_image_destination.setObjectName(u"pushButton_convert_image_destination")

        self.gridLayout_4.addWidget(self.pushButton_convert_image_destination, 2, 2, 1, 1)

        self.pushButton_convert_image = QPushButton(self.groupBox_3)
        self.pushButton_convert_image.setObjectName(u"pushButton_convert_image")

        self.gridLayout_4.addWidget(self.pushButton_convert_image, 3, 2, 1, 1)

        self.pushButton_convert_image_source_file = QPushButton(self.groupBox_3)
        self.pushButton_convert_image_source_file.setObjectName(u"pushButton_convert_image_source_file")

        self.gridLayout_4.addWidget(self.pushButton_convert_image_source_file, 0, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_12, 1, 0, 1, 1)

        self.pushButton_convert_image_source_dir = QPushButton(self.groupBox_3)
        self.pushButton_convert_image_source_dir.setObjectName(u"pushButton_convert_image_source_dir")

        self.gridLayout_4.addWidget(self.pushButton_convert_image_source_dir, 1, 2, 1, 1)

        self.lineEdit_convert_image_source_dir = QLineEdit(self.groupBox_3)
        self.lineEdit_convert_image_source_dir.setObjectName(u"lineEdit_convert_image_source_dir")

        self.gridLayout_4.addWidget(self.lineEdit_convert_image_source_dir, 1, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_8, 0, 3, 1, 1)

        self.lineEdit_convert_image_zoomX = QLineEdit(self.groupBox_3)
        self.lineEdit_convert_image_zoomX.setObjectName(u"lineEdit_convert_image_zoomX")

        self.gridLayout_4.addWidget(self.lineEdit_convert_image_zoomX, 0, 4, 1, 1)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_9, 1, 3, 1, 1)

        self.lineEdit_convert_image_zoomY = QLineEdit(self.groupBox_3)
        self.lineEdit_convert_image_zoomY.setObjectName(u"lineEdit_convert_image_zoomY")

        self.gridLayout_4.addWidget(self.lineEdit_convert_image_zoomY, 1, 4, 1, 1)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_10, 2, 3, 1, 1)

        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_11, 3, 3, 1, 1)

        self.lineEdit_convert_image_alpha = QLineEdit(self.groupBox_3)
        self.lineEdit_convert_image_alpha.setObjectName(u"lineEdit_convert_image_alpha")

        self.gridLayout_4.addWidget(self.lineEdit_convert_image_alpha, 2, 4, 1, 1)

        self.lineEdit_convert_image_rotate = QLineEdit(self.groupBox_3)
        self.lineEdit_convert_image_rotate.setObjectName(u"lineEdit_convert_image_rotate")

        self.gridLayout_4.addWidget(self.lineEdit_convert_image_rotate, 3, 4, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 3, 0, 1, 1)

        self.comboBox_convert_img_img_type = QComboBox(self.groupBox_3)
        self.comboBox_convert_img_img_type.addItem("")
        self.comboBox_convert_img_img_type.addItem("")
        self.comboBox_convert_img_img_type.addItem("")
        self.comboBox_convert_img_img_type.addItem("")
        self.comboBox_convert_img_img_type.setObjectName(u"comboBox_convert_img_img_type")

        self.gridLayout_4.addWidget(self.comboBox_convert_img_img_type, 3, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.textBrowser_3 = QTextBrowser(self.groupBox_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setMinimumSize(QSize(0, 100))
        self.textBrowser_3.setMaximumSize(QSize(16777215, 120))

        self.gridLayout_7.addWidget(self.textBrowser_3, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.gridLayout_8 = QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.lineEdit_convert_pdf_source = QLineEdit(self.groupBox_4)
        self.lineEdit_convert_pdf_source.setObjectName(u"lineEdit_convert_pdf_source")

        self.gridLayout_9.addWidget(self.lineEdit_convert_pdf_source, 0, 1, 1, 1)

        self.pushButton_convert_pdf = QPushButton(self.groupBox_4)
        self.pushButton_convert_pdf.setObjectName(u"pushButton_convert_pdf")

        self.gridLayout_9.addWidget(self.pushButton_convert_pdf, 2, 5, 1, 1)

        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_14, 0, 0, 1, 1)

        self.pushButton_convert_pdf_source = QPushButton(self.groupBox_4)
        self.pushButton_convert_pdf_source.setObjectName(u"pushButton_convert_pdf_source")

        self.gridLayout_9.addWidget(self.pushButton_convert_pdf_source, 0, 2, 1, 1)

        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_13, 1, 3, 1, 1)

        self.lineEdit_convert_pdf_destination_dir = QLineEdit(self.groupBox_4)
        self.lineEdit_convert_pdf_destination_dir.setObjectName(u"lineEdit_convert_pdf_destination_dir")

        self.gridLayout_9.addWidget(self.lineEdit_convert_pdf_destination_dir, 1, 4, 1, 1)

        self.pushButton_convert_pdf_destination = QPushButton(self.groupBox_4)
        self.pushButton_convert_pdf_destination.setObjectName(u"pushButton_convert_pdf_destination")

        self.gridLayout_9.addWidget(self.pushButton_convert_pdf_destination, 1, 5, 1, 1)

        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_9.addWidget(self.label_18, 0, 3, 1, 1)

        self.lineEdit_convert_pdf_source_dir = QLineEdit(self.groupBox_4)
        self.lineEdit_convert_pdf_source_dir.setObjectName(u"lineEdit_convert_pdf_source_dir")

        self.gridLayout_9.addWidget(self.lineEdit_convert_pdf_source_dir, 0, 4, 1, 1)

        self.pushButton_convert_pdf_source_dir = QPushButton(self.groupBox_4)
        self.pushButton_convert_pdf_source_dir.setObjectName(u"pushButton_convert_pdf_source_dir")

        self.gridLayout_9.addWidget(self.pushButton_convert_pdf_source_dir, 0, 5, 1, 1)

        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_15, 1, 0, 1, 1)

        self.lineEdit_convert_pdf_destination = QLineEdit(self.groupBox_4)
        self.lineEdit_convert_pdf_destination.setObjectName(u"lineEdit_convert_pdf_destination")

        self.gridLayout_9.addWidget(self.lineEdit_convert_pdf_destination, 1, 1, 1, 1)

        self.pushButton_convert_pdf_destination_file = QPushButton(self.groupBox_4)
        self.pushButton_convert_pdf_destination_file.setObjectName(u"pushButton_convert_pdf_destination_file")

        self.gridLayout_9.addWidget(self.pushButton_convert_pdf_destination_file, 1, 2, 1, 1)

        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_16, 2, 0, 1, 1)

        self.comboBox_convert_pdf_img_type = QComboBox(self.groupBox_4)
        self.comboBox_convert_pdf_img_type.addItem("")
        self.comboBox_convert_pdf_img_type.addItem("")
        self.comboBox_convert_pdf_img_type.addItem("")
        self.comboBox_convert_pdf_img_type.addItem("")
        self.comboBox_convert_pdf_img_type.setObjectName(u"comboBox_convert_pdf_img_type")

        self.gridLayout_9.addWidget(self.comboBox_convert_pdf_img_type, 2, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.textBrowser_4 = QTextBrowser(self.groupBox_4)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setMinimumSize(QSize(0, 80))
        self.textBrowser_4.setMaximumSize(QSize(16777215, 120))

        self.gridLayout_8.addWidget(self.textBrowser_4, 2, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_12 = QGridLayout(self.tab_3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pushButton_ocr_source = QPushButton(self.tab_3)
        self.pushButton_ocr_source.setObjectName(u"pushButton_ocr_source")

        self.gridLayout_11.addWidget(self.pushButton_ocr_source, 0, 5, 1, 1)

        self.label_20 = QLabel(self.tab_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_20, 0, 0, 1, 1)

        self.lineEdit_ocr_source = QLineEdit(self.tab_3)
        self.lineEdit_ocr_source.setObjectName(u"lineEdit_ocr_source")

        self.gridLayout_11.addWidget(self.lineEdit_ocr_source, 0, 1, 1, 4)

        self.label_22 = QLabel(self.tab_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_22, 3, 0, 1, 1)

        self.pushButton_baidu_ocr = QPushButton(self.tab_3)
        self.pushButton_baidu_ocr.setObjectName(u"pushButton_baidu_ocr")

        self.gridLayout_11.addWidget(self.pushButton_baidu_ocr, 3, 5, 1, 1)

        self.lineEdit_token = QLineEdit(self.tab_3)
        self.lineEdit_token.setObjectName(u"lineEdit_token")

        self.gridLayout_11.addWidget(self.lineEdit_token, 3, 1, 1, 4)

        self.lineEdit_baiduAPI_API_KEY = QLineEdit(self.tab_3)
        self.lineEdit_baiduAPI_API_KEY.setObjectName(u"lineEdit_baiduAPI_API_KEY")

        self.gridLayout_11.addWidget(self.lineEdit_baiduAPI_API_KEY, 1, 1, 2, 1)

        self.label_23 = QLabel(self.tab_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_23, 1, 0, 2, 1)

        self.lineEdit_baiduAPI_SECRET_KEY = QLineEdit(self.tab_3)
        self.lineEdit_baiduAPI_SECRET_KEY.setObjectName(u"lineEdit_baiduAPI_SECRET_KEY")

        self.gridLayout_11.addWidget(self.lineEdit_baiduAPI_SECRET_KEY, 1, 3, 2, 2)

        self.label_24 = QLabel(self.tab_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_24, 1, 2, 2, 1)

        self.pushButton_baidu_aip_token = QPushButton(self.tab_3)
        self.pushButton_baidu_aip_token.setObjectName(u"pushButton_baidu_aip_token")

        self.gridLayout_11.addWidget(self.pushButton_baidu_aip_token, 1, 5, 2, 1)


        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.textEdit_ocr_result = QTextEdit(self.tab_3)
        self.textEdit_ocr_result.setObjectName(u"textEdit_ocr_result")

        self.gridLayout_12.addWidget(self.textEdit_ocr_result, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_16 = QGridLayout(self.tab_4)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.groupBox_5 = QGroupBox(self.tab_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setEnabled(True)
        self.gridLayout_14 = QGridLayout(self.groupBox_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.lineEdit_proxy_port = QLineEdit(self.groupBox_5)
        self.lineEdit_proxy_port.setObjectName(u"lineEdit_proxy_port")

        self.gridLayout_13.addWidget(self.lineEdit_proxy_port, 3, 1, 1, 1)

        self.label_26 = QLabel(self.groupBox_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_26, 3, 0, 1, 1)

        self.label_28 = QLabel(self.groupBox_5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_28, 2, 2, 1, 1)

        self.lineEdit_porxy_ip = QLineEdit(self.groupBox_5)
        self.lineEdit_porxy_ip.setObjectName(u"lineEdit_porxy_ip")

        self.gridLayout_13.addWidget(self.lineEdit_porxy_ip, 2, 1, 1, 1)

        self.label_25 = QLabel(self.groupBox_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_25, 2, 0, 1, 1)

        self.lineEdit_proxy_list = QLineEdit(self.groupBox_5)
        self.lineEdit_proxy_list.setObjectName(u"lineEdit_proxy_list")

        self.gridLayout_13.addWidget(self.lineEdit_proxy_list, 6, 0, 1, 4)

        self.label_27 = QLabel(self.groupBox_5)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_13.addWidget(self.label_27, 4, 0, 1, 4)

        self.label_29 = QLabel(self.groupBox_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_29, 3, 2, 1, 1)

        self.lineEdit_proxy_password = QLineEdit(self.groupBox_5)
        self.lineEdit_proxy_password.setObjectName(u"lineEdit_proxy_password")

        self.gridLayout_13.addWidget(self.lineEdit_proxy_password, 3, 3, 1, 1)

        self.lineEdit_proxy_user = QLineEdit(self.groupBox_5)
        self.lineEdit_proxy_user.setObjectName(u"lineEdit_proxy_user")

        self.gridLayout_13.addWidget(self.lineEdit_proxy_user, 2, 3, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_5)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_13.addWidget(self.checkBox, 1, 0, 1, 2)

        self.checkBox_2 = QCheckBox(self.groupBox_5)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_13.addWidget(self.checkBox_2, 1, 2, 1, 2)


        self.gridLayout_14.addLayout(self.gridLayout_13, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.groupBox_5, 0, 0, 2, 2)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.pushButton_test = QPushButton(self.tab_4)
        self.pushButton_test.setObjectName(u"pushButton_test")
        self.pushButton_test.setEnabled(True)

        self.gridLayout_15.addWidget(self.pushButton_test, 0, 3, 1, 1)

        self.textEdit_test = QTextEdit(self.tab_4)
        self.textEdit_test.setObjectName(u"textEdit_test")
        self.textEdit_test.setEnabled(True)

        self.gridLayout_15.addWidget(self.textEdit_test, 0, 2, 2, 1)


        self.gridLayout_16.addLayout(self.gridLayout_15, 3, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 261, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_2, 2, 0, 1, 2)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout_5.addWidget(self.tabWidget, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form_PDF_Tools)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Form_PDF_Tools)
    # setupUi

    def retranslateUi(self, Form_PDF_Tools):
        Form_PDF_Tools.setWindowTitle(QCoreApplication.translate("Form_PDF_Tools", u"PDFTools V1.0", None))
        self.textBrowser_log.setHtml(QCoreApplication.translate("Form_PDF_Tools", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:2px; margin-bottom:2px; margin-left:2px; margin-right:2px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form_PDF_Tools", u"\u5206\u5272PDF", None))
        self.label.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u6e90\u6587\u4ef6:", None))
        self.pushButton_separate_destination.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u4fdd\u5b58\u76ee\u5f55", None))
        self.pushButton_separate_source.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u4fdd\u5b58\u76ee\u5f55:", None))
        self.pushButton_separate.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u5206\u5272", None))
        self.label_3.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u5206\u5272\u65b9\u5f0f:", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Form_PDF_Tools", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">1\uff1a\u5148\u9009\u62e9\u6e90\u6587\u4ef6\uff0c\u5373\u5b58\u9700\u8981\u5206\u5272\u7684PDF\u6587\u4ef6\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">2\uff1a\u9009\u62e9\u5408\u62fc\u540e\u9700\u8981\u5b58\u653e\u7684\u76ee\u5f55\uff0c\u9ed8\u8ba4\u4e3a\u6e90\u6587\u4ef6\u6240\u5728\u76ee\u5f55\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:"
                        "0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">3\uff1a\u5199\u5165\u5206\u5272\u7684\u65b9\u5f0f\uff0c</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">3.1\uff1a\u56fa\u5b9a\u95f4\u9694\u5206\u5272\uff0c\u5982\u5199\u516510\uff0c\u5219\u8868\u793a\u6bcf\u969410\u5206\u5272\u4e3a\u4e00\u4efd\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">3.2\uff1a\u6307\u5b9a\u9875\u7801\u5206\u5272\uff0c\u591a\u4e2a\u9875\u7801\u7531;\u9694\u5f00\uff0c\u59821-10;20-24;25-; \u5219\u8868\u793a1-10\u5206\u5272\u4e3a\u4e00\u4efd\uff1b20-24\u5206\u5272\u4e3a\u4e00\u4efd\uff0c25\u5230\u6700\u540e\u5206\u5272\u4e3a\u4e00\u4efd\uff1b</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form_PDF_Tools", u"\u5408\u5e76PDF", None))
        self.label_4.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u6e90\u76ee\u5f55:", None))
        self.pushButton_merge_source.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u9009\u62e9\u76ee\u5f55", None))
        self.label_5.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u4fdd\u5b58\u6587\u4ef6:", None))
        self.pushButton_merge_save.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u4fdd\u5b58\u6587\u4ef6", None))
        self.pushButton_merge.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u5408\u5e76", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form_PDF_Tools", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">1\uff1a\u5148\u9009\u62e9\u6e90\u6587\u4ef6\u76ee\u5f55\uff0c\u5373\u5b58\u653e\u4e86\u591a\u4e2a\u9700\u8981\u5408\u62fc\u7684PDF\u6587\u4ef6\u7684\u76ee\u5f55\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">2\uff1a\u9009\u62e9\u5408\u62fc\u540e\u9700\u8981\u5b58\u653e\u7684\u76ee\u5f55\uff0c\u9ed8\u8ba4\u4e3a\u6e90\u6587\u4ef6\u76ee\u5f55\uff1b</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form_PDF_Tools", u"PDF\u5206\u5272\u5408\u5e76", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form_PDF_Tools", u"PDF\u8f6c\u56fe\u7247", None))
        self.pushButton_convert_image_destination.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u4fdd\u5b58\u76ee\u5f55", None))
        self.pushButton_convert_image.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u8f6c\u6362", None))
        self.pushButton_convert_image_source_file.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_7.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u4fdd\u5b58\u76ee\u5f55:", None))
        self.label_6.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u6e90\u6587\u4ef6:", None))
        self.label_12.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u6e90\u76ee\u5f55:", None))
        self.pushButton_convert_image_source_dir.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u9009\u62e9\u76ee\u5f55", None))
        self.label_8.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u7f29\u653e\u6bd4\u4f8bX:", None))
        self.label_9.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u7f29\u653e\u6bd4\u4f8bY:", None))
        self.label_10.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u900f\u660e\u5ea6:", None))
        self.label_11.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u65cb\u8f6c\u89d2\u5ea6:", None))
        self.label_17.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u56fe\u7247\u683c\u5f0f:", None))
        self.comboBox_convert_img_img_type.setItemText(0, QCoreApplication.translate("Form_PDF_Tools", u"png", None))
        self.comboBox_convert_img_img_type.setItemText(1, QCoreApplication.translate("Form_PDF_Tools", u"jpg", None))
        self.comboBox_convert_img_img_type.setItemText(2, QCoreApplication.translate("Form_PDF_Tools", u"jpeg", None))
        self.comboBox_convert_img_img_type.setItemText(3, QCoreApplication.translate("Form_PDF_Tools", u"bmp", None))

        self.textBrowser_3.setHtml(QCoreApplication.translate("Form_PDF_Tools", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">1\uff1a\u9009\u62e9\u6e90\u6587\u4ef6\uff0c\u9700\u8981\u8f6c\u6362\u6210\u56fe\u7247\u7684pdf\u6587\u4ef6\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">1.1:\u9009\u62e9\u6e90\u76ee\u5f55\uff0c\u591a\u4e2apdf\u7684\u76ee\u5f55</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" f"
                        "ont-size:10pt; color:#ff0000;\">2\uff1a\u9009\u62e9\u4fdd\u5b58\u76ee\u5f55\uff0c\u4fdd\u5b58\u56fe\u7247\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">3\uff1a\u9009\u62e9\u9700\u8981\u8f6c\u6362\u7684\u56fe\u7247\u683c\u5f0f\uff0c</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">4:\u586b\u5199\u8f6c\u6362\u53c2\u6570\uff0c\u4e0d\u586b\u5219\u4e3a\u9ed8\u8ba4\u503c</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">  \u65cb\u8f6c\u89d2\u5ea6(\u8303\u56f40-360)\uff0c\u7f29\u653e\u6bd4\u4f8bX :2.0,\u7f29\u653e\u6bd4\u4f8bY :2.0, \u900f\u660e\u5ea60(\u8303\u56f40-100)\uff1b</span></p></body></html>", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form_PDF_Tools", u"\u56fe\u7247\u8f6cPDF", None))
        self.pushButton_convert_pdf.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u8f6c\u6362", None))
        self.label_14.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u6e90\u6587\u4ef6:", None))
        self.pushButton_convert_pdf_source.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_13.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u4fdd\u5b58\u76ee\u5f55:", None))
        self.pushButton_convert_pdf_destination.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u4fdd\u5b58\u76ee\u5f55", None))
        self.label_18.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u6e90\u76ee\u5f55:", None))
        self.pushButton_convert_pdf_source_dir.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u9009\u62e9\u76ee\u5f55", None))
        self.label_15.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u4fdd\u5b58\u6587\u4ef6:", None))
        self.pushButton_convert_pdf_destination_file.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u4fdd\u5b58\u6587\u4ef6", None))
        self.label_16.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u56fe\u7247\u683c\u5f0f:", None))
        self.comboBox_convert_pdf_img_type.setItemText(0, QCoreApplication.translate("Form_PDF_Tools", u"png", None))
        self.comboBox_convert_pdf_img_type.setItemText(1, QCoreApplication.translate("Form_PDF_Tools", u"jpg", None))
        self.comboBox_convert_pdf_img_type.setItemText(2, QCoreApplication.translate("Form_PDF_Tools", u"jpeg", None))
        self.comboBox_convert_pdf_img_type.setItemText(3, QCoreApplication.translate("Form_PDF_Tools", u"bmp", None))

        self.textBrowser_4.setHtml(QCoreApplication.translate("Form_PDF_Tools", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">1\uff1a\u9009\u62e9\u6e90\u6587\u4ef6\uff0c\u9700\u8981\u8f6c\u6362\u6210pdf\u7684\u56fe\u7247\u6587\u4ef6\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">1.1:\u9009\u62e9\u6e90\u76ee\u5f55\uff0c\u591a\u4e2a\u56fe\u7247\u7684\u76ee\u5f55</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span s"
                        "tyle=\" font-size:10pt; color:#ff0000;\">2\uff1a\u9009\u62e9\u4fdd\u5b58\u6587\u4ef6\uff0c\u56fe\u7247\u8f6c\u6362\uff0c\u4fdd\u5b58\u6210\u5355\u4e2a\u56fe\u7247\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">2-1\uff1a\u9009\u62e9\u4fdd\u5b58\u76ee\u5f55\uff0c\u56fe\u7247\u4e00\u4e00\u8f6c\u6362\uff0c\u4fdd\u5b58\u6210\u591a\u4e2aPDF\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">3\uff1a\u9009\u62e9\u9700\u8981\u8f6c\u6362\u7684\u56fe\u7247\u683c\u5f0f\uff1b</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form_PDF_Tools", u"PDF\u56fe\u7247\u4e92\u8f6c", None))
        self.pushButton_ocr_source.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u9009\u62e9\u56fe\u7247", None))
        self.label_20.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u6e90\u6587\u4ef6:", None))
        self.label_22.setText(QCoreApplication.translate("Form_PDF_Tools", u"token:", None))
        self.pushButton_baidu_ocr.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u8bc6\u522b\u56fe\u7247\u6587\u5b57", None))
        self.lineEdit_token.setText(QCoreApplication.translate("Form_PDF_Tools", u"24.160d830cf8e26ceba1f42334bec139a5.2592000.1623220220.282335-20457265", None))
        self.lineEdit_baiduAPI_API_KEY.setText("")
        self.label_23.setText(QCoreApplication.translate("Form_PDF_Tools", u"API_KEY:", None))
        self.lineEdit_baiduAPI_SECRET_KEY.setText("")
        self.label_24.setText(QCoreApplication.translate("Form_PDF_Tools", u"SECRET_KEY:", None))
        self.pushButton_baidu_aip_token.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u83b7\u53d6token", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form_PDF_Tools", u"baiduOCR", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form_PDF_Tools", u"\u4ee3\u7406\u8bbe\u7f6e", None))
        self.lineEdit_proxy_port.setText("")
        self.label_26.setText(QCoreApplication.translate("Form_PDF_Tools", u"port:", None))
        self.label_28.setText(QCoreApplication.translate("Form_PDF_Tools", u"user:", None))
        self.lineEdit_porxy_ip.setText("")
        self.label_25.setText(QCoreApplication.translate("Form_PDF_Tools", u"ip:", None))
        self.lineEdit_proxy_list.setText(QCoreApplication.translate("Form_PDF_Tools", u"127.0.0.1;", None))
        self.label_27.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u8bf7\u52ff\u5bf9\u4e00\u4e0b\u5730\u5740\u6761\u76ee\u4f7f\u7528\u4ee3\u7406\u670d\u52a1\u5668\uff0c\u82e5\u6709\u591a\u4e2a\u6761\u76ee\uff0c\u8bf7\u4f7f\u7528\u82f1\u6587\u5206\u53f7(;)\u6765\u5206\u9694\u3002", None))
        self.label_29.setText(QCoreApplication.translate("Form_PDF_Tools", u"password:", None))
        self.checkBox.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u662f\u5426\u4f7f\u7528\u4ee3\u7406", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form_PDF_Tools", u"\u662f\u5426\u4f7f\u7528\u4ee3\u7406", None))
        self.pushButton_test.setText(QCoreApplication.translate("Form_PDF_Tools", u"Test", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form_PDF_Tools", u"\u9875", None))
    # retranslateUi

