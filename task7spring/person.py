# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\milay\OneDrive\Документы\программирование(((\7taskspring\person.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_person(object):
    def setupUi(self, person):
        person.setObjectName("person")
        person.resize(450, 450)
        person.setMinimumSize(QtCore.QSize(400, 400))
        person.setMaximumSize(QtCore.QSize(450, 450))
        person.setStyleSheet("background-color: rgb(205, 240, 255)")
        self.listWidget = QtWidgets.QListWidget(person)
        self.listWidget.setGeometry(QtCore.QRect(120, 120, 211, 201))
        self.listWidget.setStyleSheet("background-color: rgb(176, 221, 255)")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)

        self.retranslateUi(person)
        QtCore.QMetaObject.connectSlotsByName(person)

    def retranslateUi(self, person):
        _translate = QtCore.QCoreApplication.translate
        person.setWindowTitle(_translate("person", "Dialog"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("person", "Целый мир от красоты,\n"
"От велика и до мала,\n"
"И напрасно ищешь ты\n"
"Отыскать ее начало.\n"
"\n"
"Что такое день иль век\n"
"Перед тем, что бесконечно?\n"
"Хоть не вечен человек,\n"
"То, что вечно,— человечно."))
        self.listWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    person = QtWidgets.QDialog()
    ui = Ui_person()
    ui.setupUi(person)
    person.show()
    sys.exit(app.exec_())
