# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\inviter.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import qrcode
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from db_connector import mysql_connect


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 685)
        MainWindow.setStyleSheet("background-color: rgb(230, 232, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 641, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.inviterId_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.inviterId_label_2.setGeometry(QtCore.QRect(40, 140, 221, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.inviterId_label_2.setFont(font)
        self.inviterId_label_2.setObjectName("inviterId_label_2")
        self.inviterId_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.inviterId_lineEdit.setGeometry(QtCore.QRect(240, 130, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.inviterId_lineEdit.setFont(font)
        self.inviterId_lineEdit.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.inviterId_lineEdit.setObjectName("inviterId_lineEdit")
        self.meetingDate_Time_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.meetingDate_Time_label_3.setGeometry(QtCore.QRect(40, 230, 321, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.meetingDate_Time_label_3.setFont(font)
        self.meetingDate_Time_label_3.setObjectName("meetingDate_Time_label_3")
        self.meeting_dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.meeting_dateEdit.setGeometry(QtCore.QRect(340, 220, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.meeting_dateEdit.setFont(font)
        self.meeting_dateEdit.setStyleSheet("")
        self.meeting_dateEdit.setObjectName("meeting_dateEdit")
        self.meeting_timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.meeting_timeEdit.setGeometry(QtCore.QRect(570, 220, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.meeting_timeEdit.setFont(font)
        self.meeting_timeEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.meeting_timeEdit.setObjectName("meeting_timeEdit")
        self.guestName_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.guestName_label_4.setGeometry(QtCore.QRect(40, 320, 221, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.guestName_label_4.setFont(font)
        self.guestName_label_4.setObjectName("guestName_label_4")
        self.guestId_label_5 = QtWidgets.QLabel(self.centralwidget)
        self.guestId_label_5.setGeometry(QtCore.QRect(40, 390, 221, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.guestId_label_5.setFont(font)
        self.guestId_label_5.setObjectName("guestId_label_5")
        self.guestName_lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.guestName_lineEdit_2.setGeometry(QtCore.QRect(240, 310, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.guestName_lineEdit_2.setFont(font)
        self.guestName_lineEdit_2.setObjectName("guestName_lineEdit_2")
        self.guestId_lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.guestId_lineEdit_3.setGeometry(QtCore.QRect(240, 390, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.guestId_lineEdit_3.setFont(font)
        self.guestId_lineEdit_3.setObjectName("guestId_lineEdit_3")
        self.submit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.submit_pushButton.setGeometry(QtCore.QRect(240, 510, 141, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.submit_pushButton.setFont(font)
        self.submit_pushButton.setStyleSheet("background-color: rgb(165, 113, 53);")
        self.submit_pushButton.setObjectName("submit_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.submit_pushButton.clicked.connect(self.action)
        # self.submit_pushButton.clicked.connect(self.generating_qrcode)

    
    # collecting the data
    def action(self):
        self.inviterId = self.inviterId_lineEdit.text()
        self.meetingDate = self.meeting_dateEdit.text()
        self.meetingTime = self.meeting_timeEdit.text()
        self.guestName = self.guestName_lineEdit_2.text()
        self.guestId = self.guestId_lineEdit_3.text()
        meeting_time = self.time_converte_in_epoch(self.meetingDate, self.meetingTime)
        self.meeting_id = self.guestId + str(meeting_time)
        data = (self.inviterId + " " + str(meeting_time) + " " + self.meeting_id + " " + self.guestName + " " + self.guestId)
        self.generating_qrcode(data)
        self.data_insertion_into_db((meeting_time, self.inviterId, self.guestName, self.guestId, self.meeting_id))

    
    # genarting the qrcodes
    def generating_qrcode(self,data):
        # data = self.inviterId + self.meetingDate + self.meetingTime + self.guestName + self.guestId
        qrcode_img = qrcode.make(data)
        qrcode_img.save(f"./qrcodes/{self.meeting_id}.jpg")

    # converting human readable format to epoch
    def time_converte_in_epoch(self,dates,times):
        dateAndTime = dates +" "+ times
        data = time.strptime(dateAndTime, "%d-%m-%Y %H:%M")
        return int(time.mktime(data))

    def data_insertion_into_db(self, data):
        try:
            cnx = mysql_connect()
            sql = "INSERT INTO visitors_data (Meeting_time, Inviter_Id,Guest_Name, Guest_Id, Meeting_id) values(%s,%s,%s,%s,%s)"
            cursor = cnx.cursor()
            cursor.execute(sql,data)
            cnx.commit()
            print("data is updated")
        
        except Exception as e:
            print(e)
        
        finally:
            cursor.close()
            cnx.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Inviting The Cadidate For Interview"))
        self.inviterId_label_2.setText(_translate("MainWindow", "Inviter_ID :-"))
        self.meetingDate_Time_label_3.setText(_translate("MainWindow", "Meeting Date & Time :-"))
        self.guestName_label_4.setText(_translate("MainWindow", "Guest_Name :-"))
        self.guestId_label_5.setText(_translate("MainWindow", "Guest_ID :-"))
        self.submit_pushButton.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
