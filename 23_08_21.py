# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_23_08_21.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from test_owen_main import driver_hard
from threading import Thread
from PyQt5.QtGui import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(966, 567)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(180, 20, 151, 61))
        self.groupBox.setObjectName("groupBox")
        self.connect = QtWidgets.QPushButton(self.groupBox)
        self.connect.setGeometry(QtCore.QRect(40, 20, 91, 21))
        self.connect.setObjectName("connect")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 10, 441, 511))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 40, 421, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 230, 271, 271))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 110, 491, 191))
        self.groupBox_3.setObjectName("groupBox_3")
        self.device_num = QtWidgets.QComboBox(self.groupBox_3)
        self.device_num.setGeometry(QtCore.QRect(30, 80, 81, 31))
        self.device_num.setObjectName("device_num")
        self.device_num.addItem("")
        self.device_num.addItem("")
        self.device_num.addItem("")
        self.device_num.addItem("")
        self.device_num.addItem("")
        self.new_q = QtWidgets.QTextEdit(self.groupBox_3)
        self.new_q.setGeometry(QtCore.QRect(150, 50, 91, 31))
        self.new_q.setObjectName("new_q")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(150, 30, 101, 16))
        self.label.setObjectName("label")
        self.set_new_q = QtWidgets.QPushButton(self.groupBox_3)
        self.set_new_q.setGeometry(QtCore.QRect(400, 50, 81, 31))
        self.set_new_q.setObjectName("set_new_q")
        self.set_q_to_t = QtWidgets.QPushButton(self.groupBox_3)
        self.set_q_to_t.setGeometry(QtCore.QRect(400, 130, 81, 31))
        self.set_q_to_t.setObjectName("set_q_to_t")
        self.comboBox_open_close = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_open_close.setGeometry(QtCore.QRect(260, 130, 121, 31))
        self.comboBox_open_close.setObjectName("comboBox_open_close")
        self.comboBox_open_close.addItem("")
        self.comboBox_open_close.addItem("")
        self.comboBox_open_close.addItem("")
        self.comboBox_open_close.addItem("")
        self.time_new = QtWidgets.QTextEdit(self.groupBox_3)
        self.time_new.setGeometry(QtCore.QRect(150, 130, 91, 31))
        self.time_new.setObjectName("time_new")
        self.line = QtWidgets.QFrame(self.groupBox_3)
        self.line.setGeometry(QtCore.QRect(133, 20, 20, 161))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox_3)
        self.line_2.setGeometry(QtCore.QRect(147, 79, 331, 51))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(170, 110, 47, 13))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 966, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.start = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_func)

        self.connect.clicked.connect(self.connect_func)
        self.set_new_q.clicked.connect(self.set_new_q_func)
        self.set_q_to_t.clicked.connect(self.set_new_q_t_func)



        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def timer_func(self):
        x = self.device.get_all_data_to_ui()

        for i in range(0,8):
            self.tableWidget_2.setItem(i+1, 1, QtWidgets.QTableWidgetItem(str("%.03f"%x[2][i])))
            self.tableWidget_2.setItem(i+1, 0, QtWidgets.QTableWidgetItem(str("%.03f"%x[3][i])))

        for i in range(0,5):
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str("%.03f"%x[0][i])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str("%.03f"%x[1][i])))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str("%.03f"%x[5][i])))

            if x[4][i]["mode"] == "time":
                if x[4][i]["dir"] == 1:
                    self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str("T(up)%d"% x[4][i]["time"])))
                if x[4][i]["dir"] == 3:
                    self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str("T(down)%d"% x[4][i]["time"])))
                if x[4][i]["dir"] == 2:
                    self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str("open_full")))
                if x[4][i]["dir"] == 4:
                    self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str("close_full")))
            if x[4][i]["mode"] == "q":
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str("Q(set)%.2f" % x[4][i]["q"])))
        if x[5][0] == 0:
            self.tableWidget.item(0,3).setBackground(QtGui.QColor(255,0,0))
        else:
            self.tableWidget.item(0, 3).setBackground(QtGui.QColor(0, 255, 0))
        if x[5][1] == 0:
            self.tableWidget.item(1, 3).setBackground(QtGui.QColor(255, 0, 0))
        else:
            self.tableWidget.item(1, 3).setBackground(QtGui.QColor(0, 255, 0))
        if x[5][2] == 0:
            self.tableWidget.item(2,3).setBackground(QtGui.QColor(255,0,0))
        else:
            self.tableWidget.item(2, 3).setBackground(QtGui.QColor(0, 255, 0))
        if x[5][3] == 0:
            self.tableWidget.item(3,3).setBackground(QtGui.QColor(255,0,0))
        else:
            self.tableWidget.item(3, 3).setBackground(QtGui.QColor(0, 255, 0))
        if x[5][4] == 0:
            self.tableWidget.item(4,3).setBackground(QtGui.QColor(255,0,0))
        else:
            self.tableWidget.item(4, 3).setBackground(QtGui.QColor(0, 255, 0))
        print(x)


    def connect_func(self):
        if self.start == 0:
            self.start = 1

            self.device = driver_hard()
            self.tr = Thread(target=self.device.loop_hard)
            self.tr.start()
            self.timer.start(500)


    def set_new_q_func(self):
        numq = int(self.device_num.currentText())
        text = self.new_q.toPlainText()
        self.device.set_new_task("q", 500, float(text), 0, numq)

    def set_new_q_t_func(self):
        numq = int(self.device_num.currentText())
        time = int(self.time_new.toPlainText())
        dir = self.comboBox_open_close.currentIndex()
        if dir == 0:
            self.device.set_new_task("time", time, 0, 1, numq)
        if dir == 1:
            self.device.set_new_task("time", time, 0, 3, numq)
        if dir == 2:
            self.device.set_new_task("time", time, 0, 4, numq)
        if dir == 3:
            self.device.set_new_task("time", time, 0, 2, numq)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "начальные настройки"))
        self.connect.setText(_translate("MainWindow", "подключиться"))
        self.groupBox_2.setTitle(_translate("MainWindow", "только отображение текущих значений"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "расход заданный"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "расход текущий"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "температура"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "выполнено"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "температура"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "давление"))
        self.groupBox_3.setTitle(_translate("MainWindow", "задание новый заданий"))
        self.device_num.setItemText(0, _translate("MainWindow", "1"))
        self.device_num.setItemText(1, _translate("MainWindow", "2"))
        self.device_num.setItemText(2, _translate("MainWindow", "3"))
        self.device_num.setItemText(3, _translate("MainWindow", "4"))
        self.device_num.setItemText(4, _translate("MainWindow", "5"))
        self.label.setText(_translate("MainWindow", "Новый расход кг/с"))
        self.set_new_q.setText(_translate("MainWindow", "задать"))
        self.set_q_to_t.setText(_translate("MainWindow", "выполнить"))
        self.comboBox_open_close.setItemText(0, _translate("MainWindow", "открыть"))
        self.comboBox_open_close.setItemText(1, _translate("MainWindow", "закрыть"))
        self.comboBox_open_close.setItemText(2, _translate("MainWindow", "закрыть полностью"))
        self.comboBox_open_close.setItemText(3, _translate("MainWindow", "открыть полностью"))
        self.label_2.setText(_translate("MainWindow", "время мс"))

if __name__ == "__main__":
    import sys
    app =QtWidgets.QApplication(sys.argv)
    main_wind = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_wind)
    main_wind.show()
    sys.exit(app.exec_())