# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Dec 10 14:49:23 2016
# by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!
import pandas as pd
from PyQt5 import QtCore, QtWidgets

from table_models import RawTableModel


class Ui_EctMainWindow(object):
    app_name = "Effective Clustering Toolkit"

    def setupUi(self, ect_main_window):
        ect_main_window.setObjectName("ect_main_window")
        ect_main_window.resize(800, 600)

        self.central_widget = QtWidgets.QWidget(ect_main_window)
        self.central_widget.setObjectName("central_widget")
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setObjectName("grid_layout")
        self.grid_layout.setContentsMargins(3, 3, 3, 3)
        # table 1
        self.table_raw = QtWidgets.QTableView()
        self.table_raw.setModel(RawTableModel(pd.DataFrame()))
        self.table_raw.setObjectName("table_raw")
        self.table_raw.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        header = self.table_raw.horizontalHeader()
        header.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        header.customContextMenuRequested.connect(ect_main_window.show_header_menu)
        # table 2
        self.table_normalized = QtWidgets.QTableView()
        self.table_normalized.setModel(RawTableModel(pd.DataFrame()))
        self.table_normalized.setObjectName("table_normalized")
        # tabRaw
        self.tab_raw = QtWidgets.QWidget()
        self.tab_raw.setObjectName("tab_raw")
        self.grid_layout_raw = QtWidgets.QGridLayout(self.tab_raw)
        self.grid_layout_raw.setObjectName("grid_layout_raw")
        # tabNormalized
        self.tab_normalized = QtWidgets.QWidget()
        self.tab_normalized.setObjectName("tab_normalized")
        self.grid_layout_normalized = QtWidgets.QGridLayout(self.tab_normalized)
        self.grid_layout_normalized.setObjectName("grid_layout_normalized")
        # add tables
        self.grid_layout_normalized.addWidget(self.table_normalized)
        self.grid_layout_raw.addWidget(self.table_raw)

        ect_main_window.action_panel_layout()

        ect_main_window.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(ect_main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_view = QtWidgets.QMenu(self.menubar)
        self.menu_view.setObjectName("menu_view")
        self.menu_settings = QtWidgets.QMenu(self.menubar)
        self.menu_settings.setObjectName("menu_settings")
        self.menu_layout = QtWidgets.QMenu(self.menu_view)
        self.menu_layout.setObjectName("menu_layout")
        self.menu_view.addMenu(self.menu_layout)

        ect_main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ect_main_window)
        self.statusbar.setObjectName("statusbar")
        ect_main_window.setStatusBar(self.statusbar)
        # open action
        self.action_open = QtWidgets.QAction(ect_main_window)
        self.action_open.setObjectName("action_open")
        self.action_open.triggered.connect(ect_main_window.action_open)
        self.menu_file.addAction(self.action_open)
        # tabLayout action
        self.action_tab_layout = QtWidgets.QAction(ect_main_window)
        self.action_tab_layout.setObjectName("action_tab_layout")
        self.action_tab_layout.triggered.connect(ect_main_window.action_tab_layout)
        self.menu_layout.addAction(self.action_tab_layout)
        # tabLayout action
        self.action_panel_layout = QtWidgets.QAction(ect_main_window)
        self.action_panel_layout.setObjectName("action_panel_layout")
        self.action_panel_layout.triggered.connect(ect_main_window.action_panel_layout)
        self.menu_layout.addAction(self.action_panel_layout)
        # normalize action
        self.action_normalize = QtWidgets.QAction(ect_main_window)
        self.action_normalize.setObjectName("action_normalize")
        self.action_normalize.triggered.connect(ect_main_window.action_normalize_settings)
        self.menu_settings.addAction(self.action_normalize)
        # exit action
        self.action_exit = QtWidgets.QAction(ect_main_window)
        self.action_exit.setObjectName("action_exit")
        self.action_exit.triggered.connect(ect_main_window.action_exit)
        self.menu_file.addAction(self.action_exit)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.retranslateUi(ect_main_window)
        QtCore.QMetaObject.connectSlotsByName(ect_main_window)

    def retranslateUi(self, ect_main_window):
        _translate = QtCore.QCoreApplication.translate
        ect_main_window.setWindowTitle(_translate("ect_main_window", Ui_EctMainWindow.app_name))
        self.menu_file.setTitle(_translate("ect_main_window", "File"))
        self.menu_view.setTitle(_translate("ect_main_window", "View"))
        self.menu_settings.setTitle(_translate("ect_main_window", "Settings"))
        self.menu_layout.setTitle(_translate("ect_main_window", "Layout"))
        self.action_open.setText(_translate("ect_main_window", "Open"))
        self.action_normalize.setText(_translate("ect_main_window", "Normalization ..."))
        self.action_exit.setText(_translate("ect_main_window", "Exit"))
        self.action_panel_layout.setText(_translate("ect_main_window", "Panel Layout"))
        self.action_tab_layout.setText(_translate("ect_main_window", "Tab Layout"))

    def translate(self, arg):
        _translate = QtCore.QCoreApplication.translate
        return _translate("ect_main_window", arg)
