<<<<<<< HEAD
from PyQt5 import QtGui
from PyQt5.QtGui import QColor

__author__ = 'eremeykin'
import pandas as pd
from PyQt5 import QtCore
=======
__author__ = 'eremeykin'
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
>>>>>>> temp-branch


class PandasTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data=pd.DataFrame(), *args):
        super(PandasTableModel, self).__init__()
        self.datatable = data
        self.layout = 'Panel'  # TODO Delete?
        self.markers = dict()
        if self.columnCount() == 0:
            self.datatable = pd.DataFrame()

    def get_actual_data(self):
        return self.datatable

    def get_by_marker(self, marker):
        return self.get_actual_data()[self.markers[marker]]

    def set_marker(self, column_name, marker):
        self.markers[marker] = column_name

    def del_all_markers(self):
        self.markers = dict()

    def del_marker(self, marker):
        try:
            del self.markers[marker]
        except KeyError:
            pass

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
<<<<<<< HEAD
        i = index.row()
        j = index.column()
        if role == QtCore.Qt.DisplayRole:
            return '{0}'.format(self.datatable.iat[i, j])
        if role == QtCore.Qt.BackgroundColorRole:
            return self.color_injection(i, j)
        else:
            return QtCore.QVariant()

    def color_injection(self, i, j):
        return QtCore.QVariant()

=======
        if role == QtCore.Qt.DisplayRole:
            i = index.row()
            j = index.column()
            return '{0}'.format(self.datatable.iat[i, j])
        else:
            return QtCore.QVariant()

>>>>>>> temp-branch
    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            c_name = self.datatable.columns.values[col]
            new_name = c_name
            for marker in self.markers.keys():
                if self.markers[marker] == col:
                    new_name += " (" + marker + ")"
            return QtCore.QVariant(new_name)
        if orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(str(self.datatable.index.values[col]))
        return QtCore.QVariant()

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled

    def get_data(self):
        return self.datatable


class NormalizedTableModel(PandasTableModel):
    def __init__(self, data, normalization, labels=None, *args):
        super(NormalizedTableModel, self).__init__(data=data)
        self.norm = normalization
        self.norm_data = self.norm.apply(self.datatable)
        if labels is None:
            self.cluster_column = pd.Series('?', index=self.norm_data.index, name='Cluster#')
        else:
            self.cluster_column = pd.Series(labels, index=self.norm_data.index, name='Cluster#')

    def get_actual_data(self):
        nd = self.norm_data.copy()
<<<<<<< HEAD
        nd['Cluster#'] = self.cluster_column
=======
        nd['Cluster#'] =self.cluster_column
>>>>>>> temp-branch
        return nd

    def update(self, dataIn):
        self.datatable = dataIn
        self.norm_data = self.norm.apply(self.datatable)

    def set_cluster(self, labels):
        self.layoutAboutToBeChanged.emit()
        self.cluster_column = pd.Series(labels, name=self.cluster_column.name)
        self.layoutChanged.emit()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            i = index.row()
            j = index.column()
            if j == super().columnCount():
                return '{0}'.format(self.cluster_column.iat[i])
            return '{0}'.format(self.norm_data.iat[i, j])
        else:
            return QtCore.QVariant()

    def headerData(self, col, orientation, role):
        if col == super().columnCount() and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            new_name = self.cluster_column.name
            for marker in self.markers.keys():
                if self.markers[marker] == col:
                    new_name += " (" + marker + ")"
            return new_name
        return super().headerData(col, orientation, role)

    def set_norm(self, normalization):
        self.norm = normalization
        self.update(self.datatable)

    def get_norm(self):
        return self.norm

<<<<<<< HEAD
=======

>>>>>>> temp-branch
    def get_data(self):
        return self.norm_data

    def columnCount(self, parent=QtCore.QModelIndex()):
        super_count = super().columnCount(parent=QtCore.QModelIndex())
        if super_count != 0:
            return super_count + 1
        else:
            return super_count


class RawTableModel(PandasTableModel):
    def __init__(self, data=pd.DataFrame()):
        super(RawTableModel, self).__init__(data=data)


class WeightTableModel(PandasTableModel):
    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        c = list(self.datatable)
<<<<<<< HEAD
        try:
            self.datatable.set_value(index='W', col=c[index.column()], value=value)
        except:
            print("Error converting to float")

class ReportTableModel(PandasTableModel):
    def __init__(self, counts, means, data=pd.DataFrame(), *args):
        super(ReportTableModel, self).__init__(data)
        self.m = means
        self.counts = counts
        self.threshold = 30

    def rowCount(self, parent=QtCore.QModelIndex()):
        return self.datatable.shape[0] + 1

    def columnCount(self, parent=QtCore.QModelIndex()):
        print(self.datatable.shape[1] + 1)
        return self.datatable.shape[1] + 1

    def data(self, index, role=QtCore.Qt.DisplayRole):
        i = index.row()
        j = index.column()
        if role == QtCore.Qt.DisplayRole:
            if j == self.columnCount() - 1 and i == self.rowCount() - 1:
                return '{0}'.format(sum(self.counts))
            if j == self.columnCount() - 1:
                return '{0}'.format(self.counts[i])
            if i == self.rowCount() - 1:
                return '{0:.3f}'.format(self.m[j])
            return '{0:.3f}'.format(self.datatable.iat[i, j])
        if role == QtCore.Qt.BackgroundColorRole:
            return self.color_injection(i, j)
        else:
            return QtCore.QVariant()

    def color_injection(self, i, j):
        try:
            if (self.datatable.iat[i, j] - self.m[j])*100/self.m[j] > self.threshold:
                return QtCore.QVariant(QColor(255, 90, 90))
            if (self.m[j] - self.datatable.iat[i, j])*100/self.m[j] > self.threshold :
                return QtCore.QVariant(QtGui.QColor(0, 191, 255))
            else:
                return QtCore.QVariant()
        except:
            return QtCore.QVariant()

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            if col == self.columnCount() - 1:
                return QtCore.QVariant("Entities")
            c_name = self.datatable.columns.values[col]
            new_name = c_name
            return QtCore.QVariant(new_name)
        if orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            if col == self.rowCount() - 1:
                return QtCore.QVariant("Mean")
            return QtCore.QVariant(str(self.datatable.index.values[col]))
        return QtCore.QVariant()
=======
        self.datatable.set_value(index='W', col=c[index.column()], value=value)
>>>>>>> temp-branch
