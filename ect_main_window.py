# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Dec 10 14:49:23 2016
# by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!
import pandas as pd
from PyQt5 import QtCore, QtWidgets

from settings import Settings
from table_models import RawTableModel, NormalizedTableModel
from ui.ui_dialog_normalization import NormalizationDialog
from ui.ui_ect_main_window import Ui_EctMainWindow


class EctMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(EctMainWindow, self).__init__()
        self.settings = Settings()
        self.ui = Ui_EctMainWindow()
        self.ui.setupUi(self)

    def action_normalize_settings(self):
        result = NormalizationDialog.open(self)
        if result:
            self.settings.normalization = result
            m = self.ui.table_normalized.model()
            m.set_norm(result)
            self.ui.table_normalized.setModel(m)

    def action_open(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '\home')[0]
        data = pd.read_csv(fname)
        model = RawTableModel(data)
        self.ui.table_raw.setModel(model)
        self.setWindowTitle(self.ui.translate(self.ui.app_name) + ": " + fname)

    def action_normalize(self, column):
        df_raw = self.ui.table_raw.model().get_data()
        ds = df_raw[df_raw.columns[column]]
        df = self.ui.table_normalized.model().get_data()
        try:
            pd.to_numeric(ds)
            if len(df) == 0:
                df = pd.DataFrame()
            df[ds.name] = ds
            model = NormalizedTableModel(df, self.settings.normalization)
            self.ui.table_normalized.setModel(model)
        except ValueError:
            from ui.ui_dialog_nominal_feature import NominalFeatureDialog
            is_ok = NominalFeatureDialog.open()
            if is_ok:
                if len(df) == 0:
                    df = pd.DataFrame()
                unique_values = ds.unique()
                for uv in unique_values:
                    new_col = pd.Series(data=0, index=ds.index)
                    new_col[ds == uv] = 1
                    df[ds.name + str(uv)] = new_col
                model = NormalizedTableModel(df, self.settings.normalization)
                self.ui.table_normalized.setModel(model)

    def show_header_menu(self, point):
        column = self.ui.table_raw.horizontalHeader().logicalIndexAt(point.x())
        # show menu about the column
        menu = QtWidgets.QMenu(self)
        action = QtWidgets.QAction(self)
        action.setObjectName("actionNormalize")
        action.triggered.connect(lambda x: self.action_normalize(column))
        action.setText(self.ui.translate("Normalize"))
        menu.addAction(action)
        menu.popup(self.ui.table_raw.horizontalHeader().mapToGlobal(point))

    def _clean(self):
        for i in reversed(range(self.ui.grid_layout.count())):
            self.ui.grid_layout.itemAt(i).widget().setParent(None)

    def action_tab_layout(self):
        # tabWidget
        self.ui.tab_widget = QtWidgets.QTabWidget()
        self.ui.tab_widget.setObjectName("tab_widget")
        self.ui.tab_widget.addTab(self.ui.tab_raw, "")
        self.ui.tab_widget.addTab(self.ui.tab_normalized, "")
        self.ui.tab_widget.setTabText(self.ui.tab_widget.indexOf(self.ui.tab_raw),
                                      self.ui.translate("Raw Data"))
        self.ui.tab_widget.setTabText(self.ui.tab_widget.indexOf(self.ui.tab_normalized),
                                      self.ui.translate("Normalized Data"))
        self._clean()
        self.ui.grid_layout.addWidget(self.ui.tab_widget)

    def action_panel_layout(self):
        # splitter
        self.ui.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        # tabWidget1
        self.ui.tab_widget_1 = QtWidgets.QTabWidget()
        self.ui.tab_widget_1.setObjectName("tab_widget_1")
        self.ui.tab_widget_1.addTab(self.ui.tab_raw, "")
        self.ui.tab_widget_1.setTabText(self.ui.tab_widget_1.indexOf(self.ui.tab_raw),
                                        self.ui.translate("Raw Data"))
        # tabWidget2
        self.ui.tab_widget_2 = QtWidgets.QTabWidget(self.ui.central_widget)
        self.ui.tab_widget_2.setObjectName("tab_widget_2")
        self.ui.tab_widget_2.addTab(self.ui.tab_normalized, "")
        self.ui.tab_widget_2.setTabText(self.ui.tab_widget_2.indexOf(self.ui.tab_normalized),
                                        self.ui.translate("Normalized Data"))
        self.ui.splitter.addWidget(self.ui.tab_widget_1)
        self.ui.splitter.addWidget(self.ui.tab_widget_2)
        # add to splitter
        self._clean()
        self.ui.grid_layout.addWidget(self.ui.splitter)

    def action_exit(self):
        sys.exit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = EctMainWindow()
    window.show()
    sys.exit(app.exec_())
