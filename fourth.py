from PyQt5 import QtCore, QtGui, QtWidgets
from capy import Ui_Dialog23

class Ui_okkk(object):
    def letsstart(self):
        self.window__ = QtWidgets.QDialog()
        self.ui = Ui_Dialog23()
        self.ui.setupUi(self.window__)
        self.window__.show()
    def setupUi(self, okkk):
        okkk.setObjectName("okkk")
        okkk.resize(450, 450)
        okkk.setMinimumSize(QtCore.QSize(450, 450))
        okkk.setMaximumSize(QtCore.QSize(450, 450))
        okkk.setToolTipDuration(-1)
        okkk.setStyleSheet("background-color: rgb(208, 239, 255)")
        self.pushButton = QtWidgets.QPushButton(okkk, clicked = lambda: self.letsstart())
        self.pushButton.setGeometry(QtCore.QRect(110, 240, 241, 121))
        self.pushButton.setStyleSheet("background-color: rgb(137, 220, 255)")
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(okkk)
        self.listWidget.setGeometry(QtCore.QRect(110, 170, 241, 41))
        self.listWidget.setStyleSheet("background-color: rgb(194, 236, 255)")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)

        self.retranslateUi(okkk)
        QtCore.QMetaObject.connectSlotsByName(okkk)

    def retranslateUi(self, okkk):
        _translate = QtCore.QCoreApplication.translate
        okkk.setWindowTitle(_translate("okkk", "Dialog"))
        self.pushButton.setText(_translate("okkk", "ОК!"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("okkk", "тогда у меня есть кое-что другое"))
        self.listWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    okkk = QtWidgets.QDialog()
    ui = Ui_okkk()
    ui.setupUi(okkk)
    okkk.show()
    sys.exit(app.exec_())
