import sys
import unittest
from PyQt5 import Qt

from PyQt5.QtTest import QTest
from PyQt5 import QtCore, QtWidgets
import ect_main_window

app = QtWidgets.QApplication(sys.argv)

class OpenTest(unittest.TestCase):

    def setUp(self):
        """Create the GUI"""
        self.form = ect_main_window.EctMainWindow()

    def test_open(self):
        file_widget = self.form.ui.menu_file
        QTest.mouseClick(file_widget, Qt.Qt.LeftButton)
        import time
        time.sleep(5)

