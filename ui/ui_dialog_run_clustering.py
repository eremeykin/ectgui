# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_run_clustering.ui'
#
# Created: Sun Feb  5 12:24:34 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
from table_models import WeightTableModel


class RunClusteringDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(RunClusteringDialog, self).__init__(parent)
        self.parent = parent
        self.setObjectName("Dialog")
        self.resize(651, 638)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 300))
        self.groupBox.setStyleSheet("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setObjectName("tableView")
        self.setTableModel()
        self.tableView.setDisabled(True)

        self.verticalLayout_2.addWidget(self.tableView)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_3.addWidget(self.radioButton_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout.addWidget(self.radioButton_5)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_3.addWidget(self.radioButton_6)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_8.setChecked(True)
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout_4.addWidget(self.radioButton_8)
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout_4.addWidget(self.radioButton_7)
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_9.setObjectName("radioButton_9")
        self.verticalLayout_4.addWidget(self.radioButton_9)
        self.verticalLayout.addWidget(self.groupBox_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi()
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.accepted.connect(self.accept)
        self.radioButton_3.toggled.connect(self.disable)
        QtCore.QMetaObject.connectSlotsByName(self)

    def disable(self):
        self.tableView.setDisabled(not self.radioButton_3.isChecked())

    def setTableModel(self):
        d = self.parent.ui.table_normalized.model().get_data()
        cols = list(d)
        if len(cols) == 0:
            return
        data = pd.DataFrame(data=np.full(fill_value=1 / len(cols), shape=(1, len(cols))), index=['W'], columns=cols)
        wtm = WeightTableModel(data)
        self.tableView.setModel(wtm)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Weights"))
        self.radioButton_2.setText(_translate("Dialog", "No feature weigths"))
        self.radioButton.setText(_translate("Dialog", "Cluster-specific weights"))
        self.radioButton_3.setText(_translate("Dialog", "Uniform weights"))
        self.groupBox_2.setTitle(_translate("Dialog", "Minkowski power"))
        self.radioButton_4.setText(_translate("Dialog", "p = 2"))
        self.radioButton_5.setText(_translate("Dialog", "p = "))
        self.radioButton_6.setText(_translate("Dialog", "Automatically calculated"))
        self.groupBox_3.setTitle(_translate("Dialog", "Number of clusters and initial centroids"))
        self.radioButton_8.setText(_translate("Dialog", "Runtime defined"))
        self.radioButton_7.setText(_translate("Dialog", "Defined by anomalous clustering"))
        self.radioButton_9.setText(_translate("Dialog", "A posteriori defined"))

    @staticmethod
    def open(parent):
        dialog = RunClusteringDialog(parent)
        result = dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            return True  # dialog.get_result()
        else:
            return False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = RunClusteringDialog(None)
    # ui.open()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())