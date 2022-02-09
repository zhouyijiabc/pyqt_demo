"""
PyQt是英国的Riverbank Computing公司开发的一套封装QT程序库的Python GUI库，由一系列Python模块组成。
包含了超过620个类、6000个函数和方法，能在很多流行的操作系统(UNIX、Linux、Windows、Mac OS等)上运行。

PyQt5 类分为很多模块，主要模块有:

    QtCore: 包含了核心的非GUI的功能。这些功能主要与时间、文件、文件夹、各种数据、流、URLs、mime类文件、进程和线程有关。

    QtGui: 包含了窗口系统、事件处理、2D图像、基本绘画、字体和文字类。

    QtWidgets: 包含了一系列创建桌面应用的UI元素。

    QtMultimedia: 包含了处理多媒体的内容和调用摄像头API的类。

    QtBluetooth: 包含了查找和连接蓝牙的类。

    QtNetwork: 包含了网络编程的类，这些工具能让TCP/IP和UDP开发变得更加方便和可靠。

    QtPositioning: 包含了定位的类，可以使用卫星、WiFi等进行定位。

    QtWebSockets: 包含了WebSocket 协议的类。

    QtWebKit: 包含了一个基于WebKit2的Web浏览器。

    QtWebKitWidgets: 包含了基于QtWidgets的WebKit1的类。

    QtXml: 包含了处理XML的类，提供了SAX和DOMAPI的工具。

    QtSvg: 提供了显示SVG内容的类，Scalable Vector Graphics (SVG)是一种基于可扩展标记语言(XML)，用于描述二维矢量图形的图形格式。

    QtSql: 提供了处理数据库的工具。

    QtTest: 提供了测试PyQt5应用的工具。


PyQt5 支持如下三种布局：绝对布局、盒布局、网格布局

"""
import sys

from PyQt5.QtWidgets import (QWidget,
                             QApplication,

                             QHBoxLayout,  # 水平布局
                             QVBoxLayout,  # 垂直布局
                             QGridLayout,  # 网格布局
                             QGroupBox, # 组布局

                             QLabel,  # 标签
                             QPushButton,  # 按钮
                             QRadioButton,  # 单选按钮
                             QCheckBox,  # 多选按钮
                             QLineEdit,  # 单行文本编辑
                             QTextEdit,  # 多行文本编辑
                             )


class layout_test(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.box_layout()
        self.grid_layout()

    def box_layout(self):
        ok_button = QPushButton('确定')  # 1. 创建控件
        cancel_button = QPushButton('取消')

        hbox = QHBoxLayout()  # 2.设置水平布局

        hbox.addStretch()  # 占位

        hbox.addWidget(ok_button)  # 3.将控件添加到水平布局里
        hbox.addWidget(cancel_button)

        vbox = QVBoxLayout()
        vbox.addStretch()  # 占位

        vbox.addLayout(hbox)  # 4.将水平布局添加到垂直布局里

        self.setGeometry(300, 300, 300, 150)
        self.setLayout(vbox)  # 5.将整体布局设置为水平布局

    def grid_layout(self):
        title = QLabel('标题')
        author = QLabel('作者')
        summary = QLabel('摘要')

        title_edit = QLineEdit()
        author_edit = QLineEdit()
        summary_edit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)  # 控件之间的空白距离

        grid.addWidget(title, 1, 0)
        grid.addWidget(title_edit, 1, 1)
        grid.addWidget(author, 2, 0)
        grid.addWidget(author_edit, 2, 1)
        grid.addWidget(summary, 3, 0)
        # summary_edit 控件 位于第4行第2列，占用5行1列
        grid.addWidget(summary_edit, 3, 1, 5, 1)

        self.setGeometry(300, 300, 300, 300)  # 设置 x,y,w,h

        self.setLayout(grid)


class WidgetTest(QWidget):
    def __init__(self):
        super().__init__()
        self.is_hide = False
        self.initUI()

    def initUI(self):
        self.layout()
        self.push_button()

    def push_button(self):
        """
        QPushButton是一个按钮控件，
        不过这个按钮控件支持两种状态，一种是Normal状态，另外一种是Checked状态。
        Normal状态就是正常的未按下的状态，而Checked状态就是按钮被按下的状态，
        按下后颜色变为蓝色，表示已经被选中。

        :return:
        """
        button1 = QPushButton('按钮1')
        button1.setDefault(True)
        button1.clicked.connect(self.push_button_func)

        button2 = QPushButton('按钮2')
        button2.setCheckable(True)
        button2.clicked.connect(self.push_button_func)
        hide_button = QPushButton('不可用按钮')
        hide_button.setEnabled(self.is_hide)

        vbox = QVBoxLayout()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(hide_button)

        self.resize(300, 300)
        self.setLayout(vbox)


    def push_button_func(self, pressed):
        if self.sender() and self.sender().text() == '按钮1':
            print(self.sender().text())
            print('button1被按下')
        if pressed and self.sender().text() == '按钮1':
            print('按钮1被按下')
        elif pressed and self.sender().text() == '按钮2':
            print('按钮2被按下')
            self.is_hide = True

    def radio_button(self):
        radio_button1 = QRadioButton('单选1')
        radio_button2 = QRadioButton('单选2')


    def text_browser(self):
        text = QTextEdit()
        text.resize(80,30)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WidgetTest()
    ex.show()

    sys.exit(app.exec_())
