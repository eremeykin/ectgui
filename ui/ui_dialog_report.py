# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_report.ui'
#
# Created: Tue Apr 25 18:57:07 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UiDialogReport(QtWidgets.QDialog):
    def __init__(self, parent, string):
        super(UiDialogReport, self).__init__(parent)
        self.setObjectName("Dialog")
        self.resize(765, 480)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setPlainText(string)
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.retranslateUi()
        self.setWindowTitle("Report")
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # Dialog = QtWidgets.QDialog()
    ui = UiDialogReport(None,'Some test \n\t string')
    ui.open()
    sys.exit(app.exec_())
