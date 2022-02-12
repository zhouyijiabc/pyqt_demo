import shutdown
# import table_handle
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
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

        self.window.shutdown_timeEdit.timeChanged.connect(self.get_shutdown_time)  # 获取关机时间
        self.window.create_plan_pushButton.clicked.connect(self.create_shutdown)  # 创建关机计划
        self.window.cancel_pushButton.clicked.connect(self.cancel_shutdown)  # 取消关机计划
        self.window.shutdown_now_pushButton.clicked.connect(self.shutdown_now)  # 立即关机

        self.window.get_wechat_path_pushButton.clicked.connect(self.get_wechat_path)  # 获取微信路径
        self.window.start_wechat_pushButton.clicked.connect(self.open_wechat)  # 开启微信

        self.marge_path = os.getcwd()
        self.window.marge_path_lineEdit.setText(self.marge_path)
        self.window.custom_path_radioButton.clicked.connect(self.open_get_marge_btu)  # 开启自定义路径按钮
        self.window.default_path_radioButton.clicked.connect(self.close_get_marge_btu)  # 关闭自定义路径按钮
        self.window.get_marge_path_pushButton.clicked.connect(self.get_marge_path)  # 获取合并文件夹路径
        self.window.marge_pushButton.clicked.connect(self.marge_file) # 合并文件

        self.window.lock_now_pushButton.clicked.connect(self.lock_window)

        self.marge_path = self.window.marge_path_lineEdit.text()

        self.apply_stylesheet = apply_stylesheet(self.app, theme='dark_teal.xml')
        self.main.show()
        sys.exit(self.app.exec_())

    def get_shutdown_time(self):
        self.set_time = self.window.shutdown_timeEdit.time().toPyTime()
        self.window.textBrowser.append(f'关机时间：{self.set_time}')

    def create_shutdown(self):
        if self.window.cycle_radioButton.isChecked():
            res_text = shutdown.shutdown(set_time=str(self.set_time), is_everyday=True)
            self.window.statusbar.showMessage(res_text, 5000)
            self.window.textBrowser.append(f'已创建关机计划  shutdown_every  每日关机时间为：{self.set_time}')
            self.window.textBrowser.append('如需取消请点击： 取消关机')
        else:
            res_text = shutdown.shutdown(set_time=str(self.set_time))
            self.window.statusbar.showMessage(res_text, 5000)
            self.window.textBrowser.append(f'已设置自动关机  时间为：{self.set_time}')
            self.window.textBrowser.append('如需取消请点击： 取消关机')

    def shutdown_now(self):
        command = 'shutdown -s -t 30'
        os.system(command)
        self.window.statusbar.showMessage('30秒后关机，如需取消请点击取消关机', 5000)
        self.window.textBrowser.append('30秒后关机，如需取消请点击： 取消关机')

    def cancel_shutdown(self):
        res_text = shutdown.stop_shutdown()
        self.window.statusbar.showMessage(res_text, 5000)
        self.window.textBrowser.append('已取消 自动关机')

    def lock_window(self):
        command = 'rundll32.exe user32.dll LockWorkStation'
        os.system(command)

    def get_wechat_path(self):
        path = QFileDialog.getOpenFileName(None, '请选择微信执行文件')
        print(path[0])
        self.window.wechat_lineEdit.setText(path[0])

    def open_wechat(self):
        num = self.window.open_num_spinBox.value()
        wechat_path = self.window.wechat_lineEdit.text()
        if ' ' in wechat_path:
            wechat_path = wechat_path[:wechat_path.find(' ')].replace('/', '/"') + wechat_path[
                                                                                   wechat_path.find(' '):].replace('/',
                                                                                                                   '"/',
                                                                                                                   1)
        print(num, type(num), wechat_path)
        command = 'start {}'.format(wechat_path)
        print(command)
        for i in range(num):
            os.system(command)

    def open_get_marge_btu(self):
        self.window.get_marge_path_pushButton.setEnabled(True)

    def close_get_marge_btu(self):
        self.window.get_marge_path_pushButton.setEnabled(False)
        self.marge_path = os.getcwd()
        self.window.marge_path_lineEdit.setText(self.marge_path)
        self.window.statusbar.showMessage(f'当前合并目录为   {self.marge_path}', 5000)

    def get_marge_path(self):
        self.marge_path = QFileDialog.getExistingDirectory(None, '请选择合并路径')
        self.window.marge_path_lineEdit.setText(self.marge_path)
        print(self.marge_path)
        self.window.statusbar.showMessage(f'设置合并目录为   {self.marge_path}', 5000)
        self.window.textBrowser.append(f'设置合并目录为   {self.marge_path}')

    def marge_file(self):
        print(self.marge_path, type(self.marge_path))
        marge = table_handle.TableHandle(file_path=self.marge_path, save_name=self.marge_path +'/margenew.xlsx')
        marge.marge_table()
        self.window.textBrowser.append(f'合并目录:   {self.marge_path}')
        self.window.textBrowser.append('合并文件名:  margenew.xlsx')


if __name__ == '__main__':
    run = Run()
    run()