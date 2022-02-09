import sys
from PyQt5.QtWidgets import *


class WidgetDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label()

    def label(self):

        button1 = QPushButton('按钮1', self)
        button1.setCheckable(True)
        button1.clicked.connect(self.btn_checked)
        label1 = QLabel('标签1')
        label1.setText('sdlfklak')
        label2 = QLabel('标签2')


        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(button1)
        self.resize(300, 500)
        self.setLayout(vbox)

    def button(self):
        pass

    def btn_checked(self):
        self.label1.setText('hahah')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WidgetDemo()
    w.show()
    sys.exit(app.exec_())