# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TT_Layout1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(722, 591))
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 110, 331, 431))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 491, 41))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(350, 60, 20, 481))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 50, 701, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(390, 360, 291, 181))
        self.calendarWidget.setObjectName("calendarWidget")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(370, 340, 341, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 70, 171, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 70, 141, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 140, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(550, 100, 121, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 100, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.lineEdit.textEdited['QString'].connect(self.listWidget.update)
        self.lineEdit.textEdited['QString'].connect(self.pushButton.update)
        self.comboBox.currentTextChanged['QString'].connect(self.pushButton.update)
        self.comboBox.objectNameChanged['QString'].connect(self.listWidget.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Teacher\'s List"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "as"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "asd"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "asd"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "a"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "dfsgretubrty"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "gy"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "ctv"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "hbe"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "rcg"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "w5v"))
        item = self.listWidget.item(10)
        item.setText(_translate("MainWindow", "ertg"))
        item = self.listWidget.item(11)
        item.setText(_translate("MainWindow", "w ret"))
        item = self.listWidget.item(12)
        item.setText(_translate("MainWindow", "gcre"))
        item = self.listWidget.item(13)
        item.setText(_translate("MainWindow", "thgvr"))
        item = self.listWidget.item(14)
        item.setText(_translate("MainWindow", "eth"))
        item = self.listWidget.item(15)
        item.setText(_translate("MainWindow", "vwr5y"))
        item = self.listWidget.item(16)
        item.setText(_translate("MainWindow", "456y356y w5re5tyvr5t6yu e"))
        item = self.listWidget.item(17)
        item.setText(_translate("MainWindow", "4ry"))
        item = self.listWidget.item(18)
        item.setText(_translate("MainWindow", "rt"))
        item = self.listWidget.item(19)
        item.setText(_translate("MainWindow", "yv "))
        item = self.listWidget.item(20)
        item.setText(_translate("MainWindow", "rwth y"))
        item = self.listWidget.item(21)
        item.setText(_translate("MainWindow", "wryv"))
        item = self.listWidget.item(22)
        item.setText(_translate("MainWindow", "ok bye"))
        item = self.listWidget.item(23)
        item.setText(_translate("MainWindow", "d"))
        item = self.listWidget.item(24)
        item.setText(_translate("MainWindow", "f"))
        item = self.listWidget.item(25)
        item.setText(_translate("MainWindow", "g"))
        item = self.listWidget.item(26)
        item.setText(_translate("MainWindow", "h"))
        item = self.listWidget.item(27)
        item.setText(_translate("MainWindow", "j"))
        item = self.listWidget.item(28)
        item.setText(_translate("MainWindow", "k"))
        item = self.listWidget.item(29)
        item.setText(_translate("MainWindow", "l"))
        item = self.listWidget.item(30)
        item.setText(_translate("MainWindow", "fghsfghdsfg"))
        item = self.listWidget.item(31)
        item.setText(_translate("MainWindow", "dgh"))
        item = self.listWidget.item(32)
        item.setText(_translate("MainWindow", "fg"))
        item = self.listWidget.item(33)
        item.setText(_translate("MainWindow", "h"))
        item = self.listWidget.item(34)
        item.setText(_translate("MainWindow", "ghs"))
        item = self.listWidget.item(35)
        item.setText(_translate("MainWindow", "fht ety"))
        item = self.listWidget.item(36)
        item.setText(_translate("MainWindow", "gvwergtb"))
        item = self.listWidget.item(37)
        item.setText(_translate("MainWindow", "vwrt"))
        item = self.listWidget.item(38)
        item.setText(_translate("MainWindow", "vywtry"))
        item = self.listWidget.item(39)
        item.setText(_translate("MainWindow", "fw"))
        item = self.listWidget.item(40)
        item.setText(_translate("MainWindow", "etgv"))
        item = self.listWidget.item(41)
        item.setText(_translate("MainWindow", "g"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#25c175;\">TEACHER LIST</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#54dd95;\">Teacher Names</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#39db80;\">Refined search</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.comboBox.setItemText(0, _translate("MainWindow", "SUBJECT"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Math"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Physics"))
        self.comboBox.setItemText(3, _translate("MainWindow", "P.E"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Chemistry"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Music"))
        self.comboBox.setItemText(6, _translate("MainWindow", "History"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Geography"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Civics"))
        self.comboBox.setItemText(9, _translate("MainWindow", "L.S"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Others"))
        self.lineEdit.setText(_translate("MainWindow", "Search Teacher..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

