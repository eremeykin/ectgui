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

        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.radioButton_11 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_11.setChecked(True)
        self.radioButton_11.setObjectName("radioButton_11")
        self.verticalLayout_4.addWidget(self.radioButton_11)

        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_8.setChecked(False)
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout_4.addWidget(self.radioButton_8)

        # self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_3)
        # self.radioButton_7.setObjectName("radioButton_7")
        # self.verticalLayout_4.addWidget(self.radioButton_7)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_10.setObjectName("radioButton_10")
        self.horizontalLayout_2.addWidget(self.radioButton_10)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        # ##############333
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_9.setObjectName("radioButton_9")
        self.verticalLayout_4.addWidget(self.radioButton_9)
        # ##############333
        self.verticalLayout.addWidget(self.groupBox_3)

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
        # self.radioButton_3.toggled.connect(self.disable)

        self.radioButton.toggled.connect(lambda x: self.refresh_disabled(self.radioButton))
        self.radioButton_2.toggled.connect(lambda x: self.refresh_disabled(self.radioButton_2))
        self.radioButton_3.toggled.connect(lambda x: self.refresh_disabled(self.radioButton_3))
        self.radioButton_4.toggled.connect(lambda x: self.refresh_disabled(self.radioButton_4))
        self.radioButton_5.toggled.connect(lambda x: self.refresh_disabled(self.radioButton_5))
        self.radioButton_6.toggled.connect(lambda x: self.refresh_disabled(self.radioButton_6))
        # self.radioButton_7.toggled.connect(lambda x: self.refresh_disabled(self.radioButton_7))
        self.radioButton_8.toggled.connect(lambda x: self.refresh_disabled(self.radioButton_8))
        self.radioButton_9.toggled.connect(lambda x: self.refresh_disabled(self.radioButton_9))
        self.radioButton_10.toggled.connect(lambda x: self.refresh_disabled(self.radioButton_10))

        self._init_disabled()
        QtCore.QMetaObject.connectSlotsByName(self)

    #
    # def disable(self):
    #     self.tableView.setDisabled(not self.radioButton_3.isChecked())

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

        self.groupBox_3.setTitle(_translate("Dialog", "1) Number of clusters"))
        self.radioButton_8.setText(_translate("Dialog", "Minimum of density"))
        # self.radioButton_7.setText(_translate("Dialog", "Anomalously defined"))
        self.radioButton_10.setText(_translate("Dialog", "Set explicitly"))
        self.radioButton_9.setText(_translate("Dialog", "(?) Cross validation"))
        self.radioButton_11.setText(_translate("Dialog", "A-Ward stop criterion"))

        self.groupBox_2.setTitle(_translate("Dialog", "2) Minkowski power"))
        self.radioButton_4.setText(_translate("Dialog", "p = 2"))
        self.radioButton_5.setText(_translate("Dialog", "p = "))
        self.radioButton_6.setText(_translate("Dialog", "Automatically calculated"))

        self.groupBox.setTitle(_translate("Dialog", "3) Weights"))
        self.radioButton_2.setText(_translate("Dialog", "No feature weights"))
        self.radioButton.setText(_translate("Dialog", "Cluster-specific weights"))
        self.radioButton_3.setText(_translate("Dialog", "No cluster-specificity"))

    def _init_disabled(self):
        self.radioButton.setDisabled(True)

        self.lineEdit.setDisabled(True)
        self.lineEdit_2.setDisabled(True)

        self.radioButton_5.setDisabled(True)
        self.radioButton_6.setDisabled(True)
        self.radioButton_9.setDisabled(True)

        self.tableView.setDisabled(not self.radioButton_3.isChecked())

    def refresh_disabled(self, rbutton):
        if rbutton.isChecked():
            # Minimum of density
            if rbutton == self.radioButton_8:
                self.radioButton_2.setEnabled(True)
                self.radioButton.setEnabled(False)
                self.radioButton_3.setEnabled(True)
                self.radioButton_4.setEnabled(True)
                self.radioButton_5.setEnabled(False)
                self.radioButton_6.setEnabled(False)
                self.lineEdit_2.setEnabled(False)
            # Anomalously defined
            if rbutton == self.radioButton_10:
                self.radioButton_2.setEnabled(True)
                self.radioButton.setEnabled(True)
                self.radioButton_3.setEnabled(True)
                self.radioButton_4.setEnabled(True)
                self.radioButton_5.setEnabled(True)
                self.radioButton_6.setEnabled(True)
                self.lineEdit_2.setEnabled(False)

            # Set explicitly
            if rbutton == self.radioButton_10:
                self.radioButton_2.setEnabled(True)
                self.radioButton.setEnabled(True)
                self.radioButton_3.setEnabled(True)
                self.radioButton_4.setEnabled(True)
                self.radioButton_5.setEnabled(True)
                self.radioButton_6.setEnabled(True)
                self.lineEdit_2.setEnabled(True)
            # p = 2
            if rbutton == self.radioButton_4:
                self.lineEdit.setEnabled(False)
            # p =
            if rbutton == self.radioButton_5:
                self.lineEdit.setEnabled(True)
            # Automatically calculated
            if rbutton == self.radioButton_6:
                self.lineEdit.setEnabled(False)
            # Cluster-specific weights
            if rbutton == self.radioButton:
                self.tableView.setDisabled(True)
            # No feature weights
            if rbutton == self.radioButton_2:
                self.tableView.setDisabled(True)
            # Uniform weights
            if rbutton == self.radioButton_3:
                self.tableView.setDisabled(False)

        for gr_box in [self.groupBox, self.groupBox_2, self.groupBox_3]:
            first_enabled = None
            for widget in gr_box.children():
                if isinstance(widget, QtWidgets.QRadioButton):
                    if widget.isEnabled():
                        first_enabled = widget
                        break
            for widget in gr_box.children():
                if isinstance(widget, QtWidgets.QRadioButton) \
                        and (not widget.isEnabled()) and widget.isChecked():
                    widget.setChecked(False)
                    first_enabled.setChecked(True)

    def get_result(self):
        try:
            n_clusters = int(self.lineEdit_2.text())
        except:
            n_clusters = None
        try:
            if self.radioButton_4.isChecked():
                minkowski = 2
            else:
                minkowski = int(self.lineEdit_2.text())
        except:
            minkowski = None
        try:
            weights = self.tableView.model().get_data()
        except:
            weights = None

        return RunClusteringDialog.Result(self.radioButton_11.isChecked(),
                                          self.radioButton_8.isChecked(),
                                          self.radioButton_9.isChecked(),
                                          self.radioButton_6.isChecked(),
                                          self.radioButton.isChecked(),
                                          n_clusters, minkowski, weights)

    @staticmethod
    def open(parent):
        dialog = RunClusteringDialog(parent)
        result = dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            res = dialog.get_result()
            return res
        else:
            return False

    class Result:
        def __init__(self, award_criterion, minimum_of_density, cross_validation, auto_mink, cluster_spec_weights,
                     n_clusters, minkowski,
                     weights):
            self.award_criterion = award_criterion
            self.minimum_of_density = minimum_of_density
            self.cross_validation = cross_validation
            self.n_clusters = n_clusters
            self.auto_mink = auto_mink
            self.cluster_spec_weights = cluster_spec_weights
            self.minkowski = minkowski
            self.weights = weights

        def __str__(self):
            return "minimum_of_density: " + str(self.minimum_of_density) + ';\n' + \
                   "cross_validation: " + str(self.cross_validation) + ';\n' + \
                   "n_clusters: " + str(self.n_clusters) + ';\n' + \
                   "auto_mink: " + str(self.auto_mink) + ";\n" + \
                   "cluster_spec_weights:" + str(self.cluster_spec_weights) + ";\n" + \
                   "minkowski: " + str(self.minkowski) + ';\n' + \
                   "weights: " + str(self.weights)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = RunClusteringDialog(None)
    # ui.open()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
