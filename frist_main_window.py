from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon
import sys

# 主窗口类型
# QMainWindow: 包含菜单栏，工具栏，状态栏，标题栏，是最常见的窗口形式
# QDialog：是对话窗口的基类
# QWidget：不确定窗口用途就用这个


class FirstMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWindow, self).__init__(parent)

        self.setWindowTitle('第一个主窗口应用')
        self.resize(800, 600)
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('q5.png'))
    main = FirstMainWindow()
    main.show()
    sys.exit(app.exec_())

