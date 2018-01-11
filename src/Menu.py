#!/usr/bin/env python

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp


class Menu:
    def __init__(self, window_bar):
        self.menubar = window_bar

    def addMenu(self):
        menu = self.menubar.addMenu("文件(F)")
        menu.addAction(QAction(QIcon("icon.png"), "保存", self.menubar, triggered=self.men_print))

    def men_print(self):
        print('menu_print')