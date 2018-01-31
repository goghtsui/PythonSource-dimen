#!/usr/bin/env python
# -*- coding:utf-8 -*-


from src import Content
from src import Constants
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMessageBox


class Menu:
    def __init__(self, window_bar):
        self.window = window_bar
        self.menubar = window_bar.menuBar()
        self.content = Content.Content()

    def addMenu(self):
        # menu = self.menubar.addMenu(self.content.menu_file())
        # menu.addAction(QAction(QIcon(Constants.ICON_ANDROID), "保存", self.menubar, triggered=lambda: QMessageBox.about(self.window, '关闭', '关闭。。。')))
        menu = self.menubar.addMenu(self.content.menu_option())
        menu.addAction(QAction(QIcon(Constants.ICON_PENCIL), "1 * 1 * 160", self.menubar, triggered=self.men_fill_one))
        menu.addAction(
            QAction(QIcon(Constants.ICON_PENCIL), "1.5 * 1.5 * 240", self.menubar, triggered=self.men_fill_second))
        menu.addAction(
            QAction(QIcon(Constants.ICON_PENCIL), "2 * 2 * 320", self.menubar, triggered=self.men_fill_third))

        menu = self.menubar.addMenu(self.content.menu_language())
        menu.addAction(QAction(QIcon(Constants.ICON_LANG), self.content.menu_language_change(), self.menubar,
                               triggered=self.switch_lang))

        menu = self.menubar.addMenu(self.content.menu_help())
        menu.addAction(QAction(QIcon(Constants.ICON_BOOK), self.content.menu_help_instruc(), self.menubar,
                               triggered=lambda: QMessageBox.about(self.window, self.content.menu_help_instruc(),
                                                                   Constants.INSTRUCTIONS)))

        menu = self.menubar.addMenu(self.content.menu_about())
        menu.addAction(QAction(QIcon(Constants.ICON_BOY), self.content.menu_about_author(), self.menubar,
                               triggered=lambda: QMessageBox.about(self.window, self.content.menu_about_author(),
                                                                   Constants.AUTHOR)))

    def men_fill_one(self):
        self.window.density_edit.setText('1')
        self.window.scale_density_edit.setText('1')
        self.window.xdpi_edit.setText('160')

    def men_fill_second(self):
        self.window.density_edit.setText('1.5')
        self.window.scale_density_edit.setText('1.5')
        self.window.xdpi_edit.setText('240')

    def men_fill_third(self):
        self.window.density_edit.setText('2')
        self.window.scale_density_edit.setText('2')
        self.window.xdpi_edit.setText('320')

    def switch_lang(self):
        if Constants.LANGUAGE == 0:
            Constants.LANGUAGE = 1
        else:
            Constants.LANGUAGE = 0

        # 修改窗口标题
        self.window.setWindowTitle(self.content.get_window_title())
        self.window.lable_subtitle.setText(self.content.get_sub_title())
        # 修改菜单
        self.menubar.clear()
        self.addMenu()
        # 修改输入选项文字
        self.window.label_file_path.setText(self.content.get_lable_file_path())
        self.window.label_debug_info.setText(self.content.get_lable_debug_info())
        self.window.select_button.setText(self.content.get_button_browse())
        self.window.convert_button.setText(self.content.get_button_convert())
