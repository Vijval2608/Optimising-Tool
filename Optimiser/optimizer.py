# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'optimizer.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(170, 541)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gui = QFrame(self.centralwidget)
        self.gui.setObjectName(u"gui")
        self.gui.setGeometry(QRect(9, 10, 151, 521))
        self.gui.setStyleSheet(u"QFrame{\n"
"background-color : #212121 ;\n"
"border-radius : 10px;\n"
"}")
        self.gui.setFrameShape(QFrame.NoFrame)
        self.gui.setFrameShadow(QFrame.Plain)
        self.CircularProgressBar_CPU = QFrame(self.gui)
        self.CircularProgressBar_CPU.setObjectName(u"CircularProgressBar_CPU")
        self.CircularProgressBar_CPU.setGeometry(QRect(10, 40, 120, 120))
        self.CircularProgressBar_CPU.setFrameShape(QFrame.NoFrame)
        self.CircularProgressBar_CPU.setFrameShadow(QFrame.Raised)
        self.CircularProgress_CPU = QFrame(self.CircularProgressBar_CPU)
        self.CircularProgress_CPU.setObjectName(u"CircularProgress_CPU")
        self.CircularProgress_CPU.setGeometry(QRect(10, 10, 100, 100))
        self.CircularProgress_CPU.setStyleSheet(u"QFrame{\n"
"	border-radius:50px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 85, 141, 0), stop:0.750 rgba(223, 255, 0, 255));\n"
"}\n"
"")
        self.CircularProgress_CPU.setFrameShape(QFrame.NoFrame)
        self.CircularProgress_CPU.setFrameShadow(QFrame.Raised)
        self.container_CPU = QFrame(self.CircularProgressBar_CPU)
        self.container_CPU.setObjectName(u"container_CPU")
        self.container_CPU.setGeometry(QRect(15, 15, 90, 90))
        self.container_CPU.setAutoFillBackground(False)
        self.container_CPU.setStyleSheet(u"QFrame{\n"
"	border-radius: 45px;\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.container_CPU.setFrameShape(QFrame.NoFrame)
        self.container_CPU.setFrameShadow(QFrame.Raised)
        self.heading_CPU = QLabel(self.container_CPU)
        self.heading_CPU.setObjectName(u"heading_CPU")
        self.heading_CPU.setGeometry(QRect(0, 10, 91, 31))
        font = QFont()
        font.setPointSize(10)
        self.heading_CPU.setFont(font)
        self.heading_CPU.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"background-color: none;")
        self.progress_CPU = QLabel(self.container_CPU)
        self.progress_CPU.setObjectName(u"progress_CPU")
        self.progress_CPU.setGeometry(QRect(0, 30, 91, 31))
        font1 = QFont()
        font1.setPointSize(48)
        font1.setBold(False)
        self.progress_CPU.setFont(font1)
        self.progress_CPU.setStyleSheet(u"background-color: none; color:rgb(255, 255, 255);")
        self.progress_CPU.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.CircularProgressBar_DISK = QFrame(self.gui)
        self.CircularProgressBar_DISK.setObjectName(u"CircularProgressBar_DISK")
        self.CircularProgressBar_DISK.setGeometry(QRect(10, 170, 120, 120))
        self.CircularProgressBar_DISK.setFrameShape(QFrame.NoFrame)
        self.CircularProgressBar_DISK.setFrameShadow(QFrame.Raised)
        self.CircularProgress_DISK = QFrame(self.CircularProgressBar_DISK)
        self.CircularProgress_DISK.setObjectName(u"CircularProgress_DISK")
        self.CircularProgress_DISK.setGeometry(QRect(10, 10, 100, 100))
        self.CircularProgress_DISK.setStyleSheet(u"QFrame{\n"
"	border-radius:50px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.000 rgba(255, 85, 141, 0), stop:0.001 rgba(223, 255, 0, 255));\n"
"}\n"
"")
        self.CircularProgress_DISK.setFrameShape(QFrame.NoFrame)
        self.CircularProgress_DISK.setFrameShadow(QFrame.Raised)
        self.container_DISK = QFrame(self.CircularProgressBar_DISK)
        self.container_DISK.setObjectName(u"container_DISK")
        self.container_DISK.setGeometry(QRect(15, 15, 90, 90))
        self.container_DISK.setAutoFillBackground(False)
        self.container_DISK.setStyleSheet(u"QFrame{\n"
"	border-radius: 45px;\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.container_DISK.setFrameShape(QFrame.NoFrame)
        self.container_DISK.setFrameShadow(QFrame.Raised)
        self.heading_DISK = QLabel(self.container_DISK)
        self.heading_DISK.setObjectName(u"heading_DISK")
        self.heading_DISK.setGeometry(QRect(0, 10, 91, 31))
        self.heading_DISK.setFont(font)
        self.heading_DISK.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"background-color: none;")
        self.progress_DISK = QLabel(self.container_DISK)
        self.progress_DISK.setObjectName(u"progress_DISK")
        self.progress_DISK.setGeometry(QRect(0, 30, 91, 31))
        self.progress_DISK.setFont(font1)
        self.progress_DISK.setStyleSheet(u"background-color: none; color:rgb(255, 255, 255);")
        self.progress_DISK.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.CircularProgressBar_GPU = QFrame(self.gui)
        self.CircularProgressBar_GPU.setObjectName(u"CircularProgressBar_GPU")
        self.CircularProgressBar_GPU.setGeometry(QRect(10, 300, 120, 120))
        self.CircularProgressBar_GPU.setFrameShape(QFrame.NoFrame)
        self.CircularProgressBar_GPU.setFrameShadow(QFrame.Raised)
        self.CircularProgress_GPU = QFrame(self.CircularProgressBar_GPU)
        self.CircularProgress_GPU.setObjectName(u"CircularProgress_GPU")
        self.CircularProgress_GPU.setGeometry(QRect(10, 10, 100, 100))
        self.CircularProgress_GPU.setStyleSheet(u"QFrame{\n"
"	border-radius:50px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 85, 141, 0), stop:0.750 rgba(223, 255, 0, 255));\n"
"}\n"
"")
        self.CircularProgress_GPU.setFrameShape(QFrame.NoFrame)
        self.CircularProgress_GPU.setFrameShadow(QFrame.Raised)
        self.container_GPU = QFrame(self.CircularProgressBar_GPU)
        self.container_GPU.setObjectName(u"container_GPU")
        self.container_GPU.setGeometry(QRect(15, 15, 90, 90))
        self.container_GPU.setAutoFillBackground(False)
        self.container_GPU.setStyleSheet(u"QFrame{\n"
"	border-radius: 45px;\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.container_GPU.setFrameShape(QFrame.NoFrame)
        self.container_GPU.setFrameShadow(QFrame.Raised)
        self.heading_GPU = QLabel(self.container_GPU)
        self.heading_GPU.setObjectName(u"heading_GPU")
        self.heading_GPU.setGeometry(QRect(0, 10, 91, 31))
        self.heading_GPU.setFont(font)
        self.heading_GPU.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"background-color: none;")
        self.progress_GPU = QLabel(self.container_GPU)
        self.progress_GPU.setObjectName(u"progress_GPU")
        self.progress_GPU.setGeometry(QRect(0, 30, 91, 31))
        self.progress_GPU.setFont(font1)
        self.progress_GPU.setStyleSheet(u"background-color: none; color:rgb(255, 255, 255);")
        self.progress_GPU.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.Buttons = QFrame(self.gui)
        self.Buttons.setObjectName(u"Buttons")
        self.Buttons.setGeometry(QRect(20, 419, 111, 91))
        self.Buttons.setFrameShape(QFrame.NoFrame)
        self.Buttons.setFrameShadow(QFrame.Raised)
        self.Optimize_Btn = QPushButton(self.Buttons)
        self.Optimize_Btn.setObjectName(u"Optimize_Btn")
        self.Optimize_Btn.setGeometry(QRect(10, 10, 91, 24))
        self.Optimize_Btn.setStyleSheet(u"QPushButton{\n"
"	border-radius : 10px; color : #ffffff;\n"
"	background-color: rgb(222, 49, 99);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #ffffff; color: #000;\n"
"}")
        self.Cache_Btn = QPushButton(self.Buttons)
        self.Cache_Btn.setObjectName(u"Cache_Btn")
        self.Cache_Btn.setGeometry(QRect(10, 50, 91, 24))
        self.Cache_Btn.setStyleSheet(u"QPushButton{\n"
"	border-radius : 10px; color : #ffffff;\n"
"	background-color: rgb(222, 49, 99);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #ffffff; color: #000;\n"
"}")
        self.Close = QPushButton(self.gui)
        self.Close.setObjectName(u"Close")
        self.Close.setGeometry(QRect(110, 10, 31, 24))
        font2 = QFont()
        font2.setPointSize(16)
        self.Close.setFont(font2)
        self.Close.setStyleSheet(u"QPushButton{\n"
"	border-radius : 10px;\n"
"	background-color: none;\n"
"	color: rgb(236, 240, 241);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Optim", u"Optim", None))
        self.heading_CPU.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:200; font-size:8pt;\">CPU</span></p></body></html>", None))
        self.progress_CPU.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:48pt; font-weight:100; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">0</span><span style=\" font-size:16pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.heading_DISK.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:200; font-size:8pt;\">DISK</span></p></body></html>", None))
        self.progress_DISK.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:48pt; font-weight:100; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">0</span><span style=\" font-size:16pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.heading_GPU.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:200; font-size:8pt;\">RAM</span></p></body></html>", None))
        self.progress_GPU.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:48pt; font-weight:300; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">0</span><span style=\" font-size:16pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.Optimize_Btn.setText(QCoreApplication.translate("MainWindow", u"OPTIMIZE", None))
        self.Cache_Btn.setText(QCoreApplication.translate("MainWindow", u"CACHE CLEAR", None))
        self.Close.setText(QCoreApplication.translate("MainWindow", u"\u2715", None))
    # retranslateUi

