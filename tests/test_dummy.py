from tests.test import MyApp
from time import sleep
from PyQt5.QtCore import *


def test_myapp(qtbot):
    window = MyApp()
    qtbot.addWidget(window)
    window.show()
    qtbot.waitForWindowShown(window)
    sleep(3)
    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)
    assert window.label.text() == 'accept'
    qtbot.stopForInteraction()
