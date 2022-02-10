import shutdown
from PyQt5.QtWidgets import *
import sys
import os
from qt_material import apply_stylesheet
from tool_box_ui import Ui_mainWindow


class Run:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main = QMainWindow()
        self.window = Ui_mainWindow()
        self.window.setupUi(self.main)
        self.set_time = str(self.window.shutdown_timeEdit.time().toPyTime())
        print(self.set_time)

        self.window.shutdown_timeEdit.timeChanged.connect(self.get_shutdown_time)
        self.window.create_plan_pushButton.clicked.connect(self.create_shutdown)
        self.window.cancel_pushButton.clicked.connect(self.cancel_shutdown)

        self.window.get_wechat_path_pushButton.clicked.connect(self.get_wechat_path)

        self.apply_stylesheet = apply_stylesheet(self.app, theme='dark_teal.xml')
        self.main.show()
        sys.exit(self.app.exec_())

    def get_shutdown_time(self):
        self.set_time = self.window.shutdown_timeEdit.time().toPyTime()
        print(self.set_time)
        print(type(self.set_time))

    def create_shutdown(self):
        if self.window.cycle_radioButton.isChecked():
            res_text = shutdown.shutdown(set_time=str(self.set_time), is_everyday=True)
            self.window.statusbar.showMessage(res_text, 5000)
        else:
            res_text = shutdown.shutdown(set_time=str(self.set_time))
            self.window.statusbar.showMessage(res_text, 5000)

    def cancel_shutdown(self):
        res_text = shutdown.stop_shutdown()
        self.window.statusbar.showMessage(res_text, 5000)

    def get_wechat_path(self):
        path = QFileDialog.getOpenFileName(None, '请选择微信执行文件')
        print(path[0])
        self.window.wechat_lineEdit.setText(path[0])


if __name__ == '__main__':
    run = Run()
    run
