# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Dec 10 14:49:23 2016
# by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!
import pandas as pd
from PyQt5 import QtCore, QtWidgets

from normalization import Normalization
from table_models import RawTableModel, NormalizedTableModel


class Ui_EctMainWindow(QtWidgets.QWidget):
    app_name = "Effective Clustering Toolkit"

    def setupUi(self, ect_main_window):
        ect_main_window.setObjectName("ect_main_window")
        ect_main_window.resize(800, 600)

        self.central_widget = QtWidgets.QWidget(ect_main_window)
        self.central_widget.setObjectName("central_widget")
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setObjectName("grid_layout")
        self.grid_layout.setContentsMargins(2, 2, 2, 2)
        # table 1
        self.table_raw = QtWidgets.QTableView()
        self.table_raw.setModel(RawTableModel(pd.DataFrame()))
        self.table_raw.setObjectName("table_raw")
        self.table_raw.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        header_raw = self.table_raw.horizontalHeader()
        header_raw.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        header_raw.customContextMenuRequested.connect(
            lambda p: ect_main_window.show_header_menu(point=p, table=self.table_raw))
        # table 2
        self.table_normalized = QtWidgets.QTableView()
        norm_table_model = NormalizedTableModel(pd.DataFrame(),
                                                Normalization(Normalization.Center.NONE_CENTER,
                                                              Normalization.Range.NONE_RANGE))
        self.table_normalized.setModel(norm_table_model)
        self.table_normalized.setObjectName("table_normalized")
        header_norm = self.table_normalized.horizontalHeader()
        header_norm.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        header_norm.customContextMenuRequested.connect(
            lambda p: ect_main_window.show_header_menu(point=p, table=self.table_normalized))

        header_raw.sectionDoubleClicked.connect(
            lambda point: ect_main_window.double_clicked_raw(point))

        header_norm.sectionDoubleClicked.connect(
            lambda point: ect_main_window.double_clicked_norm(point))

        self.tab_raw = QtWidgets.QWidget()
        self.tab_raw.setObjectName("tab_raw")
        self.grid_layout_raw = QtWidgets.QGridLayout(self.tab_raw)
        self.grid_layout_raw.setContentsMargins(2, 2, 2, 2)
        self.grid_layout_raw.setObjectName("grid_layout_raw")
        # tabNormalized
        self.tab_normalized = QtWidgets.QWidget()
        self.tab_normalized.setObjectName("tab_normalized")
        self.grid_layout_normalized = QtWidgets.QGridLayout(self.tab_normalized)
        self.grid_layout_normalized.setObjectName("grid_layout_normalized")
        # add tables
        self.grid_layout_normalized.addWidget(self.table_normalized)
        self.grid_layout_normalized.setContentsMargins(2, 2, 2, 2)
        self.grid_layout_raw.addWidget(self.table_raw)

        ect_main_window.action_panel_layout()

        ect_main_window.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(ect_main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        # File menu
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        # View menu
        self.menu_view = QtWidgets.QMenu(self.menubar)
        self.menu_view.setObjectName("menu_view")
        # Setting menu
        self.menu_settings = QtWidgets.QMenu(self.menubar)
        self.menu_settings.setObjectName("menu_settings")
        # Layout menu
        self.menu_layout = QtWidgets.QMenu(self.menu_view)
        self.menu_layout.setObjectName("menu_layout")
        self.menu_view.addMenu(self.menu_layout)
        # Clustering menu
        self.menu_run = QtWidgets.QMenu(self.menubar)
        self.menu_run.setObjectName("menu_clustering")
        # Plot menu
        self.menu_plot = QtWidgets.QMenu(self.menubar)
        self.menu_plot.setObjectName("menu_plot")
        # Report menu
        self.menu_report = QtWidgets.QMenu(self.menubar)
        self.menu_report.setObjectName("menu_report")

        # open action
        self.action_open = QtWidgets.QAction(ect_main_window)
        self.action_open.setObjectName("action_open")
        self.action_open.triggered.connect(ect_main_window.action_open)
        self.menu_file.addAction(self.action_open)

        # Menu File->Data
        self.menu_data = QtWidgets.QMenu(self.menu_file)
        self.menu_data.setObjectName("menu_data")
        self.menu_file.addMenu(self.menu_data)

        ect_main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ect_main_window)
        self.statusbar.setObjectName("statusbar")
        ect_main_window.setStatusBar(self.statusbar)
        # generate action
        self.action_generate = QtWidgets.QAction(ect_main_window)
        self.action_generate.setObjectName("action_generate")
        self.action_generate.triggered.connect(ect_main_window.action_generate)
        self.menu_data.addAction(self.action_generate)
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
        # Run clustering action
        self.action_clustering = QtWidgets.QAction(ect_main_window)
        self.action_clustering.setObjectName("action_clustering")
        self.action_clustering.triggered.connect(ect_main_window.action_clustering)
        self.menu_run.addAction(self.action_clustering)
        # Run A-ward clustering
        # self.action_a_ward = QtWidgets.QAction(ect_main_window)
        # self.action_a_ward.setObjectName("action_a_ward")
        # self.action_a_ward.triggered.connect(ect_main_window.action_a_ward)
        # self.menu_run.addAction(self.action_a_ward)

        # action normalize all
        self.action_norm_all = QtWidgets.QAction(ect_main_window)
        self.action_norm_all.setObjectName("action_norm_all")
        self.action_norm_all.triggered.connect(ect_main_window.action_norm_all)
        self.menu_data.addAction(self.action_norm_all)
        # action clear normalize
        self.action_clear_norm = QtWidgets.QAction(ect_main_window)
        self.action_clear_norm.setObjectName("action_clear_norm")
        self.action_clear_norm.triggered.connect(ect_main_window.action_clear_norm)
        self.menu_data.addAction(self.action_clear_norm)
        # exit action
        self.action_exit = QtWidgets.QAction(ect_main_window)
        self.action_exit.setObjectName("action_exit")
        self.action_exit.triggered.connect(ect_main_window.action_exit)
        self.menu_file.addAction(self.action_exit)
        # by_markers action
        self.action_by_markers = QtWidgets.QAction(ect_main_window)
        self.action_by_markers.setObjectName("action_by_markers")
        self.action_by_markers.triggered.connect(ect_main_window.plot_by_markers)
        self.menu_plot.addAction(self.action_by_markers)
        # delete markers
        self.action_delete_markers = QtWidgets.QAction(ect_main_window)
        self.action_delete_markers.setObjectName("action_delete_markers")
        self.action_delete_markers.triggered.connect(ect_main_window.delete_markers)
        self.menu_plot.addAction(self.action_delete_markers)
        # menu plot->svd
        self.menu_svd = QtWidgets.QMenu(self.menu_view)
        self.menu_svd.setObjectName("menu_svd")
        self.menu_plot.addMenu(self.menu_svd)
        # normalized action
        self.action_normalized = QtWidgets.QAction(ect_main_window)
        self.action_normalized.setObjectName("action_normalized")
        self.action_normalized.triggered.connect(ect_main_window.action_plot_svd_norm)
        # raw data
        self.action_raw = QtWidgets.QAction(ect_main_window)
        self.action_raw.setObjectName("action_raw")
        self.action_raw.triggered.connect(ect_main_window.action_plot_svd_raw)
        # report action
        self.action_report = QtWidgets.QAction(ect_main_window)
        self.action_report.setObjectName("action_report")
        self.action_report.triggered.connect(ect_main_window.action_report)
        self.menu_report.addAction(self.action_report)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_run.menuAction())
        self.menubar.addAction(self.menu_plot.menuAction())
        self.menubar.addAction(self.menu_report.menuAction())
        self.menu_svd.addAction(self.action_normalized)
        self.menu_svd.addAction(self.action_raw)

        self.retranslateUi(ect_main_window)
        QtCore.QMetaObject.connectSlotsByName(ect_main_window)

    def retranslateUi(self, ect_main_window):
        _translate = QtCore.QCoreApplication.translate
        ect_main_window.setWindowTitle(_translate("ect_main_window", Ui_EctMainWindow.app_name))
        self.menu_file.setTitle(_translate("ect_main_window", "File"))
        self.menu_view.setTitle(_translate("ect_main_window", "View"))
        self.menu_settings.setTitle(_translate("ect_main_window", "Settings"))
        self.menu_layout.setTitle(_translate("ect_main_window", "Layout"))
        self.menu_run.setTitle(_translate("ect_main_window", "Run"))
        self.menu_plot.setTitle(_translate("ect_main_window", "Plot"))
        self.menu_data.setTitle(_translate("ect_main_window", "Data"))
        self.menu_report.setTitle(_translate("ect_main_window", "Report"))
        self.action_open.setText(_translate("ect_main_window", "Open"))
        self.action_generate.setText(_translate("ect_main_window", "Generate"))
        self.action_normalize.setText(_translate("ect_main_window", "Normalization ..."))
        self.action_exit.setText(_translate("ect_main_window", "Exit"))
        self.action_panel_layout.setText(_translate("ect_main_window", "Panel Layout"))
        self.action_tab_layout.setText(_translate("ect_main_window", "Tab Layout"))
        self.action_clustering.setText(_translate("ect_main_window", "Clustering"))
        # self.action_a_ward.setText(_translate("ect_main_window", "A Ward"))
        self.action_by_markers.setText(_translate("ect_main_window", "Plot Data by Markers"))
        self.action_delete_markers.setText(_translate("ect_main_window", "Delete All Markers"))
        self.action_normalized.setText(_translate("ect_main_window", "Normalaized"))
        self.action_raw.setText(_translate("ect_main_window", "Raw"))
        self.menu_svd.setTitle(_translate("ect_main_window", "SVD"))
        self.action_norm_all.setText(_translate("ect_main_window", "Normalize All"))
        self.action_clear_norm.setText(_translate("ect_main_window", "Clear Normalized"))
        self.action_report.setText(_translate("ect_main_window", "Show ..."))

    def translate(self, arg):
        _translate = QtCore.QCoreApplication.translate
        return _translate("ect_main_window", arg)
