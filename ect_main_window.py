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

    def show_header_menu(self, point, table):
        if table is None:
            return
        column = table.horizontalHeader().logicalIndexAt(point.x())
        table_model = table.model()
        # show menu about the column
        menu = QtWidgets.QMenu(self)
        if isinstance(table_model, RawTableModel):
            action_norm = QtWidgets.QAction(self)
            action_norm.setObjectName("actionNormalize")
            action_norm.triggered.connect(lambda x: self.action_normalize(column))
            action_norm.setText(self.ui.translate("Normalize"))
            menu.addAction(action_norm)
        if isinstance(table_model, NormalizedTableModel):
            action_del = QtWidgets.QAction(self)
            action_del.setObjectName("actionDelete")
            action_del.triggered.connect(lambda x: self.action_delete(column))
            action_del.setText(self.ui.translate("Delete"))
            menu.addAction(action_del)
            if column + 1 == table.model().columnCount():
                action_del.setDisabled(True)

        action_hist = QtWidgets.QAction(self)
        action_hist.setObjectName("actionHistogram")
        action_hist.triggered.connect(lambda x: self.action_hist(table, column))
        action_hist.setText(self.ui.translate("Histogram"))
        if column + 1 == table.model().columnCount():
            action_hist.setDisabled(True)
        menu.addAction(action_hist)
        menu.popup(table.horizontalHeader().mapToGlobal(point))

    def action_hist(self, table, column):
        import numpy as np
        import matplotlib.mlab as mlab
        import matplotlib.pyplot as plt

        x = table.model().get_data()
        x = x[x.columns[column]]
        print(x)
        n, bins, patches = plt.hist(x, 50, normed=0, facecolor='green', alpha=0.95)

        plt.xlabel('Values')
        plt.ylabel('Count')

        plt.title('$\mathrm{{Histogram\ of\ {:s}:}}\ \mu={:.2f},\ \sigma={:.2f}$'.format(x.name, x.mean(), x.std()))
        plt.grid(True)
        plt.show()

    def _clean(self):
        for i in reversed(range(self.ui.grid_layout.count())):
            self.ui.grid_layout.itemAt(i).widget().setParent(None)

    def action_delete(self, column):
        df = self.ui.table_normalized.model().get_data()
        df.drop(df.columns[[column]], axis=1, inplace=True)
        model = NormalizedTableModel(df, self.settings.normalization)
        self.ui.table_normalized.setModel(model)

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

    def action_clustering(self):
        from ui.ui_dialog_run_clustering import RunClusteringDialog
        dialog = RunClusteringDialog.open(self)
        return
        from eclustering.pattern_init import a_pattern_init
        from eclustering.a_ward import a_ward
        data = self.ui.table_normalized.model().get_data()
        data_m = data.as_matrix()
        labels, centroids = a_pattern_init(data_m)
        labels = a_ward(data_m, K_star=4, labels=labels)
        data['Cluster#'] = labels
        model = NormalizedTableModel(data, self.settings.normalization)
        self.ui.table_normalized.setModel(model)

    def action_a_ward(self):
        print(self.ui.table_normalized.model().get_data())
        from eclustering.pattern_init import a_pattern_init
        from eclustering.a_ward import a_ward
        data = self.ui.table_normalized.model().get_data()
        data_m = data.as_matrix()
        labels, centroids = a_pattern_init(data_m)
        labels = a_ward(data_m, K_star=4, labels=labels)
        m = self.ui.table_normalized.model()
        m.set_cluster(labels)
        self.ui.table_normalized.setModel(m)
        # return
        # data['Cluster#'] = labels
        # model = NormalizedTableModel(data, self.settings.normalization)
        # self.ui.table_normalized.setModel(model)

    def action_exit(self):
        sys.exit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = EctMainWindow()
    window.show()
    sys.exit(app.exec_())
