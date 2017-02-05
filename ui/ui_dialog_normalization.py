# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test3.ui'
#
# Created: Thu Dec 15 00:49:06 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from normalization import Normalization


class NormalizationDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(NormalizationDialog, self).__init__(parent)
        self.mink = False
        self.parent = parent
        self.setObjectName("Dialog")
        self.resize(329, 161)
        self.grid_layout_2 = QtWidgets.QGridLayout(self)
        self.grid_layout_2.setObjectName("grid_layout_2")
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setObjectName("grid_layout")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("vertical_layout")

        # info
        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setObjectName("label")
        self.vertical_layout.addWidget(self.label_1)

        # disable
        self.horizontal_layout_3 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_3.setObjectName("horizontal_layout_3")
        self.radio_button = QtWidgets.QRadioButton(self)
        self.radio_button.setObjectName("label_4")
        self.radio_button.setChecked(True)
        self.radio_button.toggled.connect(self.disable)
        self.horizontal_layout_3.addWidget(self.radio_button)
        spacer_item3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_3.addItem(spacer_item3)
        self.vertical_layout.addLayout(self.horizontal_layout_3)

        # center
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.horizontal_layout.addWidget(self.label_2)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout.addItem(spacer_item)
        self.combo_box_1 = QtWidgets.QComboBox(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.combo_box_1.sizePolicy().hasHeightForWidth())
        self.combo_box_1.setSizePolicy(size_policy)
        self.combo_box_1.setMinimumSize(QtCore.QSize(150, 0))
        self.combo_box_1.setMaximumSize(QtCore.QSize(150, 16777215))
        self.combo_box_1.setObjectName("combo_box_1")
        self.combo_box_1.currentIndexChanged.connect(self.cbox_1_handler)
        self.horizontal_layout.addWidget(self.combo_box_1)
        self.vertical_layout.addLayout(self.horizontal_layout)

        # text edit for minkowski power
        self.horizontal_layout_4 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_4.setObjectName("horizontal_layout_4")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setObjectName("label_4")
        self.horizontal_layout_4.addWidget(self.label_4)
        spacer_item_3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_4.addItem(spacer_item_3)
        self.text_box_1 = QtWidgets.QLineEdit(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.text_box_1.sizePolicy().hasHeightForWidth())
        self.text_box_1.setSizePolicy(size_policy)
        self.text_box_1.setMinimumSize(QtCore.QSize(150, 0))
        self.text_box_1.setMaximumSize(QtCore.QSize(150, 16777215))
        self.text_box_1.setObjectName("text_box_1")
        self.horizontal_layout_4.addWidget(self.text_box_1)
        self.vertical_layout.addLayout(self.horizontal_layout_4)

        # range
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2.setObjectName("horizontal_layout_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.horizontal_layout_2.addWidget(self.label_3)
        spacer_item_1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_2.addItem(spacer_item_1)
        self.combo_box_2 = QtWidgets.QComboBox(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.combo_box_2.sizePolicy().hasHeightForWidth())
        self.combo_box_2.setSizePolicy(size_policy)
        self.combo_box_2.setMinimumSize(QtCore.QSize(150, 0))
        self.combo_box_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.combo_box_2.setObjectName("combo_box_2")
        self.horizontal_layout_2.addWidget(self.combo_box_2)
        self.vertical_layout.addLayout(self.horizontal_layout_2)
        spacer_item_2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout.addItem(spacer_item_2)

        # buttons
        self.button_box = QtWidgets.QDialogButtonBox(self)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.vertical_layout.addWidget(self.button_box)
        self.grid_layout.addLayout(self.vertical_layout, 0, 0, 1, 1)
        self.grid_layout_2.addLayout(self.grid_layout, 0, 0, 1, 1)

        self.disable()
        self.retranslateUi(self)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.set_settings()

    def accept(self):
        try:
            if self.mink:
                float(self.text_box_1.text())
            QtWidgets.QDialog.accept(self)
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Please, enter proper power (float value)")
            msg.setWindowTitle("Wrong power value")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

    def cbox_1_handler(self):
        self.mink = False
        if Normalization.Center.get(self.combo_box_1.currentText()) == Normalization.Center.MINKOWSKI_CENTER:
            self.mink = True
        self.disable()

    def set_settings(self):
        norm = self.parent.settings.normalization
        self.radio_button.setChecked(not norm.enabled)
        self.combo_box_1.setCurrentText(norm.center_type.name)
        self.combo_box_2.setCurrentText(norm.range_type.name)
        self.text_box_1.setText(str(norm.p))

    def disable(self):
        state = self.radio_button.isChecked()
        self.label_2.setDisabled(state)
        self.label_3.setDisabled(state)
        self.label_4.setDisabled(state)
        self.combo_box_1.setDisabled(state)
        self.combo_box_2.setDisabled(state)
        self.text_box_1.setDisabled(state)
        if not self.mink:
            self.label_4.setDisabled(True)
            self.text_box_1.setDisabled(True)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_1.setText(_translate("Dialog", "Please, specify normalization settings:"))
        self.label_2.setText(_translate("Dialog", "Center:"))
        self.label_3.setText(_translate("Dialog", "Range:"))
        self.label_4.setText(_translate("Dialog", "Minkowski Power:"))
        self.radio_button.setText(_translate("Dialog", "Normalization disabled"))
        self.combo_box_1.addItems([x.name for x in Normalization.Center.all()])
        self.combo_box_2.addItems([x.name for x in Normalization.Range.all()])

    def get_result(self):
        center = Normalization.Center.get(self.combo_box_1.currentText())
        range = Normalization.Range.get(self.combo_box_2.currentText())
        p = None
        if self.mink:
            p = float(self.text_box_1.text())
        return Normalization(center, range, not self.radio_button.isChecked(), p)

    @staticmethod
    def open(parent):
        dialog = NormalizationDialog(parent)
        result = dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            return dialog.get_result()
        else:
            return False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = NormalizationDialog(None)
    ui.open()
    exit()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
