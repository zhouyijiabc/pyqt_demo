from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence


# 主界面
class MainWindow(QMainWindow):
    def closeEvent(self, e):
        if not text.document().isModified(): # 如果没有被修改
            return
        answer = QMessageBox.question(window, '关闭之前查看', '关闭之前是否保存文件',
                                      QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
                                      )
        if answer & QMessageBox.Save:
            save_file()
        elif answer & QMessageBox.Cancel:
            e.ignore()


app = QApplication([])
app.setApplicationName("文本编辑器")
text = QPlainTextEdit()
window = MainWindow()
window.setMinimumSize(800, 600) # 初始化大小
window.setCentralWidget(text)

# 菜单项的添加
menu = window.menuBar().addMenu('文件')
open_action = QAction('打开')
file_path = None


def open_file():
    global file_path
    path = QFileDialog.getOpenFileName(window, 'open')[0]
    if path:
        text.setPlainText(open(path).read())
        file_path = path


open_action.setShortcut(QKeySequence.Open)
open_action.triggered.connect(open_file)
menu.addAction(open_action)


def save_file():
    if file_path is None:
        pass
    else:
        with open(file_path, 'w') as f:
            f.write(text.toPlainText())
        text.document().setModified(False)


save_action = QAction('保存')
save_action.setShortcut(QKeySequence.Save)
menu.addAction(save_action)
save_action.triggered.connect(save_file)


def save_as():
    global file_path
    path = QFileDialog.getSaveFileName(window, '另存为')[0]
    if path:
        file_path = path
        save_file()


save_as_action = QAction('另存为')
save_as_action.triggered.connect(save_as)
menu.addAction(save_as_action)




menu.addSeparator() # 分割线
exit_action = QAction('退出')
exit_action.setShortcut(QKeySequence.Close)
menu.addAction(exit_action)
exit_action.triggered.connect(window.close)


# 帮助

def show_about():
    about_text = '<center>这是一个简易的文本编辑器</center><p>版本1.0</p>'
    QMessageBox.about(window, '说明', about_text)


help_menu = window.menuBar().addMenu('帮助')
about_action = QAction('关于')
about_action.triggered.connect(show_about)
help_menu.addAction(about_action)







window.show()
app.exec_()
