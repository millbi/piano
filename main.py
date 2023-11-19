# -*- coding: utf-8 -*-
import multiprocessing

# Form implementation generated from reading ui file 'piano1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
import playsound
from threading import Thread
from data import write_song
import uuid


class Ui_Piano(object):
    def setupUi(self, Piano):
        Piano.setObjectName("Piano")
        Piano.resize(656, 200)

        self.piano = Piano

        self.centralwidget = QtWidgets.QWidget(Piano)
        self.centralwidget.setObjectName("centralwidget")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(30, 0, 42, 180))
        self.btn1.setText("")
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(70, 0, 42, 180))
        self.btn2.setText("")
        self.btn2.setObjectName("btn2")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(50, 0, 35, 120))
        self.Button_1.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Button_1.setText("")
        self.Button_1.setObjectName("Button_1")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(110, 0, 42, 180))
        self.btn3.setText("")
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(150, 0, 42, 180))
        self.btn4.setText("")
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(190, 0, 42, 180))
        self.btn5.setText("")
        self.btn5.setObjectName("btn5")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(230, 0, 42, 180))
        self.btn6.setText("")
        self.btn6.setObjectName("btn6")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(270, 0, 42, 180))
        self.btn7.setText("")
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(310, 0, 42, 180))
        self.btn8.setText("")
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(350, 0, 42, 180))
        self.btn9.setText("")
        self.btn9.setObjectName("btn9")
        self.btn10 = QtWidgets.QPushButton(self.centralwidget)
        self.btn10.setGeometry(QtCore.QRect(390, 0, 42, 180))
        self.btn10.setText("")
        self.btn10.setObjectName("btn10")
        self.btn11 = QtWidgets.QPushButton(self.centralwidget)
        self.btn11.setGeometry(QtCore.QRect(430, 0, 42, 180))
        self.btn11.setText("")
        self.btn11.setObjectName("btn11")
        self.btn12 = QtWidgets.QPushButton(self.centralwidget)
        self.btn12.setGeometry(QtCore.QRect(470, 0, 42, 180))
        self.btn12.setText("")
        self.btn12.setObjectName("btn12")
        self.btn13 = QtWidgets.QPushButton(self.centralwidget)
        self.btn13.setGeometry(QtCore.QRect(510, 0, 42, 180))
        self.btn13.setText("")
        self.btn13.setObjectName("btn13")
        self.btn14 = QtWidgets.QPushButton(self.centralwidget)
        self.btn14.setGeometry(QtCore.QRect(550, 0, 42, 180))
        self.btn14.setText("")
        self.btn14.setObjectName("btn14")
        self.btn15 = QtWidgets.QPushButton(self.centralwidget)
        self.btn15.setGeometry(QtCore.QRect(590, 0, 42, 180))
        self.btn15.setText("")
        self.btn15.setObjectName("btn15")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(90, 0, 35, 120))
        self.Button_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Button_2.setText("")
        self.Button_2.setObjectName("Button_2")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(170, 0, 35, 120))
        self.Button_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Button_3.setText("")
        self.Button_3.setObjectName("Button_3")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(210, 0, 35, 120))
        self.Button_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Button_4.setText("")
        self.Button_4.setObjectName("Button_4")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(250, 0, 35, 120))
        self.Button_5.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Button_5.setText("")
        self.Button_5.setObjectName("Button_5")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(330, 0, 35, 120))
        self.Button_6.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Button_6.setText("")
        self.Button_6.setObjectName("Button_6")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(370, 0, 35, 120))
        self.Button_7.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Button_7.setText("")
        self.Button_7.setObjectName("Button_7")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(450, 0, 35, 120))
        self.Button_8.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Button_8.setText("")
        self.Button_8.setObjectName("Button_8")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(490, 0, 35, 120))
        self.Button_9.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Button_9.setText("")
        self.Button_9.setObjectName("Button_9")
        self.Button_10 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_10.setGeometry(QtCore.QRect(530, 0, 35, 120))
        self.Button_10.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Button_10.setText("")
        self.Button_10.setObjectName("Button_10")
        self.btn1.raise_()
        self.btn2.raise_()
        self.Button_1.raise_()
        self.btn3.raise_()
        self.btn4.raise_()
        self.btn5.raise_()
        self.btn6.raise_()
        self.btn7.raise_()
        self.btn8.raise_()
        self.btn9.raise_()
        self.btn10.raise_()
        self.btn11.raise_()
        self.btn12.raise_()
        self.btn13.raise_()
        self.btn14.raise_()
        self.btn15.raise_()
        self.Button_2.raise_()
        self.Button_3.raise_()
        self.Button_4.raise_()
        self.Button_5.raise_()
        self.Button_6.raise_()
        self.Button_7.raise_()
        self.Button_9.raise_()
        self.Button_10.raise_()
        self.Button_8.raise_()
        Piano.setCentralWidget(self.centralwidget)

        self.retranslateUi(Piano)
        QtCore.QMetaObject.connectSlotsByName(Piano)

        self.th = {}

        #   white
        self.btn1.clicked.connect(self.run_threads)
        self.btn2.clicked.connect(self.run_threads)
        self.btn3.clicked.connect(self.run_threads)
        self.btn4.clicked.connect(self.run_threads)
        self.btn5.clicked.connect(self.run_threads)
        self.btn6.clicked.connect(self.run_threads)
        self.btn7.clicked.connect(self.run_threads)
        self.btn8.clicked.connect(self.run_threads)
        self.btn9.clicked.connect(self.run_threads)
        self.btn10.clicked.connect(self.run_threads)
        self.btn11.clicked.connect(self.run_threads)
        self.btn12.clicked.connect(self.run_threads)
        self.btn13.clicked.connect(self.run_threads)
        self.btn14.clicked.connect(self.run_threads)
        self.btn15.clicked.connect(self.run_threads)

        #   black
        self.Button_1.clicked.connect(self.run_threads)
        self.Button_2.clicked.connect(self.run_threads)
        self.Button_3.clicked.connect(self.run_threads)
        self.Button_4.clicked.connect(self.run_threads)
        self.Button_5.clicked.connect(self.run_threads)
        self.Button_6.clicked.connect(self.run_threads)
        self.Button_7.clicked.connect(self.run_threads)
        self.Button_8.clicked.connect(self.run_threads)
        self.Button_9.clicked.connect(self.run_threads)
        self.Button_10.clicked.connect(self.run_threads)

        self.new = {}
        self.ke = str(uuid.uuid4())[:5]

    def play_notes(self, notePath):
        done = False
        while not done:
            playsound.playsound(notePath)
            print(notePath)
            self.new.setdefault(self.ke, []).append(notePath)
            print(self.new)
            if len(self.new[self.ke]) == 5:
                write_song(self.new, 'songs.json')
                p = open('songs.json')
                filedata = p.read()
                filedata = filedata.replace('}{', ', ')
                with open('songs.json', 'w') as file:
                    file.write(filedata)
                self.new = {}
                self.ke = str(uuid.uuid4())[:5]
            done = True
            continue

    def run_threads(self):
        self.th[self.piano.sender().objectName()] = Thread(target=self.play_notes, args=(
            "Sounds\\" + "{}.wav".format(self.piano.sender().objectName()),))
        self.th[self.piano.sender().objectName()].start()
        self.th[self.piano.sender().objectName()].join()

    def retranslateUi(self, Piano):
        _translate = QtCore.QCoreApplication.translate
        Piano.setWindowTitle(_translate("Piano", "Пианино"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Piano = QtWidgets.QMainWindow()
    ui = Ui_Piano()
    ui.setupUi(Piano)
    Piano.show()
    sys.exit(app.exec_())
