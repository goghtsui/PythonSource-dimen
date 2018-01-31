#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from src import Menu
from src import Content
from src import Transfer
from src import Constants
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
import ctypes

try:
    temp1 = ctypes.windll.LoadLibrary('../DLL/api-ms-win-crt-runtime-l1-1-0.dll')
except:
    pass

qtCreatorFile = "launcher.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class PyQtApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # 设置窗口图标
        self.setWindowIcon(QIcon(Constants.ICON_ANDROID))
        self.menu_bar = Menu.Menu(self)
        self.menu_bar.addMenu()
        self.select_button.clicked.connect(self.selectFile)
        self.convert_button.clicked.connect(self.converter)
        self.content = Content.Content()

    def converter(self):
        self.output_log(self.content.seprate())
        if self.density_edit.toPlainText() and self.scale_density_edit.toPlainText() and self.xdpi_edit.toPlainText() and self.file_path_edit.toPlainText():
            Transfer.Transfer(float(self.density_edit.toPlainText()), float(self.scale_density_edit.toPlainText()),
                              float(self.xdpi_edit.toPlainText()), str(self.file_path_edit.toPlainText())).generator(
                self.output_log)
        else:
            self.output_log(self.content.param_error())

    def selectFile(self):
        """   select xml file """
        file_name, file_type = QFileDialog.getOpenFileName(self, Constants.dialog_title, Constants.dialog_init_path,
                                                           Constants.dialog_file_type)
        self.output_log(self.content.output_file_path() % file_name)
        self.file_path_edit.append(file_name)

    def output_log(self, log_info):
        """  output info to consle  """
        if log_info:
            self.output_edit.append('\n' + log_info)
            # print('\n' + log_info)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PyQtApp()
    window.show()
    sys.exit(app.exec_())
