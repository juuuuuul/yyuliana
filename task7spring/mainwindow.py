from PyQt5 import QtCore, QtGui, QtWidgets
from may import Ui_may
from person import Ui_person
from friendship import Ui_friendship
from idk import Ui_idk

class Ui_MainWindow(object):
     def openmay(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_may()
        self.ui.setupUi(self.window)
        self.window.show()
     def openperson(self):
        self.window_ = QtWidgets.QDialog()
        self.ui = Ui_person()
        self.ui.setupUi(self.window_)
        self.window_.show()
     def openfrienship(self):
        self.window__ = QtWidgets.QDialog()
        self.ui = Ui_friendship()
        self.ui.setupUi(self.window__)
        self.window__.show()
     def openidk(self):
        self.window___ = QtWidgets.QDialog()
        self.ui = Ui_idk()
        self.ui.setupUi(self.window___)
        self.window___.show()
     def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        MainWindow.setStyleSheet("background-color: rgb(205, 240, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(90, 140, 221, 41))
        self.listWidget.setStyleSheet("background-color: rgb(181, 223, 255)")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openmay())
        self.pushButton.setGeometry(QtCore.QRect(40, 210, 131, 51))
        self.pushButton.setStyleSheet("background-color:rgb(156, 201, 255)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openperson())
        self.pushButton_2.setGeometry(QtCore.QRect(220, 210, 131, 51))
        self.pushButton_2.setStyleSheet("background-color:rgb(156, 201, 255)"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openfrienship())
        self.pushButton_3.setGeometry(QtCore.QRect(40, 280, 131, 51))
        self.pushButton_3.setStyleSheet("background-color:rgb(156, 201, 255)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openidk())
        self.pushButton_4.setGeometry(QtCore.QRect(220, 280, 131, 51))
        self.pushButton_4.setStyleSheet("background-color:rgb(156, 201, 255)"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

     def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "о чём хотите прочитать стих?"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "о мае"))
        self.pushButton_2.setText(_translate("MainWindow", "о человеке"))
        self.pushButton_3.setText(_translate("MainWindow", "о дружбе"))
        self.pushButton_4.setText(_translate("MainWindow", "не определился(лась)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
