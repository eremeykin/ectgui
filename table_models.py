__author__ = 'eremeykin'
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np


class PandasTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data=pd.DataFrame(), *args):
        super(PandasTableModel, self).__init__()
        self.datatable = data
        self.layout = 'Panel'  # TODO Delete?
        if self.columnCount() == 0:
            self.datatable = pd.DataFrame()

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
            return '{0}'.format(self.datatable.iat[i, j])
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


class NormalizedTableModel(PandasTableModel):
    def __init__(self, data, normalization, labels=None, *args):
        super(NormalizedTableModel, self).__init__(data=data)
        self.norm = normalization
        self.norm_data = self.norm.apply(self.datatable)
        if labels is None:
            self.cluster_column = pd.Series('?', index=self.norm_data.index, name='CLUSTER #')
        else:
            self.cluster_column = pd.Series(labels, index=self.norm_data.index, name='CLUSTER #')

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
        # print(super().columnCount())
        if col == super().columnCount() and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.cluster_column.name
        return super().headerData(col, orientation, role)

    def set_norm(self, normalization):
        self.norm = normalization
        self.update(self.datatable)

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
        self.datatable.set_value(index='W', col=c[index.column()], value=value)
