# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test3.ui'
#
# Created: Thu Dec 15 00:49:06 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class NormalizationDialog(QtWidgets.QDialog):

    class Result(object):
        class Center(object):
            Minimum = 0
            Mean = 2
            Median = 4
            MinkovskyCenter = 8

        class Range(object):
            Semirange = 0
            StandardDeviation = 2
            AbsoluteDeviation = 4

        def __init__(self, center, range):
            self.center=None
            self.range=None
            if center == 'minimum': self.center = NormalizationDialog.Result.Center.Minimum
            elif center == 'mean': self.center = NormalizationDialog.Result.Center.Mean
            elif center == 'median': self.center = NormalizationDialog.Result.Center.Median
            elif center == 'Minkovsky center': self.center = NormalizationDialog.Result.Center.MinkovskyCenter
            else: raise ValueError('Unknown center type:' + str(center))
            if range == 'semirange': self.range = NormalizationDialog.Result.Range.Semirange
            elif range == 'standard deviation': self.range = NormalizationDialog.Result.Range.StandardDeviation
            elif range == 'absolute deviation from the median': self.range = NormalizationDialog.Result.Range.AbsoluteDeviation
            else: raise ValueError('Unknown range type:' + str(range))

        def __str__(self):
            return '('+str(self.center)+';'+str(self.range)+')'

        def __bool__(self):
            return self.center is not None and self.range is not None

    def __init__(self, parent):
        super(NormalizationDialog, self).__init__(parent)
        self.setObjectName("Dialog")
        self.resize(329, 161)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox_1 = QtWidgets.QComboBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_1.sizePolicy().hasHeightForWidth())
        self.comboBox_1.setSizePolicy(sizePolicy)
        self.comboBox_1.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_1.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_1.setObjectName("comboBox")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.comboBox_2 = QtWidgets.QComboBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Please, specify normalization settings:"))
        self.label_2.setText(_translate("Dialog", "Center:"))
        self.comboBox_1.setItemText(0, _translate("Dialog", "minimum"))
        self.comboBox_1.setItemText(1, _translate("Dialog", "mean"))
        self.comboBox_1.setItemText(2, _translate("Dialog", "median"))
        self.comboBox_1.setItemText(3, _translate("Dialog", "Minkovsky center"))
        self.label_3.setText(_translate("Dialog", "Range:"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "semirange"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "standard deviation"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "absolute deviation from the median"))

    def get_result(self):
        center = str(self.comboBox_1.currentText())
        range = str(self.comboBox_2.currentText())
        return NormalizationDialog.Result(center, range)

    @staticmethod
    def open(parent=None):
        dialog = NormalizationDialog(parent)
        result = dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            return dialog.get_result()
        else:
            return False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    print(NormalizationDialog.open())
    exit()
    Dialog = QtWidgets.QDialog()
    ui = NormalizationDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

