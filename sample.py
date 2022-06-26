# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1372, 905)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 40, 261, 23))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(400, 40, 261, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(1000, 300, 261, 23))
        self.checkBox_3.setObjectName("checkBox_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(880, 70, 456, 171))
        self.calendarWidget.setObjectName("calendarWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 70, 111, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 70, 111, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1000, 330, 121, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(880, 40, 194, 26))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 70, 231, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(510, 70, 231, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(1120, 330, 231, 25))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1372, 22))
        self.menubar.setObjectName("menubar")
        self.menuHome_Automation = QtWidgets.QMenu(self.menubar)
        self.menuHome_Automation.setObjectName("menuHome_Automation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHome_Automation.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "First Floor East Door Configs"))
        self.checkBox_2.setText(_translate("MainWindow", "First Floor North Door Configs"))
        self.checkBox_3.setText(_translate("MainWindow", "Second Floor North Door Configs"))
        self.pushButton.setText(_translate("MainWindow", "1st E Configs"))
        self.pushButton_2.setText(_translate("MainWindow", "1st N Configs"))
        self.pushButton_3.setText(_translate("MainWindow", "2nd N Configs"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Temparature Sensore Enable"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Audio Enable"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Gas Enable"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Light Enable"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Temparature Sensore Enable"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Audio Enable"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Gas Enable"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Light Enable"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Temparature Sensore Enable"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Audio Enable"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Gas Enable"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Light Enable"))
        self.menuHome_Automation.setTitle(_translate("MainWindow", "Home Automation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

