# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kovaleva_dialog.ui'
#
# Created: Tue Mar 14 00:05:56 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtGui import QIntValidator
from PyQt5.QtGui import QValidator
import re
import string


class Validator(QValidator):
    def __init__(self, parent=None):
        super(Validator, self).__init__(parent)
        self._replace = re.compile(r'[^A-Za-z0-9]').sub

    def validate(self, str, pos):
        prts = str.split('x')
        if len(prts) == 2:
            str = ''.join([x for x in prts[0] if x in string.digits]) + 'x' + ''.join(
                [x for x in prts[1] if x in string.digits])
        else:
            str += 'x1'
        return QValidator.Acceptable, str, pos


class KovalevaGeneratorDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(KovalevaGeneratorDialog, self).__init__(parent)
        self.setObjectName("Dialog")
        self.resize(476, 250)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setValidator(QIntValidator())

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setValidator(QIntValidator())
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setValidator(Validator())

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setValidator(QDoubleValidator())

        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Minimal cluster cardinality"))
        self.label_2.setText(_translate("Dialog", "Number of clusters"))
        self.label_3.setText(_translate("Dialog", "Size"))
        self.label_4.setText(_translate("Dialog", "a"))

    @staticmethod
    def open(parent=None):
        dialog = KovalevaGeneratorDialog(parent)
        result = dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            return dialog.get_result()
        else:
            return False

    def get_result(self):
        min_cluster_card = int(self.lineEdit.text())
        K = int(self.lineEdit_2.text())
        size = (int(self.lineEdit_3.text().split('x')[0]), int(self.lineEdit_3.text().split('x')[1]))
        a = float(self.lineEdit_4.text().replace(',','.'))
        return min_cluster_card, K, size, a

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Minimal cluster cardinality"))
        self.label_2.setText(_translate("Dialog", "Number of clusters"))
        self.label_3.setText(_translate("Dialog", "Size"))
        self.label_4.setText(_translate("Dialog", "a"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = KovalevaGeneratorDialog()
    # ui.open()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
