# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deeplx.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_deeplxform(object):
    def setupUi(self, deeplxform):
        deeplxform.setObjectName("deeplxform")
        deeplxform.setWindowModality(QtCore.Qt.NonModal)
        deeplxform.resize(400, 223)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(deeplxform.sizePolicy().hasHeightForWidth())
        deeplxform.setSizePolicy(sizePolicy)
        deeplxform.setMaximumSize(QtCore.QSize(400, 300))
        self.gridLayout = QtWidgets.QGridLayout(deeplxform)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(deeplxform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 35))
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.deeplx_address = QtWidgets.QLineEdit(deeplxform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deeplx_address.sizePolicy().hasHeightForWidth())
        self.deeplx_address.setSizePolicy(sizePolicy)
        self.deeplx_address.setMinimumSize(QtCore.QSize(210, 35))
        self.deeplx_address.setObjectName("deeplx_address")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.deeplx_address)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.set_deeplx = QtWidgets.QPushButton(deeplxform)
        self.set_deeplx.setMinimumSize(QtCore.QSize(0, 35))
        self.set_deeplx.setObjectName("set_deeplx")
        self.verticalLayout_2.addWidget(self.set_deeplx)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(deeplxform)
        QtCore.QMetaObject.connectSlotsByName(deeplxform)

    def retranslateUi(self, deeplxform):
        deeplxform.setWindowTitle("DeepLX")
        self.label.setText("DeepLX_address")
        self.set_deeplx.setText("OK")
