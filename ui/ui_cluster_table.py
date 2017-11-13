# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cluster_table.ui'
#
# Created: Sun Jun 18 12:56:42 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!
import pandas as pd
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

from table_models import ReportTableModel


class UiDialogCLusterTable(QtWidgets.QDialog):
    def __init__(self, parent, report):
        super(UiDialogCLusterTable, self).__init__(parent)
        self.report = report
        self.setObjectName("Dialog")
        self.resize(795, 590)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.set_model()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def set_model(self):
        df = pd.DataFrame(columns=list(self.report.norm_data.columns))
        counts = []
        for ul in self.report.u_labels:
            s = pd.Series(self.report.clusters[ul].centroid, index=list(self.report.norm_data.columns))
            df = df.append(s, ignore_index=True)
            counts.append(self.report.clusters[ul].power)

        wtm = ReportTableModel(counts, self.report.data.mean(), df)
        self.tableView.setModel(wtm)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.resizeColumnsToContents()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # Dialog = QtWidgets.QDialog()
    ui = UiDialogCLusterTable(None)
    ui.open()
    sys.exit(app.exec_())
