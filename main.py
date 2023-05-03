from PyQt5 import QtCore, QtGui, QtWidgets
from cat import Ui_Dialog
from fourth import Ui_okkk

class Ui_start(object):
    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def start_(self):
        self.window_ = QtWidgets.QDialog()
        self.ui = Ui_okkk()
        self.ui.setupUi(self.window_)
        self.window_.show()

    def setupUi(self, start):
        start.setObjectName("start")
        start.resize(450, 450)
        start.setMinimumSize(QtCore.QSize(450, 450))
        start.setMaximumSize(QtCore.QSize(450, 450))
        start.setStyleSheet("background-color: rgb(208, 239, 255)")
        self.centralwidget = QtWidgets.QWidget(start)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(30, 280, 171, 61))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(137, 220, 255)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.start_())
        self.pushButton_2.setGeometry(QtCore.QRect(240, 280, 171, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(137, 220, 255)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 140, 351, 61))
        self.listWidget.setStyleSheet("background-color: rgb(194, 236, 255)")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        start.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(start)
        self.statusbar.setObjectName("statusbar")
        start.setStatusBar(self.statusbar)

        self.retranslateUi(start)
        QtCore.QMetaObject.connectSlotsByName(start)

    def retranslateUi(self, start):
        _translate = QtCore.QCoreApplication.translate
        start.setWindowTitle(_translate("start", "MainWindow"))
        self.pushButton.setText(_translate("start", "ДАВАЙ"))
        self.pushButton_2.setText(_translate("start", "НЕ ХОЧУ"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("start", "                                 привет!"))
        item = self.listWidget.item(1)
        item.setText(_translate("start", "          предлагаю посмотреть на котиков"))
        self.listWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    start = QtWidgets.QMainWindow()
    ui = Ui_start()
    ui.setupUi(start)
    start.show()
    sys.exit(app.exec_())
