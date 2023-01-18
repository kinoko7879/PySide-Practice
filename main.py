"""
This script aims to build some kind of automation that become time-saving tool

1. Build basic UI first then implement logic behind
2. Compare Two or multiple images 
    2-1. Automate chose ROI then run related analysis
    2-2. 
3. Log analysis
4. Build a terminal emulator to make things easier



=============Split line============================
Todo list
1. choose icon for toolbar
2. Find an appropiate widget to handle terminal emulator
3. Research how to open specific file like othe gui applications
"""
from PySide2.QtWidgets import (QApplication, QWidget, 
        QMainWindow, QPushButton, QLabel,
        QToolBar, QAction, QStatusBar, QVBoxLayout, QTabWidget)
import cv2 
from PySide2.QtCore import QSize, Qt 
from PySide2.QtGui import QIcon,QPixmap
import sys
from ImageAnalysis.ImgAnalysisWindow import ImgAnalysisWindow 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.w1 = ImgAnalysisWindow()
        self.setWindowTitle("時を止まれ")
        button = QPushButton("Terminal here")
        toolbar = QToolBar("Things start here")
        #self.setFixedSize(QSize(400, 100))
        #bt1_action = QAction("Image Analysis", self)
        bt1_action = QAction(QIcon('shiba.png'), "Image Analysis", self)
        bt1_action.setStatusTip("You can't see me!!")
        bt1_action.triggered.connect(self.show_Img_Window)
        toolbar.addAction(bt1_action)
        #bt2_action = QAction("Log Analysis", self)
        bt2_action = QAction(QIcon('log.png'), "Log Analysis", self)
        bt2_action.setStatusTip("You should not pass!!!")
        toolbar.addAction(bt2_action)
        

        self.addToolBar(toolbar)
        self.setStatusBar(QStatusBar(self))
        self.setFixedSize(QSize(1800,1900))
        self.setCentralWidget(button)
    def show_Img_Window(self):
        if self.w1.isVisible():
            self.w1.hide()
        else:
            self.w1.show()
app = QApplication(sys.argv)

window =MainWindow()
window.show()

app.exec_()
