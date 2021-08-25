# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_test_20_08_2021.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from flow_meter_class_py import flow_meter_class, mx110_read_data
from threading import Timer
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 318)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.but_open = QtWidgets.QPushButton(self.centralwidget)
        self.but_open.setGeometry(QtCore.QRect(100, 20, 75, 23))
        self.but_open.setObjectName("but_open")
        self.but_save = QtWidgets.QPushButton(self.centralwidget)
        self.but_save.setGeometry(QtCore.QRect(180, 20, 75, 23))
        self.but_save.setObjectName("but_save")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.check_save = QtWidgets.QCheckBox(self.centralwidget)
        self.check_save.setGeometry(QtCore.QRect(10, 50, 81, 17))
        self.check_save.setObjectName("check_save")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 100, 61, 21))
        self.label_3.setObjectName("label_3")
        self.out_rate = QtWidgets.QTextEdit(self.centralwidget)
        self.out_rate.setGeometry(QtCore.QRect(0, 130, 81, 31))
        self.out_rate.setObjectName("out_rate")
        self.out_temp = QtWidgets.QTextEdit(self.centralwidget)
        self.out_temp.setGeometry(QtCore.QRect(90, 130, 71, 31))
        self.out_temp.setObjectName("out_temp")
        self.out_press = QtWidgets.QTextEdit(self.centralwidget)
        self.out_press.setGeometry(QtCore.QRect(180, 130, 71, 31))
        self.out_press.setObjectName("out_press")
        self.test_ad_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.test_ad_1.setGeometry(QtCore.QRect(10, 200, 91, 31))
        self.test_ad_1.setObjectName("test_ad_1")
        self.text_ad_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.text_ad_2.setGeometry(QtCore.QRect(10, 240, 91, 31))
        self.text_ad_2.setObjectName("text_ad_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.timer = QTimer()
        self.timer.timeout.connect(self.read_devices_data)

        self.but_open.clicked.connect(self.main_loop)
        self.but_save.clicked.connect(self.save_func)

        self.data_rate = 0
        self.data_temp = 0
        self.data_press = 0
        self.saved = False


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def save_func(self):
        self.saved = True
        self.f.close()

    def main_loop(self):
        self.comport = self.lineEdit.text()
        #self.q1 = flow_meter_class(str(self.comport),1,9600,1,8,1,167,171,default_valume=4)
        #self.T1 = mx110_read_data(str(self.comport),16,9600,1,8,1,default_valume=4)
        self.q1 = flow_meter_class("COM5", 1, 9600, 1, 8, 1, 167, 171, default_valume=4)
        self.T1 = mx110_read_data("COM5", 16, 9600, 1, 8, 1, default_valume=4)
        if self.check_save.isChecked() and self.saved == False:

            self.f = open('text_with_data.txt', 'w')
            self.f.write("rate,temp,press\n")

        self.out_press.setText("start")
        self.out_rate.setText("start")
        self.out_temp.setText("start")
        self.timer.start(500)

    def read_devices_data(self):
        self.datas = self.q1.read_temp_and_flow()
        self.data_temps = self.T1.read_data()
        #print(self.data_temps)
        self.out_rate.setText("%.3f"%self.datas[0])
        self.out_temp.setText("%.3f"%self.datas[1])
        self.out_press.setText("%.3f"%self.data_temps[0])
        self.data_rate = self.datas[0]
        self.data_temp = self.datas[1]
        self.data_press = self.data_temps[0]
        if self.check_save.isChecked() and self.saved == False:
            now = datetime.datetime.now()
            self.f.write("%f,%f,%f," % (self.data_rate, self.data_temp, self.data_press))
            self.f.write(str(now.strftime("%H:%M:%S\n")))




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.but_open.setText(_translate("MainWindow", "открыть"))
        self.but_save.setText(_translate("MainWindow", "сохранить"))
        self.check_save.setText(_translate("MainWindow", "сохранять"))
        self.label.setText(_translate("MainWindow", "расход"))
        self.label_2.setText(_translate("MainWindow", "температура"))
        self.label_3.setText(_translate("MainWindow", "давление"))


if __name__ == "__main__":
    import sys
    app =QtWidgets.QApplication(sys.argv)
    main_wind = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_wind)
    main_wind.show()
    sys.exit(app.exec_())