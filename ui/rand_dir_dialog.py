# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rand_dir_dialog.ui'
#
# Created: Thu Mar 16 00:42:47 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtGui import QIntValidator


class RandDirDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(RandDirDialog, self).__init__(parent)
        self.setObjectName("Dialog")
        self.resize(300, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.toggled.connect(lambda x: self.check_box_toggled())
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBox)
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setValidator(QDoubleValidator())
        self.lineEdit.setText(str(0.32))
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setValidator(QIntValidator())
        if parent is not None:
            V = parent.ui.table_normalized.model().get_data().shape[1]
            self.lineEdit_2.setText(str(V))
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.check_box_toggled()
        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def check_box_toggled(self):
        self.label.setEnabled(self.checkBox.isChecked())
        self.label_2.setEnabled(self.checkBox.isChecked())
        self.lineEdit.setEnabled(self.checkBox.isChecked())
        self.lineEdit_2.setEnabled(self.checkBox.isChecked())

    @staticmethod
    def open(parent=None):
        dialog = RandDirDialog(parent)
        result = dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            return dialog.get_result()
        else:
            return False

    def get_result(self):
        try:
            epsilon = float(self.lineEdit.text())
        except:
            epsilon = None
        try:
            s_directions = int(self.lineEdit_2.text())
        except:
            s_directions = None
        return self.checkBox.isChecked(), epsilon, s_directions

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox.setText(_translate("Dialog", "Random directions"))
        self.label.setText(_translate("Dialog", "Epsilon"))
        self.label_2.setText(_translate("Dialog", "Number of directions"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = RandDirDialog(None)
    # ui.open()
    # ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
