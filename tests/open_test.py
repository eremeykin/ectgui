import sys
import unittest
from PyQt5 import QtGui

from PyQt5 import Qt

from PyQt5.QtTest import QTest
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog

import ect_main_window
import threading
import time
from pprint import pprint

app = QtWidgets.QApplication(sys.argv)


class OpenTest(unittest.TestCase):
    def setUp(self):
        """Create the GUI"""
        self.form = ect_main_window.EctMainWindow()

    def check(self, wid):
        for w in wid.findChildren(QtWidgets.QWidget):
            w.setWindowTitle('MYSUPERTEST')
            self.check(w)
            print('set')

    def test(self):
        time.sleep(5)
        wds = self.form.ui.findChildren(QtWidgets.QWidget)
        wds = app.topLevelWidgets()
        for w in wds:
            w.setWindowTitle('MYSUPERTEST')
            self.check(w)
        print('OK')
        # dialog = self.form.ui.findChildren(QtWidgets.QWidget)
        # while not dialog:
        #     dialog = self.form.ui.findChildren(QtWidgets.QWidget)
        #     if len(dialog)>0: dialog=dialog[0]
        #     time.sleep(1)
        # b = dialog.findChildren(object)
        # dialog.setWindowTitle('MYSUPERTEST')
        # QTest.keyClicks(dialog, 'L', QtCore.Qt.ControlModifier)



    def test_open(self):
        file_widget = self.form.ui.menu_file
        QTest.mouseClick(file_widget, Qt.Qt.LeftButton)
        file_open_widget = self.form.ui.action_open
        t = threading.Thread(target=self.test)
        t.daemon = True
        t.start()
        file_open_widget.trigger()

        # t = threading.Thread(target=self.open_filedialog, args=(file_open_widget,))
        # t = threading.Thread(target=file_open_widget.toggle)

        # t = threading.Thread(target=file_open_widget.trigger)

        # print('1')
        # t.daemon = True
        # print('2')
        # t.start()
        # print('3')
        # # QTest.keyClicks(self.form.ui, 'L', Qt.ControlModifier)
        # import time
        # time.sleep(200)
        # print(self.form.findChildren(QDialog))
        # for w in app.topLevelWidgets():
        #     print('4')
        #     print(type(w))
        #     print(str(w))
