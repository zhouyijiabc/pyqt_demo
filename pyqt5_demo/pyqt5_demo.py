# pyqt5 基本组件
from PyQt5.QtCore import QDateTime, QTimer, Qt  # 时间任务调度
from PyQt5.QtWidgets import (QApplication,  # 必需
                             QGridLayout,  # 网格布局
                             QHBoxLayout,  # 水平布局
                             QVBoxLayout,  # 垂直布局

                             QGroupBox,  # 分组容器
                             QTabWidget,  # 选项卡容器

                             QLabel,  # 标签
                             QCheckBox,  # 列表框
                             QRadioButton,  # 单选按钮
                             QComboBox,  # 下拉列表
                             QLineEdit,  # 单行文本
                             QTextEdit,  # 多行文本
                             QDialog,  #
                             QPushButton,  # 按钮
                             QSlider,  # 滑块
                             QScrollBar,  # 滚动条
                             QSpinBox,  #
                             QDateTimeEdit,  #
                             QTableWidget,  #
                             QProgressBar,  # 进度条
                             QDial,  # 旋钮
                             QWidget,  #
                             QStyleFactory,  # 样式
                             QSizePolicy  # 大小设置
                             )


# 第1步：设置组件
# 第2步：设置布局
# 第3步：将组件添加进布局
# 第4步：将布局添加进整体布局


class WidgetGallery(QDialog):
    def __init__(self, parent=None):  # 不继承父类
        # 设置自定义样式
        super(WidgetGallery, self).__init__(parent)
        self.originalPalette = QApplication.palette()  # 设置原生模板

        # 下拉列表
        style_combobox = QComboBox()
        style_combobox.addItems(QStyleFactory.keys())

        # 标签
        style_label = QLabel('样式')
        style_label.setBuddy(style_combobox)  # 设置标签对应的组件

        # 下拉列表选择不同的样式，进行更改
        style_combobox.activated[str].connect(self.chang_style)

        self.use_stander_checkbox = QCheckBox('使用标准样式')
        self.use_stander_checkbox.setChecked(True)
        self.use_stander_checkbox.toggled.connect(self.chang_palette)
        disable_widget_checkbox = QCheckBox('禁用组件')
        self.createTopLeftGroupBox()
        self.create_top_right_group_box()
        self.create_bottom_left_tabwidget()
        self.create_bottom_right_group_box()
        self.create_progressbar()

        # 顶端布局 水平布局
        top_layout = QHBoxLayout()  # 设置布局方式为水平布局
        top_layout.addWidget(style_label)  # 将组件添加进布局
        top_layout.addWidget(style_combobox)
        top_layout.addWidget(self.use_stander_checkbox)
        top_layout.addWidget(disable_widget_checkbox)
        main_layout = QGridLayout()  # 整体布局是网格布局
        main_layout.addLayout(top_layout, 0, 0, 1, 2)  # 将布局添加进整体布局里
        main_layout.addWidget(self.top_left_group, 1, 0)
        main_layout.addWidget(self.top_right_group, 1, 1)
        main_layout.addWidget(self.bottom_left_tabwidget, 2, 0)
        main_layout.addWidget(self.bottom_right_group, 2, 1)
        main_layout.addWidget(self.progressbar, 3, 0, 1, 2)
        self.setLayout(main_layout)  # 将布局添加进整体布局里
        self.setWindowTitle('基本组件')

    # 左上角：第一组基本组件
    def createTopLeftGroupBox(self):
        self.top_left_group = QGroupBox('第一组')
        radiobutton1 = QRadioButton('单选1')
        radiobutton1.setChecked(True)

        radiobutton2 = QRadioButton('单选2')
        radiobutton3 = QRadioButton('单选3')

        checkbox = QCheckBox('Tri-state checkbox')  # 多种状态的checkbox
        checkbox.setTristate(True)
        checkbox.setCheckState(Qt.PartiallyChecked)
        # 垂直布局
        layout = QVBoxLayout()
        layout.addWidget(radiobutton1)
        layout.addWidget(radiobutton2)
        layout.addWidget(radiobutton3)
        layout.addWidget(checkbox)
        self.top_left_group.setLayout(layout)

    # 右上角：第二组基本组件
    def create_top_right_group_box(self):
        self.top_right_group = QGroupBox('第二组')
        default_button = QPushButton('默认Button')
        default_button.setDefault(True)
        toggle_button = QPushButton('开关Button')
        toggle_button.setCheckable(True)
        toggle_button.setChecked(True)

        flat_button = QPushButton('FlatButton')
        flat_button.setFlat(True)

        layout = QVBoxLayout()
        layout.addWidget(default_button)
        layout.addWidget(toggle_button)
        layout.addWidget(flat_button)
        self.top_right_group.setLayout(layout)

    # 左下角 构建选项卡
    def create_bottom_left_tabwidget(self):
        self.bottom_left_tabwidget = QTabWidget()
        self.bottom_left_tabwidget.setSizePolicy(QSizePolicy.Preferred,
                                                 QSizePolicy.Ignored)

        # 标签
        tab1 = QWidget()
        table_widget = QTableWidget(10, 10)
        tab1hbox = QHBoxLayout()
        tab1hbox.addWidget(table_widget)
        tab1.setLayout(tab1hbox)

        tab2 = QWidget()
        textedit = QTextEdit()
        textedit.setPlainText('菩提本无数\n'
                              '明镜亦非台\n'
                              '本来无一物\n'
                              '何处惹尘埃')
        tab2hbox = QHBoxLayout()
        tab2hbox.addWidget(textedit)
        tab2.setLayout(tab2hbox)
        self.bottom_left_tabwidget.addTab(tab1, '表格')
        self.bottom_left_tabwidget.addTab(tab2, '文本')

    # 右下角 第三组
    def create_bottom_right_group_box(self):
        self.bottom_right_group = QGroupBox('第三组')

        linted = QLineEdit('str3')
        linted.setEchoMode(QLineEdit.Password)
        name_label = QLabel('密码')
        name_label.setBuddy(linted)

        spinbox = QSpinBox(self.bottom_right_group)
        spinbox.setValue(20)

        datetimeedit = QDateTimeEdit(self.bottom_right_group)
        datetimeedit.setDateTime(QDateTime.currentDateTime())

        slide = QSlider(Qt.Horizontal, self.bottom_right_group)
        slide.setValue(50)

        scrollbar = QScrollBar(Qt.Horizontal, self.bottom_right_group)
        scrollbar.setValue(40)

        dial = QDial(self.bottom_right_group)
        dial.setValue(20)
        dial.setNotchesVisible(True)

        layout = QGridLayout()
        layout.addWidget(linted, 0, 0, 1, 0)
        layout.addWidget(spinbox, 1, 0, 1, 2)
        layout.addWidget(datetimeedit, 2, 0, 1, 2)
        layout.addWidget(slide, 3, 0)
        layout.addWidget(scrollbar, 4, 0)
        layout.addWidget(dial, 3, 1, 2, 1)
        self.bottom_right_group.setLayout(layout)

    #  构建进度条
    def create_progressbar(self):
        self.progressbar = QProgressBar()
        self.progressbar.setRange(0, 1000)
        self.progressbar.setValue(0)

        timer = QTimer(self)
        timer.timeout.connect(self.advance_progressbar)  # qt事件处理机制
        timer.start(1000)

    def advance_progressbar(self):
        cur_val = self.progressbar.value()
        max_val = self.progressbar.maximum()
        self.progressbar.setValue(cur_val + (max_val - cur_val) / 100)

    # 改变模板
    def chang_palette(self):
        if self.use_stander_checkbox.isChecked():
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.originalPalette)

    # 改变样式
    def chang_style(self, style_name):
        QApplication.setStyle(QStyleFactory.create(style_name))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()  # 实例化
    gallery.show()
    sys.exit(app.exec_())  # 循环处理
