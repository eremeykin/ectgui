# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Dec 10 14:49:23 2016
# by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from normalization_dialog import NormalizationDialog
import numpy as np


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data=pd.DataFrame(), parent=None, *args):
        super(TableModel, self).__init__()
        self.datatable = data

    def update(self, dataIn):
        self.datatable = dataIn

    def rowCount(self, parent=QtCore.QModelIndex()):
        return self.datatable.shape[0]

    def columnCount(self, parent=QtCore.QModelIndex()):
        if len(self.datatable.shape) > 1:
            return self.datatable.shape[1]
        if self.datatable.shape[0] == 0:
            return 1
        return 0

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            i = index.row()
            j = index.column()
            return '{0}'.format(self.datatable.iget_value(i, j))
        else:
            return QtCore.QVariant()

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.datatable.columns.values[col])
        if orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(str(self.datatable.index.values[col]))
        return QtCore.QVariant()

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled

    def get_data(self):
        return self.datatable


class Ui_MainWindow(QtWidgets.QMainWindow):
    app_name = "Effective Clustering Toolkit"
    _translate = QtCore.QCoreApplication.translate

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)

        # table 1
        self.tableRaw = QtWidgets.QTableView()
        self.tableRaw.setModel(TableModel(pd.DataFrame()))
        self.tableRaw.setObjectName("tableRaw")
        self.tableRaw.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        header = self.tableRaw.horizontalHeader()
        header.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        header.customContextMenuRequested.connect(self.showHeaderMenu)

        # table 2
        self.tablePrepared = QtWidgets.QTableView()
        self.tablePrepared.setModel(TableModel(pd.DataFrame()))
        self.tablePrepared.setObjectName("tablePrepared")

        self.tab_layout()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuLayout = QtWidgets.QMenu(self.menuView)
        self.menuLayout.setObjectName("menuLayout")
        self.menuView.addMenu(self.menuLayout)

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # open action
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.open)
        self.menuFile.addAction(self.actionOpen)

        # tabLayout action
        self.actionTabLayout = QtWidgets.QAction(MainWindow)
        self.actionTabLayout.setObjectName("actionTabLayout")
        self.actionTabLayout.triggered.connect(self.tab_layout)
        self.menuLayout.addAction(self.actionTabLayout)

        # tabLayout action
        self.actionPanelLayout = QtWidgets.QAction(MainWindow)
        self.actionPanelLayout.setObjectName("actionPanelLayout")
        self.actionPanelLayout.triggered.connect(self.panel_layout)
        self.menuLayout.addAction(self.actionPanelLayout)

        # normalize action
        self.actionNormalize = QtWidgets.QAction(MainWindow)
        self.actionNormalize.setObjectName("actionNormalize")
        self.actionNormalize.triggered.connect(self.normalize)
        self.menuEdit.addAction(self.actionNormalize)

        # exit action
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.close_app)
        self.menuFile.addAction(self.actionExit)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def normalize(self):
        result = NormalizationDialog.open()
        if result:
            df = self.tablePrepared.model().get_data()
            center = None
            range = None
            if result.center == NormalizationDialog.Result.Center.Mean:
                center = df.mean()
            if result.center == NormalizationDialog.Result.Center.Median:
                center = df.median()
            if result.center == NormalizationDialog.Result.Center.Minimum:
                center = df.min()
            if result.center == NormalizationDialog.Result.Center.MinkovskyCenter:
                raise Error('Unsupported yet')
            if result.range == NormalizationDialog.Result.Range.AbsoluteDeviation:
                range = df.std()
            if result.range == NormalizationDialog.Result.Range.Semirange:
                range = df.max()-df.min()
            if result.range == NormalizationDialog.Result.Range.AbsoluteDeviation:
                raise Error('Unsupported yet')
            if center is None or range is None:
                raise Error('Undefined error')
            new_df = (df - center)/range
            model = TableModel(new_df)
            self.tablePrepared.setModel(model)

    def open(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '\home')[0]
        data = pd.read_csv(fname)
        model = TableModel(data)
        self.tableRaw.setModel(model)
        MainWindow.setWindowTitle(Ui_MainWindow._translate("MainWindow", Ui_MainWindow.app_name) + ": " + fname)

    def prepare(self, column):
        df_raw = self.tableRaw.model().get_data()
        ds = df_raw[df_raw.columns[column]]
        df = self.tablePrepared.model().get_data()
        try:
            pd.to_numeric(ds)
            if len(df) == 0:
                df = pd.DataFrame()
            df[ds.name] = ds
            model = TableModel(df)
            self.tablePrepared.setModel(model)
        except ValueError:
            from nominal_feature_dialog import NominalFeatureDialog
            is_ok = NominalFeatureDialog.open()
            if is_ok:
                if len(df) == 0:
                     df = pd.DataFrame()
                unique_values = ds.unique()
                for uv in unique_values:
                    new_col = pd.Series(data=0, index=ds.index)
                    new_col[ds == uv] = 1
                    df[ds.name+str(uv)] = new_col
                model = TableModel(df)
                self.tablePrepared.setModel(model)


    def showHeaderMenu(self, point):
        column = self.tableRaw.horizontalHeader().logicalIndexAt(point.x())
        # show menu about the column
        menu = QtWidgets.QMenu(self)
        action = QtWidgets.QAction(MainWindow)
        action.setObjectName("actionPrepare")
        action.triggered.connect(lambda x: self.prepare(column))
        action.setText(Ui_MainWindow._translate("MainWindow", "Prepare"))
        menu.addAction(action)
        menu.popup(self.tableRaw.horizontalHeader().mapToGlobal(point))

    def _clean(self):
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)

    def tab_layout(self):
        self._clean()
        # tabRaw
        self.tabRaw = QtWidgets.QWidget()
        self.tabRaw.setObjectName("tab")
        self.gridLayoutRaw = QtWidgets.QGridLayout(self.tabRaw)
        self.gridLayoutRaw.setObjectName("gridLayoutRaw")
        # tabPrepared
        self.tabPrepared = QtWidgets.QWidget()
        self.tabPrepared.setObjectName("tabPrepared")
        self.gridLayoutPrepared = QtWidgets.QGridLayout(self.tabPrepared)
        self.gridLayoutPrepared.setObjectName("gridLayoutPrepared")
        # add tables
        self.gridLayoutPrepared.addWidget(self.tablePrepared)
        self.gridLayoutRaw.addWidget(self.tableRaw)
        # tabWidget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.addTab(self.tabRaw, "")
        self.tabWidget.addTab(self.tabPrepared, "")
        # add to layout
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRaw),
                                  Ui_MainWindow._translate("MainWindow", "Raw Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPrepared),
                                  Ui_MainWindow._translate("MainWindow", "Prepared Data"))

    def panel_layout(self):
        self._clean()
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.splitter.addWidget(self.tableRaw)
        self.splitter.addWidget(self.tablePrepared)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

    def close_app(self):
        sys.exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", Ui_MainWindow.app_name))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuLayout.setTitle(_translate("MainWindow", "Layout"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionNormalize.setText(_translate("MainWindow", "Normalize"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionPanelLayout.setText(_translate("MainWindow", "Panel Layout"))
        self.actionTabLayout.setText(_translate("MainWindow", "Tab Layout"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRaw), _translate("MainWindow", "Raw Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPrepared), _translate("MainWindow", "Prepared Data"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())

