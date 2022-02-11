# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tool_box_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(892, 811)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setToolTip("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.wechat_lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.wechat_lineEdit.setObjectName("wechat_lineEdit")
        self.horizontalLayout_2.addWidget(self.wechat_lineEdit)
        self.get_wechat_path_pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.get_wechat_path_pushButton.setObjectName("get_wechat_path_pushButton")
        self.horizontalLayout_2.addWidget(self.get_wechat_path_pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.open_num_spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.open_num_spinBox.setProperty("value", 2)
        self.open_num_spinBox.setObjectName("open_num_spinBox")
        self.horizontalLayout_2.addWidget(self.open_num_spinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.start_wechat_pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.start_wechat_pushButton.setObjectName("start_wechat_pushButton")
        self.horizontalLayout_2.addWidget(self.start_wechat_pushButton)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(5, 1)
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cycle_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.cycle_radioButton.setObjectName("cycle_radioButton")
        self.gridLayout_2.addWidget(self.cycle_radioButton, 0, 6, 1, 1)
        self.once_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.once_radioButton.setChecked(True)
        self.once_radioButton.setObjectName("once_radioButton")
        self.gridLayout_2.addWidget(self.once_radioButton, 0, 5, 1, 1)
        self.create_plan_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.create_plan_pushButton.setObjectName("create_plan_pushButton")
        self.gridLayout_2.addWidget(self.create_plan_pushButton, 0, 2, 1, 1)
        self.shutdown_timeEdit = QtWidgets.QTimeEdit(self.groupBox)
        self.shutdown_timeEdit.setMaximumDate(QtCore.QDate(2000, 1, 1))
        self.shutdown_timeEdit.setTime(QtCore.QTime(16, 59, 0))
        self.shutdown_timeEdit.setObjectName("shutdown_timeEdit")
        self.gridLayout_2.addWidget(self.shutdown_timeEdit, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(98, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.cancel_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.gridLayout_2.addWidget(self.cancel_pushButton, 0, 7, 1, 1)
        self.shutdown_now_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.shutdown_now_pushButton.setObjectName("shutdown_now_pushButton")
        self.gridLayout_2.addWidget(self.shutdown_now_pushButton, 0, 4, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_4.addWidget(self.textBrowser)
        self.gridLayout.addWidget(self.groupBox_4, 5, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.marge_path_lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.marge_path_lineEdit.setObjectName("marge_path_lineEdit")
        self.horizontalLayout_3.addWidget(self.marge_path_lineEdit)
        self.get_marge_path_pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.get_marge_path_pushButton.setEnabled(False)
        self.get_marge_path_pushButton.setObjectName("get_marge_path_pushButton")
        self.horizontalLayout_3.addWidget(self.get_marge_path_pushButton)
        self.default_path_radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.default_path_radioButton.setChecked(True)
        self.default_path_radioButton.setObjectName("default_path_radioButton")
        self.horizontalLayout_3.addWidget(self.default_path_radioButton)
        self.custom_path_radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.custom_path_radioButton.setObjectName("custom_path_radioButton")
        self.horizontalLayout_3.addWidget(self.custom_path_radioButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.marge_pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.marge_pushButton.setObjectName("marge_pushButton")
        self.horizontalLayout_3.addWidget(self.marge_pushButton)
        self.gridLayout.addWidget(self.groupBox_3, 4, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lock_time_timeEdit = QtWidgets.QTimeEdit(self.groupBox_5)
        self.lock_time_timeEdit.setMinimumTime(QtCore.QTime(12, 0, 0))
        self.lock_time_timeEdit.setObjectName("lock_time_timeEdit")
        self.gridLayout_3.addWidget(self.lock_time_timeEdit, 0, 1, 1, 1)
        self.cycle_lock_radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.cycle_lock_radioButton.setObjectName("cycle_lock_radioButton")
        self.gridLayout_3.addWidget(self.cycle_lock_radioButton, 0, 6, 1, 1)
        self.once_lock_radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.once_lock_radioButton.setChecked(True)
        self.once_lock_radioButton.setObjectName("once_lock_radioButton")
        self.gridLayout_3.addWidget(self.once_lock_radioButton, 0, 5, 1, 1)
        self.create_lock_pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.create_lock_pushButton.setObjectName("create_lock_pushButton")
        self.gridLayout_3.addWidget(self.create_lock_pushButton, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.lock_now_pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.lock_now_pushButton.setObjectName("lock_now_pushButton")
        self.gridLayout_3.addWidget(self.lock_now_pushButton, 0, 4, 1, 1)
        self.cancel_lock_pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.cancel_lock_pushButton.setObjectName("cancel_lock_pushButton")
        self.gridLayout_3.addWidget(self.cancel_lock_pushButton, 0, 7, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox_5, 2, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "小工具箱"))
        self.groupBox_2.setTitle(_translate("mainWindow", "微信多开"))
        self.label_2.setText(_translate("mainWindow", "微信路径："))
        self.get_wechat_path_pushButton.setToolTip(_translate("mainWindow", "<html><head/><body><p>第一次使用需要设置微信程序路径</p></body></html>"))
        self.get_wechat_path_pushButton.setText(_translate("mainWindow", "设置路径"))
        self.label_3.setText(_translate("mainWindow", "多开数量："))
        self.start_wechat_pushButton.setText(_translate("mainWindow", "开启"))
        self.groupBox.setTitle(_translate("mainWindow", "关机计划"))
        self.cycle_radioButton.setText(_translate("mainWindow", "每日循环"))
        self.once_radioButton.setText(_translate("mainWindow", "单次关机"))
        self.create_plan_pushButton.setText(_translate("mainWindow", "创建"))
        self.shutdown_timeEdit.setDisplayFormat(_translate("mainWindow", "HH:mm:ss"))
        self.label.setText(_translate("mainWindow", "关机时间："))
        self.cancel_pushButton.setText(_translate("mainWindow", "取消关机"))
        self.shutdown_now_pushButton.setText(_translate("mainWindow", "立即关机"))
        self.groupBox_4.setTitle(_translate("mainWindow", "状态反馈"))
        self.groupBox_3.setTitle(_translate("mainWindow", "excel合并"))
        self.label_4.setText(_translate("mainWindow", "合并路径："))
        self.get_marge_path_pushButton.setToolTip(_translate("mainWindow", "<html><head/><body><p>第一次使用需要设置微信程序路径</p></body></html>"))
        self.get_marge_path_pushButton.setText(_translate("mainWindow", "选择文件夹"))
        self.default_path_radioButton.setText(_translate("mainWindow", "当前路径"))
        self.custom_path_radioButton.setText(_translate("mainWindow", "自定义路径"))
        self.marge_pushButton.setText(_translate("mainWindow", "合并"))
        self.groupBox_5.setTitle(_translate("mainWindow", "锁屏"))
        self.lock_time_timeEdit.setDisplayFormat(_translate("mainWindow", "HH:mm:ss"))
        self.cycle_lock_radioButton.setText(_translate("mainWindow", "每日循环"))
        self.once_lock_radioButton.setText(_translate("mainWindow", "单次锁屏"))
        self.create_lock_pushButton.setText(_translate("mainWindow", "创建锁屏计划"))
        self.label_5.setText(_translate("mainWindow", "锁屏时间"))
        self.lock_now_pushButton.setText(_translate("mainWindow", "立即锁屏"))
        self.cancel_lock_pushButton.setText(_translate("mainWindow", "取消计划"))
