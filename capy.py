
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog23(object):
    def setupUi(self, Dialog23):
        Dialog23.setObjectName("Dialog23")
        Dialog23.resize(450, 450)
        Dialog23.setMinimumSize(QtCore.QSize(450, 450))
        Dialog23.setMaximumSize(QtCore.QSize(450, 450))
        Dialog23.setStyleSheet("background-color: rgb(208, 239, 255)\n"
"")
        self.label = QtWidgets.QLabel(Dialog23)
        self.label.setGeometry(QtCore.QRect(50, -90, 531, 621))
        self.label.setStyleSheet("background-color: rgb(208, 239, 255)\n"
"")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\milay\\OneDrive\\Документы\\программирование(((\\7\\../../../Изображения/работа/р.jpg"))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Dialog23)
        self.listWidget.setGeometry(QtCore.QRect(140, 400, 171, 41))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)

        self.retranslateUi(Dialog23)
        QtCore.QMetaObject.connectSlotsByName(Dialog23)

    def retranslateUi(self, Dialog23):
        _translate = QtCore.QCoreApplication.translate
        Dialog23.setWindowTitle(_translate("Dialog23", "Dialog"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog23", "   капибара    ٩(｡•́‿•̀｡)۶"))
        self.listWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog23 = QtWidgets.QDialog()
    ui = Ui_Dialog23()
    ui.setupUi(Dialog23)
    Dialog23.show()
    sys.exit(app.exec_())
