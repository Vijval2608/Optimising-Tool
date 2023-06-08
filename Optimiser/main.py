import sys
import subprocess
import psutil
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from optimizer import Ui_MainWindow

class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon("Optim.ico"))
        self.setToolTip("Optim")
        self.activated.connect(self.iconActivated)

    def iconActivated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.parent().show()

class SplashWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0 , 120))
        self.ui.gui.setGraphicsEffect(self.shadow)

        self.ui.Close.setCursor(QCursor(Qt.PointingHandCursor))
        self.ui.Close.clicked.connect(self.close)

        self.ui.Optimize_Btn.clicked.connect(self.optimize)
        self.ui.Optimize_Btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.ui.Cache_Btn.clicked.connect(self.clear_cache)
        self.ui.Cache_Btn.setCursor(QCursor(Qt.PointingHandCursor))

        # Center align progress bar
        self.ui.progress_CPU.setAlignment(Qt.AlignCenter)
        self.ui.progress_DISK.setAlignment(Qt.AlignCenter)
        self.ui.progress_GPU.setAlignment(Qt.AlignCenter)

        # Create a timer to update the system info
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateSystemInfo)
        self.timer.start(100)

        # Initialize position of the mouse
        self.dragPos = None

        self.show()

    def optimize(self):
        subprocess.run("powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c", shell=True)

    def clear_cache(self):
        subprocess.run("del /f /s /q %temp%\\*", shell=True)
        subprocess.run("del /f /s /q %systemroot%\\temp\\*", shell=True)

    def progressBarValue(self, cpu, disk, gpu):
        
        def calcProgress(value):
            progress = (100 - value)/ 100.00
            return progress
        
        stylesheet = """
        QFrame{
            border-radius:50px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 85, 141, 0), stop:{STOP_2} rgba(222, 49, 99, 255));
        }
        """

        p_cpu = calcProgress(cpu)
        p_disk = calcProgress(disk)
        p_gpu = calcProgress(gpu)
        stop_cpu1 = str(p_cpu - 0.05)
        stop_cpu2 = str(p_cpu)
        stop_disk1 = str(p_disk - 0.05)
        stop_disk2 = str(p_disk)
        stop_gpu1 = str(p_gpu - 0.05)
        stop_gpu2 = str(p_gpu)

        newStylesheet_cpu = stylesheet.replace("{STOP_1}", stop_cpu1).replace("{STOP_2}", stop_cpu2)
        newStylesheet_disk = stylesheet.replace("{STOP_1}", stop_disk1).replace("{STOP_2}", stop_disk2)
        newStylesheet_gpu = stylesheet.replace("{STOP_1}", stop_gpu1).replace("{STOP_2}", stop_gpu2)
        self.ui.CircularProgress_CPU.setStyleSheet(newStylesheet_cpu)
        self.ui.CircularProgress_DISK.setStyleSheet(newStylesheet_disk)
        self.ui.CircularProgress_GPU.setStyleSheet(newStylesheet_gpu)


    def updateSystemInfo(self):
        cpu_percent = psutil.cpu_percent()
        disk_usage = psutil.disk_usage('/').percent
        mem_info = psutil.virtual_memory()
        mem_usage = mem_info.used / mem_info.total * 100
        mem_usage = round(mem_usage, 1)
        self.progressBarValue(cpu_percent,disk_usage,mem_usage)

        htmlText_cpu = """<p align="center" style=" margin-top:0px; font-weight:200; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt;">{VALUE_CPU}</span><span style=" font-size:14pt; vertical-align:super;">%</span></p>"""
        htmlText_disk = """<p align="center" style=" margin-top:0px; font-weight:200; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt;">{VALUE_DISK}</span><span style=" font-size:14pt; vertical-align:super;">%</span></p>"""
        htmlText_gpu = """<p align="center" style=" margin-top:0px; font-weight:200; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt;">{VALUE_GPU}</span><span style=" font-size:14pt; vertical-align:super;">%</span></p>"""
        
        newHtml_cpu = htmlText_cpu.replace("{VALUE_CPU}", str(cpu_percent))
        newHtml_disk = htmlText_disk.replace("{VALUE_DISK}", str(disk_usage))
        newHtml_gpu = htmlText_gpu.replace("{VALUE_GPU}", str(mem_usage))
        self.ui.progress_CPU.setText(newHtml_cpu)
        self.ui.progress_DISK.setText(newHtml_disk)
        self.ui.progress_GPU.setText(newHtml_gpu)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.dragPos:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = None

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon('Optim.ico'))
        window = SplashWindow()
        sys.exit(app.exec())
    except Exception:
        pass