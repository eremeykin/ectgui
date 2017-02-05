__author__ = 'eremeykin'
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd


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
    def __init__(self, data, normalization, *args):
        super(NormalizedTableModel, self).__init__(data=data)
        self.norm = normalization
        self.norm_data = self.norm.apply(self.datatable)

    def update(self, dataIn):
        self.datatable = dataIn
        self.norm_data = self.norm.apply(self.datatable)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            i = index.row()
            j = index.column()
            return '{0}'.format(self.norm_data.iat[i, j])
        else:
            return QtCore.QVariant()

    def set_norm(self, normalization):
        self.norm = normalization
        self.update(self.datatable)

    def get_data(self):
        return self.norm_data


class RawTableModel(PandasTableModel):
    def __init__(self, data=pd.DataFrame()):
        super(RawTableModel, self).__init__(data=data)


class WeightTableModel(PandasTableModel):
    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        c = list(self.datatable)
        self.datatable.set_value(index='W', col=c[index.column()], value=value)
