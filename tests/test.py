# from tests.test_ui import Ui_Dialog
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
from time import sleep

qtCreatorFile = "test_ui.ui"
Ui_Dialog, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(Ui_Dialog, QWidget):
    parse_triggered = pyqtSignal()

    def __init__(self, parent=None, name=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)

    def accept(self):
        # for i in range(1000000):
        #     print(i)
        self.label.setText('accept')

    def reject(self):
        self.label.setText('reject')


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QWidget
    a = QApplication([])
    w = QWidget()
    w.show()
    from PyQt5 import QtCore
    # app = QApplication(sys.argv)
    # window = MyApp()
    # window.   show()
    from time import sleep
    sleep(10)
    # sys.exit(app.exec_())
