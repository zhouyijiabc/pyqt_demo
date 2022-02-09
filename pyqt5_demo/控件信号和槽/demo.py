import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('demo')
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self):
        self.QObject_test()
        self.check_box_test()
        self.label_test()
        self.push_button_test()

    def label_test(self):
        label_str = 'ceshi'
        test_label = QLabel(label_str, self)
        test_label.setToolTip('这是一个提示框')

    def push_button_test(self):
        push_button = QPushButton('测试按钮', self)
        push_button.setCheckable(True)
        push_button.clicked[bool].connect(self.push_button_func)

    def push_button_func(self, pressed):
        source = self.sender()
        print(source.text())
        print(pressed)
        if pressed:
            self.setWindowTitle('button_checked')
        else:
            self.setWindowTitle('button_no_check')

    def check_box_test(self):
        check_box = QCheckBox('测试', self)
        check_box.move(50, 50)
        check_box.toggle()
        check_box.stateChanged.connect(self.change_title)

    def change_title(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('is_checked')

        else:
            self.setWindowTitle('is_not_checked')

    def QObject_test(self):
        # 测试api
        pass
        # obj = QObject()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())




