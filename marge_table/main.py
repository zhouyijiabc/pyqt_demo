from PyQt5.QtWidgets import *
from marge import Ui_MainWindow
import sys
import os
import table_handle
from qt_material import apply_stylesheet


"""

['dark_amber.xml',
 'dark_blue.xml',
 'dark_cyan.xml',
 'dark_lightgreen.xml',
 'dark_pink.xml',
 'dark_purple.xml',
 'dark_red.xml',
 'dark_teal.xml',
 'dark_yellow.xml',
 'light_amber.xml',
 'light_blue.xml',
 'light_cyan.xml',
 'light_cyan_500.xml',
 'light_lightgreen.xml',
 'light_pink.xml',
 'light_purple.xml',
 'light_red.xml',
 'light_teal.xml',
 'light_yellow.xml']



"""


class signal:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main = QMainWindow()
        self.w = Ui_MainWindow()
        self.w.setupUi(self.main)
        self.w.default_path_radion.clicked.connect(self.hide_btu2)
        self.marge_path = os.getcwd()
        self.w.textBrowser.setText(f'当前合并目录：  {self.marge_path}')
        self.w.statusbar.showMessage(self.marge_path, 3000)

        self.w.custom_btu.clicked.connect(self.change_path_btu)

        self.w.custom_path_radion.clicked.connect(self.open_custom_path)

        self.w.is_sort_checkbox.clicked.connect(self.open_sort)

        self.w.marg_btu.clicked.connect(self.marge_file)

        self.apply_stylesheet = apply_stylesheet(self.app, theme='dark_teal.xml')
        self.main.show()
        sys.exit(self.app.exec_())

    def change_path_btu(self):
        self.w.textBrowser.append('请点击  自定义文件夹按钮  选择合并文件目录')
        path = QFileDialog.getExistingDirectory(None, '选择合并文件夹')
        print(path)

        self.w.textBrowser.append(f'当前合并目录：  {path}')
        self.marge_path = path

    def hide_btu2(self):

        self.w.custom_btu.setEnabled(False)

    def open_custom_path(self):
        self.w.custom_btu.setEnabled(True)
        self.w.textBrowser.append('请选择自定义文件夹')

    def open_sort(self):
        if self.w.is_sort_checkbox.isChecked():
            self.w.sort_label.setEnabled(True)
            self.w.col_names.setEnabled(True)
            self.w.textBrowser.append('开启排序请选择排序列名')
        else:
            self.w.sort_label.setEnabled(False)
            self.w.col_names.setEnabled(False)
            self.w.textBrowser.append('关闭排序')

    def marge_file(self):
        path = self.marge_path
        file_name = 'marge1.xlsx'
        a = table_handle.TableHandle(file_path=path, save_name=file_name)
        a.marge_table()


if __name__ == '__main__':
    l = signal()
    l
