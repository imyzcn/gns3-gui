# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/noplay/code/gns3/gns3-gui/gns3/ui/new_server_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewServerDialog(object):
    def setupUi(self, NewServerDialog):
        NewServerDialog.setObjectName("NewServerDialog")
        NewServerDialog.resize(394, 228)
        self.formLayout = QtWidgets.QFormLayout(NewServerDialog)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.uiServerProtocolLabel = QtWidgets.QLabel(NewServerDialog)
        self.uiServerProtocolLabel.setObjectName("uiServerProtocolLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.uiServerProtocolLabel)
        self.uiServerProtocolComboBox = QtWidgets.QComboBox(NewServerDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiServerProtocolComboBox.sizePolicy().hasHeightForWidth())
        self.uiServerProtocolComboBox.setSizePolicy(sizePolicy)
        self.uiServerProtocolComboBox.setObjectName("uiServerProtocolComboBox")
        self.uiServerProtocolComboBox.addItem("")
        self.uiServerProtocolComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uiServerProtocolComboBox)
        self.uiServerHostLabel = QtWidgets.QLabel(NewServerDialog)
        self.uiServerHostLabel.setObjectName("uiServerHostLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.uiServerHostLabel)
        self.uiServerHostLineEdit = QtWidgets.QLineEdit(NewServerDialog)
        self.uiServerHostLineEdit.setObjectName("uiServerHostLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.uiServerHostLineEdit)
        self.uiServerPortLabel = QtWidgets.QLabel(NewServerDialog)
        self.uiServerPortLabel.setObjectName("uiServerPortLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.uiServerPortLabel)
        self.uiServerPortSpinBox = QtWidgets.QSpinBox(NewServerDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiServerPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiServerPortSpinBox.setSizePolicy(sizePolicy)
        self.uiServerPortSpinBox.setSuffix(" TCP")
        self.uiServerPortSpinBox.setMaximum(65535)
        self.uiServerPortSpinBox.setProperty("value", 3080)
        self.uiServerPortSpinBox.setObjectName("uiServerPortSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.uiServerPortSpinBox)
        self.uiServerUserLabel = QtWidgets.QLabel(NewServerDialog)
        self.uiServerUserLabel.setObjectName("uiServerUserLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.uiServerUserLabel)
        self.uiServerUserLineEdit = QtWidgets.QLineEdit(NewServerDialog)
        self.uiServerUserLineEdit.setToolTip("")
        self.uiServerUserLineEdit.setObjectName("uiServerUserLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.uiServerUserLineEdit)
        self.uiServerPasswordLabel = QtWidgets.QLabel(NewServerDialog)
        self.uiServerPasswordLabel.setObjectName("uiServerPasswordLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.uiServerPasswordLabel)
        self.uiServerPasswordLineEdit = QtWidgets.QLineEdit(NewServerDialog)
        self.uiServerPasswordLineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.uiServerPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.uiServerPasswordLineEdit.setObjectName("uiServerPasswordLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.uiServerPasswordLineEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewServerDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)
        self.label = QtWidgets.QLabel(NewServerDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label)

        self.retranslateUi(NewServerDialog)
        self.buttonBox.accepted.connect(NewServerDialog.accept)
        self.buttonBox.rejected.connect(NewServerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewServerDialog)

    def retranslateUi(self, NewServerDialog):
        _translate = QtCore.QCoreApplication.translate
        NewServerDialog.setWindowTitle(_translate("NewServerDialog", "New server"))
        self.uiServerProtocolLabel.setText(_translate("NewServerDialog", "Protocol:"))
        self.uiServerProtocolComboBox.setCurrentText(_translate("NewServerDialog", "HTTP"))
        self.uiServerProtocolComboBox.setItemText(0, _translate("NewServerDialog", "HTTP"))
        self.uiServerProtocolComboBox.setItemText(1, _translate("NewServerDialog", "HTTPS"))
        self.uiServerHostLabel.setText(_translate("NewServerDialog", "Host:"))
        self.uiServerHostLineEdit.setText(_translate("NewServerDialog", "192.168.56.101"))
        self.uiServerPortLabel.setText(_translate("NewServerDialog", "Port:"))
        self.uiServerUserLabel.setText(_translate("NewServerDialog", "User:"))
        self.uiServerPasswordLabel.setText(_translate("NewServerDialog", "Password:"))
        self.label.setText(_translate("NewServerDialog", "Leave blank for no password."))

