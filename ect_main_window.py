# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Dec 10 14:49:23 2016
# by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!
import time
from threading import Thread

import matplotlib
import pandas as pd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from clustering.agglomerative.pattern_initialization.ap_init import APInit
from clustering.agglomerative.pattern_initialization.ap_init_pb_matlab import APInitPBMatlabCompatible
from clustering.agglomerative.a_ward import AWard
from clustering.agglomerative.a_ward_pb import AWardPB
from clustering.agglomerative.ik_means.ik_means import IKMeans
from clustering.agglomerative.utils.matlab_compatible import IMWKMeansClusterStructureMatlabCompatible

from clustering.divisive.depddp import DEPDDP
from clustering.divisive.bikm_r import BiKMeansR
# from clustering.agglomerative.a_ward_p_beta import a_ward_p_beta

# from clustering.agglomerative.a_ward import a_ward
# from clustering.agglomerative.pattern_initialization import anomalous_cluster
# from clustering.agglomerative.pattern_initialization import anomalous_cluster_p_beta
# from clustering.divisive.BiKM_R import BiKM_R
# from clustering.divisive.dePDDP import dePDDP
from report import Report
from settings import Settings
from table_models import RawTableModel, NormalizedTableModel
from ui.PlotInfo import PlotInfo
from ui.kovaleva_dialog import KovalevaGeneratorDialog
from ui.progress import ProgressDialog
from ui.rand_dir_dialog import RandDirDialog
from ui.ui_cluster_table import UiDialogCLusterTable
from ui.ui_dialog_normalization import NormalizationDialog
from ui.ui_dialog_report import UiDialogReport
from ui.ui_dialog_run_clustering import RunClusteringDialog
from ui.ui_ect_main_window import Ui_EctMainWindow

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle
from generators.kovaleva import kovaleva


class EctMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(EctMainWindow, self).__init__()
        self.settings = Settings()
        self.ui = Ui_EctMainWindow()
        self.ui.setupUi(self)
        self.plot_info = PlotInfo([self.ui.table_normalized.model(), self.ui.table_raw.model()])
        self.in_progress = False

    def action_normalize_settings(self):
        result = NormalizationDialog.open(self)
        if result:
            self.settings.normalization = result
            m = self.ui.table_normalized.model()
            m.set_norm(result)
            self.ui.table_normalized.setModel(m)

    def _load(self, name):
        try:
            data = pd.read_csv(name)
            model = RawTableModel(data)
            self.ui.table_raw.setModel(model)
            self.setWindowTitle(self.ui.translate(self.ui.app_name) + ": " + name)
        except pd.io.common.CParserError:
            # infoBox = QMessageBox()
            # infoBox.setIcon(QMessageBox.Information)
            # infoBox.setText("Error")
            # infoBox.setInformativeText("An error occurred while loading the file. \nPlease, check file format. ")
            # infoBox.setWindowTitle("Opening error")
            # infoBox.setDetailedText(str(traceback.format_exc()))
            # infoBox.setStandardButtons(QMessageBox.Ok)
            # infoBox.resize(500,100)
            # infoBox.exec_()
            # QMessageBox.setDetailedText("Test")
            mb = QMessageBox.question(self, 'Error',
                                      'An error occured while loading the file.\nPlease, check file format.',
                                      QMessageBox.Ok)

    class ProgressThread(Thread):
        def __init__(self):
            super(EctMainWindow.ProgressThread, self).__init__()
            self.__stoped = False
            self.dialog = ProgressDialog(None)
            self.dialog.setupUi(None)

        def stop(self):
            self.__stoped = True

        def run(self):
            self.dialog.show()
            while not self.__stoped:
                pass
            self.dialog.hide()

    def action_open(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self.ui, 'Open file', '\home')[0]
        if not fname:
            return
        thread = EctMainWindow.ProgressThread()
        thread.start()
        self._load(fname)
        thread.stop()

    def action_generate(self):
        kgd = KovalevaGeneratorDialog.open(self)
        if kgd:
            data, labels = kovaleva(*kgd)
            # data = kovaleva(*kgd)
            # data = np.column_stack(data)
            fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Save new data as', 'gen_data.csv')[0]
            np.savetxt(fileName, data, delimiter=',', comments='',
                       header=','.join(['F' + str(i) for i in range(data.shape[1])]))
            self._load(fileName)

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
                    df[ds.name + str('[' + uv + ']')] = new_col
                    if len(unique_values) == 2:
                        break
                model = NormalizedTableModel(df, self.settings.normalization)
                self.ui.table_normalized.setModel(model)

    def double_clicked_raw(self, column):
        self.action_normalize(column)

    def double_clicked_norm(self, column):
        self.action_delete(self.ui.table_normalized, column)

    def show_header_menu(self, point, table):
        if table is None:
            return
        column = table.horizontalHeader().logicalIndexAt(point.x())
        table_model = table.model()
        menu = QtWidgets.QMenu(self)
        if isinstance(table_model, RawTableModel):
            action_norm = QtWidgets.QAction(self)
            action_norm.setObjectName("actionNormalize")
            action_norm.triggered.connect(lambda x: self.action_normalize(column))
            action_norm.setText(self.ui.translate("Normalize"))
            menu.addAction(action_norm)

        action_del = QtWidgets.QAction(self)
        action_del.setObjectName("actionDelete")
        action_del.triggered.connect(lambda x: self.action_delete(table, column))
        action_del.setText(self.ui.translate("Delete"))
        menu.addAction(action_del)
        if column + 1 == table.model().columnCount():
            action_del.setDisabled(True)

        action_hist = QtWidgets.QAction(self)
        action_hist.setObjectName("actionHistogram")
        action_hist.triggered.connect(lambda x: self.action_hist(table, column))
        action_hist.setText(self.ui.translate("Histogram"))

        menu.addAction(action_hist)

        menu_set = QtWidgets.QMenu(menu)
        menu_set.setTitle("Set")

        marker = 'X'
        action_set_as = QtWidgets.QAction(self)
        action_set_as.setObjectName("actionSetAs" + marker)
        action_set_as.triggered.connect(lambda x: self.action_set_as(table, column, marker='X'))
        action_set_as.setText(self.ui.translate("as " + marker))
        menu_set.addAction(action_set_as)
        marker = 'Y'
        action_set_as = QtWidgets.QAction(self)
        action_set_as.setObjectName("actionSetAs" + marker)
        action_set_as.triggered.connect(lambda x: self.action_set_as(table, column, marker='Y'))
        action_set_as.setText(self.ui.translate("as " + marker))
        menu_set.addAction(action_set_as)
        marker = 'C'
        action_set_as = QtWidgets.QAction(self)
        action_set_as.setObjectName("actionSetAs" + marker)
        action_set_as.triggered.connect(lambda x: self.action_set_as(table, column, marker='C'))
        action_set_as.setText(self.ui.translate("as " + marker))
        menu_set.addAction(action_set_as)

        action_set_as_index = QtWidgets.QAction(self)
        action_set_as_index.setObjectName("actionSetAsIndex")
        action_set_as_index.triggered.connect(lambda x: self.action_set_as_index(column))
        action_set_as_index.setText(self.ui.translate("as Index"))
        menu_set.addAction(action_set_as_index)

        menu.addMenu(menu_set)

        if column + 1 == table.model().columnCount():
            action_hist.setDisabled(True)
        menu.popup(table.horizontalHeader().mapToGlobal(point))

    def action_report(self):
        report = Report.get_report()
        ui = UiDialogReport(self, str(report))
        ui.open()
        ui.showMaximized()
        ctabel = UiDialogCLusterTable(self, report)
        ctabel.open()

    def action_set_as_index(self, column):
        table = self.ui.table_raw
        header = table.verticalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        model = table.model()
        data = model.get_data()
        new_index = data[data.columns[column]]
        self.action_delete(table, column)
        model.datatable.index = new_index

    def action_set_as(self, table, column, marker):
        self.plot_info.set(table, column, marker)

    def delete_markers(self):
        self.plot_info.delete_markers()

    def plot_by_markers(self):
        clist = ['b', 'g', 'r', 'c', 'm', 'y', 'k', ]
        colors = cycle(clist)
        markers = cycle(['o', 'p', '.', 's', '8', 'h'])
        size = cycle([75, 150, 125, 100])

        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.axis('equal')

        cdata = self.plot_info.get('C')
        if cdata is not None:
            for l in np.unique(cdata):
                s = next(size)
                m = next(markers)
                c = next(colors)
                plt.scatter(self.plot_info.get('X')[cdata == l], self.plot_info.get('Y')[cdata == l], s=s, marker=m,
                            color=c)
        else:
            plt.scatter(self.plot_info.get('X'), self.plot_info.get('Y'), s=150, marker='o', color='b')
        # show_num = True
        # if show_num:
        #     for i, j in data:
        #         label = labels[ind]
        #         ind += 1
        #         ax.annotate(str(label), xy=(i, j), xytext=(4, 3), textcoords='offset points')
        plt.grid(True)
        plt.show()

    def __action_plot_svd(self, data, centroids=None):
        if data is None or len(data) == 0:
            QMessageBox.question(self, 'Nothing to plot',
                                 'There is no data to plot.',
                                 QMessageBox.Ok)
        U, mu, Vt = np.linalg.svd(data.as_matrix())
        clist = ['b', 'g', 'r', 'c', 'm', 'y', 'k', ]
        colors = cycle(clist)
        markers = cycle(['o', 'p', '.', 's', '8', 'h'])
        size = cycle([75, 150, 125, 100])

        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.axis('equal')

        cdata = self.plot_info.get('C')
        if cdata is None:
            cdata = self.ui.table_normalized.model().cluster_column
            if len(cdata) < 1: cdata = None
        if cdata is not None:
            for l in np.unique(cdata):
                s = next(size)
                m = next(markers)
                c = next(colors)
                plt.scatter(U[:, 0][cdata == l] * np.sqrt(mu[0]), U[:, 1][cdata == l] * np.sqrt(mu[1]), s=s, marker=m,
                            color=c)
        else:
            plt.scatter(U[:, 0] * np.sqrt(mu[0]), U[:, 1] * np.sqrt(mu[1]), s=150, marker='o', color='b')
        plt.grid(True)

        colors = cycle(clist)  # reset colors
        if centroids is not None:
            for centroid in centroids:
                c = next(colors)
                c_svd = centroid.dot(Vt.T[:, 0:2]) / np.sqrt(mu[0:2])
                plt.scatter(c_svd[0], c_svd[1], s=800, marker='*', edgecolor='black', linewidth='3', facecolor=c)
                # plt.scatter(c_svd[0], c_svd[1], s=400, marker='o', color=c)
        plt.show()

    def action_plot_svd_norm(self):
        data = self.ui.table_normalized.model().get_actual_data()
        del data[data.columns[-1]]
        centroids = None
        try:
            centroids = Report.get_report().centroids
        except:
            pass
        self.__action_plot_svd(data, centroids)

    def action_plot_svd_raw(self):
        data = self.ui.table_raw.model().get_data()
        has_nominal = False
        for c in data:
            if not np.issubdtype(data[c].dtype, np.number):
                has_nominal = True
        if has_nominal:
            reply = QMessageBox.question(self, 'Nominal Feature',
                                         'There is a nominal feature(s).\n It will be ignored.',
                                         QMessageBox.Cancel, QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                data = data._get_numeric_data()
            else:
                return
        self.__action_plot_svd(data)

    def action_hist(self, table, column):
        x = table.model().get_data()
        x = x[x.columns[column]]
        n, bins, patches = plt.hist(x, 50, normed=0, facecolor='green', alpha=0.95)

        plt.xlabel('Values')
        plt.ylabel('Count')

        plt.title('$\mathrm{{Histogram\ of\ {:s}:}}\ \mu={:.2f},\ \sigma={:.2f}$'.format(x.name, x.mean(), x.std()))
        plt.grid(True)
        plt.show()

    def _clean(self):
        for i in reversed(range(self.ui.grid_layout.count())):
            self.ui.grid_layout.itemAt(i).widget().setParent(None)

    def action_delete(self, table, column):
        model = table.model()
        df = model.get_data()
        df.drop(df.columns[[column]], axis=1, inplace=True)
        if isinstance(model, NormalizedTableModel):
            model = NormalizedTableModel(df, self.settings.normalization)
            table.setModel(model)
        if isinstance(model, RawTableModel):
            model = RawTableModel(df)
            table.setModel(model)

    def action_norm_all(self):
        data = self.ui.table_raw.model().get_data()
        for i in range(len(data) - 1):
            try:
                self.action_normalize(i)
            except:
                pass

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
        data = self.ui.table_normalized.model().get_data()
        data_m = data.as_matrix()
        labels = None
        dialog_res = RunClusteringDialog.open(self)
        end = 0
        start = 0
        if not dialog_res:
            return
        report = Report.get_report()
        report.set_norm_data(data)
        report.set_data(self.ui.table_raw.model().get_data())
        report.set_norm(self.ui.table_normalized.model().get_norm())

        if dialog_res.weights is not None:
            data_m = data_m * dialog_res.weights.as_matrix()

        if dialog_res.award_criterion:
            start = time.time()
            # a_labels, centroids = anomalous_cluster(data_m)
            run_ap_init = APInit(data_m)
            run_ap_init()
            run_ik_means = IKMeans(run_ap_init.cluster_structure)
            run_ik_means()
            cs = run_ik_means.cluster_structure
            run_a_ward = AWard(cs, alpha=0.5)
            labels = run_a_ward()
            end = time.time()
            report.set_labels(labels)
            report.set_alg('anomalous clustering + A-Ward')

        if dialog_res.minimum_of_density:
            res = RandDirDialog.open(self)
            if res:
                if not res[0]:
                    start = time.time()
                    run_depddp = DEPDDP(data_m)
                    labels = run_depddp()
                    end = time.time()
                    report.set_labels(labels)
                    report.set_alg('dePDDP (Principal Direction Divisive Partitioning)')
                else:
                    start = time.time()
                    run_bikmeansr = BiKMeansR(data_m, epsilon=res[1], directions_num=res[2])
                    labels = run_bikmeansr()
                    end = time.time()
                    report.set_labels(labels)
                    report.set_alg('BiKM-R (Bisecting K-Means divisive clustering)')

        if dialog_res.n_clusters is not None:
            if dialog_res.minkowski == 2 and not dialog_res.cluster_spec_weights:
                start = time.time()
                run_ap_init = APInit(data_m)
                run_ap_init()
                run_ik_means = IKMeans(run_ap_init.cluster_structure)
                run_ik_means()
                cs = run_ik_means.cluster_structure
                run_a_ward = AWard(cs, k_star=dialog_res.n_clusters)
                labels = run_a_ward()
                end = time.time()
                report.set_labels(labels)
                report.set_alg('anomalous clustering + A-Ward')
            else:
                start = time.time()

                run_ap_init_pb = APInitPBMatlabCompatible(data_m, p=dialog_res.minkowski, beta=2)
                run_ap_init_pb()
                # change cluster structure to matlab compatible
                clusters = run_ap_init_pb.cluster_structure.clusters
                new_cluster_structure = IMWKMeansClusterStructureMatlabCompatible(data_m, p=dialog_res.minkowski, beta=2)
                new_cluster_structure.add_all_clusters(clusters)
                run_ik_means = IKMeans(new_cluster_structure)
                run_ik_means()
                cs = run_ik_means.cluster_structure
                run_a_ward_pb = AWardPB(cs, k_star=dialog_res.n_clusters)
                labels = run_a_ward_pb()
                end = time.time()
                report.set_labels(labels)
                report.set_alg('anomalous clustering + A-ward p,beta')

        if labels is not None:
            report.set_labels(labels)
            infoBox = QMessageBox()
            infoBox.setIcon(QMessageBox.Information)
            infoBox.setText("Clustering completed")
            infoBox.setInformativeText("Informative Text")
            infoBox.setWindowTitle("Notification")
            detailed_text = "Time: " + str(end - start) + "\n"
            detailed_text += "Algorithm: " + report.alg
            infoBox.setDetailedText(detailed_text)
            infoBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            infoBox.exec_()
            model = NormalizedTableModel(data, self.settings.normalization, labels)
            self.ui.table_normalized.setModel(model)
        else:
            infoBox = QMessageBox()
            infoBox.setIcon(QMessageBox.Information)
            infoBox.setText("Error")
            infoBox.setInformativeText("An error occurred")
            infoBox.setWindowTitle("An error occurred")
            infoBox.setDetailedText("No detailed info")
            infoBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            infoBox.exec_()

    def action_clear_norm(self):
        for column in reversed(range(len(self.ui.table_normalized.model().get_data().columns))):
            self.action_delete(self.ui.table_normalized, column)

    def action_exit(self):
        sys.exit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = EctMainWindow()
    window.show()
    sys.exit(app.exec_())
