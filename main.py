from PyQt5.QtWidgets import *
from login import Ui_LoginDialog

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = QDialog()
    login_dialog = Ui_LoginDialog()
    login_dialog.setupUi(main)
    main.show()
    sys.exit(app.exec_())


