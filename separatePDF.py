#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/16 12:26
# @Author : linjinting
# @Project : pdf_phtoto
# @File : splitPDF.py
# @Software: PyCharm

import os
from PyPDF2 import PdfFileWriter, PdfFileReader

class SeparatePDF(object):
    def __init__(self, logger=None):
        if not logger:
            import logging
            logger = logging.getLogger(__file__)
        self.m_Logger = logger

        self.m_pattern = None
        self.m_pattern_type = None
        self.pdf_input = None
        # self.pdf_output = None
        self.sum_page_count = 0

    def run(self, pattern, source_filename, output_path):
        ret = self.read_file(source_filename)
        if ret == -1:
            return

        self.handle_separate_pattern(pattern)
        self.handle_page_num(source_filename, output_path)

    def read_file(self, source_filename):
        try:
            fp_read_file = open(source_filename, 'rb')
        except Exception as e:
            self.m_Logger.error(e)
            return -1
        self.pdf_input = PdfFileReader(fp_read_file)  # 将要分割的PDF内容格式
        self.sum_page_count = self.pdf_input.getNumPages()

    def handle_separate_pattern(self, pattern):
        try:
            self.m_pattern = int(pattern)
            self.m_pattern_type = "space"
            self.m_Logger.info(self.m_pattern)
            # return number
        except:
            self.m_pattern = pattern.split(";")
            self.m_pattern_type = "assign"
            self.m_Logger.info(self.m_pattern)

    def handle_page_num(self,source_filename, out_path):
        if self.m_pattern_type == "space":
            self.merge_for_space(source_filename, out_path)
        elif self.m_pattern_type == "assign":
            self.merge_for_assign(source_filename, out_path)
        else:
            self.m_Logger.error("分割方式格式错误")

    def merge_for_space(self, source_filename, out_path):
        remainder_count = self.sum_page_count
        start_page = 1
        end_page = 0
        while remainder_count > 0:
            if self.m_pattern < remainder_count:
                end_page = self.m_pattern + end_page
            else:
                end_page = self.sum_page_count
            _filename = "%d-%d_%s" % (start_page, end_page, os.path.basename(source_filename))
            output_file_path = os.path.join(out_path, _filename)
            self.merger(output_file_path, start_page, end_page)
            start_page = 1 + end_page
            remainder_count = remainder_count - self.m_pattern

    def merge_for_assign(self, source_filename, out_path):
        try:
            for pattern in self.m_pattern:
                if not pattern:
                    return
                pages = pattern.split("-")
                if len(pages) == 0:
                    return
                elif len(pages) == 1:
                    pages[0] = int(pages[0])
                    pages.append(-1)
                elif len(pages) == 2:
                    pages[0] = int(pages[0])
                    if not pages[1]:
                        pages[1] = -1
                    else:
                        pages[1] = int(pages[1])
                else:
                    self.m_Logger.error("分割方式格式错误")
                    return
                _filename = "%d-%d_%s" % (pages[0], pages[1], os.path.basename(source_filename))
                output_file_path = os.path.join(out_path, _filename)
                self.merger(output_file_path, pages[0], pages[1])
        except Exception as e:
            self.m_Logger.error("分割方式格式错误%s" % e)

    def merger(self, out_file, start_page, end_page):
        pdf_output = PdfFileWriter()  # 实例一个 PDF文件编写器
        start_page = start_page - 1
        if end_page > self.sum_page_count or end_page == 0:
            end_page = self.sum_page_count
        for i in range(start_page, end_page):
            pdf_output.addPage(self.pdf_input.getPage(i))
        try:
            with open(out_file, 'wb') as sub_fp:
                pdf_output.write(sub_fp)
        except Exception as e:
            print(type(e))
            self.m_Logger.error("open %s error:%s" %(out_file, e))

        del pdf_output
        self.m_Logger.info(f'完成分割{start_page +1}页-{end_page}页，保存为{out_file}!')
