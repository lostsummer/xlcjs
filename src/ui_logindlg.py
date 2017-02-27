# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logindlg.ui'
#
# Created: Mon Feb 27 15:53:36 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName(_fromUtf8("LoginDialog"))
        LoginDialog.resize(710, 564)
        self.label = QtGui.QLabel(LoginDialog)
        self.label.setGeometry(QtCore.QRect(140, 40, 431, 361))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(LoginDialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 430, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(_translate("LoginDialog", "挖深式消力池消能设计", None))
        self.label.setText(_translate("LoginDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">挖深式消力池消能设计软件</span></p><p align=\"center\"><br/><span style=\" font-size:18pt; font-weight:600;\">开发单位：广东珠荣工程设计有限公司</span></p><p align=\"center\"><br/></p><p><span style=\" font-size:14pt;\">版本信息：V1.0</span></p><p><span style=\" font-size:14pt;\">开发者：程怡 贾杰 代长贤</span></p><p><span style=\" font-size:14pt;\">地址：广州市天河区天寿路105号天寿大厦</span></p><p><span style=\" font-size:14pt;\">邮编：510610</span></p><p><span style=\" font-size:14pt;\">电话：020-38811301</span></p></body></html>", None))
        self.pushButton.setText(_translate("LoginDialog", "登陆计算", None))

