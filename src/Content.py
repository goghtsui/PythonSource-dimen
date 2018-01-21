#!/usr/bin/env python

import Constants


class Content:
    def __init__(self):
        self.lang = Constants.LANGUAGE

    def get_window_title(self):
        if Constants.LANGUAGE == 0:
            return 'Dimens Adapter 4.1'
        else:
            return 'Dimens 适配器 4.1'

    def get_sub_title(self):
        if Constants.LANGUAGE == 0:
            return 'Dimens Adapter'
        else:
            return 'Dimens 适配器'

    def start_convert_data(self):
        if Constants.LANGUAGE == 0:
            return '>> Start to convert the data...'
        else:
            return '>> 开始转换数据...'

    def seprate(self):
        if Constants.LANGUAGE == 0:
            return '========================='
        else:
            return '========华丽分割=========='

    def param_error(self):
        if Constants.LANGUAGE == 0:
            return 'Please enter the correct information.'
        else:
            return '请输入正确的配置参数'

    def output_file_path(self):
        if Constants.LANGUAGE == 0:
            return 'Select file path %s '
        else:
            return '目标文件地址：%s '

    def start_parse_param(self):
        if Constants.LANGUAGE == 0:
            return '>> Start to parse parameters...'
        else:
            return '开始解析配置参数'

    def load_dimen_file(self):
        if Constants.LANGUAGE == 0:
            return '>> Loading the xml file : %s '
        else:
            return '正在加载文件 : %s '

    def load_success(self):
        if Constants.LANGUAGE == 0:
            return '>> File read successfully..'
        else:
            return '文件读取成功'

    def generate_data(self):
        if Constants.LANGUAGE == 0:
            return '>> Start to generate the target xml data...'
        else:
            return '开始生成目标配置数据'

    def generate_file(self):
        if Constants.LANGUAGE == 0:
            return '>> Start to generate the target xml file...'
        else:
            return '正在创建目标文件...'

    def start_write_date(self):
        if Constants.LANGUAGE == 0:
            return '>> Start to write data to target xml file...'
        else:
            return '正在写数据，请稍后...'

    def convert_success(self):
        if Constants.LANGUAGE == 0:
            return '>> Write successfully...'
        else:
            return '数据转换完成...'

    def new_file_path(self):
        if Constants.LANGUAGE == 0:
            return '>> Target File Path: %s '
        else:
            return '转换文件：%s '

    def get_lable_file_path(self):
        if Constants.LANGUAGE == 0:
            return 'file path'
        else:
            return '文件地址'

    def get_lable_debug_info(self):
        if Constants.LANGUAGE == 0:
            return 'debug info'
        else:
            return '调试信息'

    def get_button_browse(self):
        if Constants.LANGUAGE == 0:
            return 'browser'
        else:
            return '浏览...'

    def get_button_convert(self):
        if Constants.LANGUAGE == 0:
            return '  start  '
        else:
            return '开始转换'

    def menu_file(self):
        if Constants.LANGUAGE == 0:
            return 'File'
        else:
            return '文件'

    def menu_option(self):
        if Constants.LANGUAGE == 0:
            return 'Options'
        else:
            return '选项'

    def menu_language(self):
        if Constants.LANGUAGE == 0:
            return 'Language'
        else:
            return '语言'

    def menu_help(self):
        if Constants.LANGUAGE == 0:
            return 'Help'
        else:
            return '帮助'

    def menu_about(self):
        if Constants.LANGUAGE == 0:
            return 'About'
        else:
            return '关于'

    def menu_language_change(self):
        if Constants.LANGUAGE == 0:
            return 'Chinese'
        else:
            return 'English'

    def menu_help_instruc(self):
        if Constants.LANGUAGE == 0:
            return 'Instructions'
        else:
            return '使用说明'

    def menu_about_author(self):
        if Constants.LANGUAGE == 0:
            return 'Author'
        else:
            return '作者'
