#!/usr/bin/env python

import sys
import Menu
import Creator
import Transfer
import Constants
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog

qtCreatorFile = "launcher.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class PyQtApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.menu_bar = Menu.Menu(self.menuBar())
        self.menu_bar.addMenu()
        self.select_button.clicked.connect(self.selectFile)
        self.convert_button.clicked.connect(self.converter)

    def converter(self):
        self.output_log('=======seprator========.')
        if self.density_edit.toPlainText() and self.scale_density_edit.toPlainText() and self.xdpi_edit.toPlainText() and self.file_path_edit.toPlainText():
            Transfer.Transfer(float(self.density_edit.toPlainText()), float(self.scale_density_edit.toPlainText()),
                              float(self.xdpi_edit.toPlainText()), str(self.file_path_edit.toPlainText())).generator(self.output_log)
        else:
            self.output_log('Please enter the correct information.')

    def selectFile(self):
        """   select xml file """
        file_name, file_type = QFileDialog.getOpenFileName(self, Constants.dialog_title, Constants.dialog_init_path, Constants.dialog_file_type)
        self.output_log('Select file path %s ' % file_name)
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
