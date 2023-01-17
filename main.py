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
"""
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QToolBar, QAction, QStatusBar
from PySide2.QtCore import QSize, Qt 
from PySide2.QtGui import QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("時を止まれ")
        button = QPushButton("Terminal here")
        toolbar = QToolBar("Things start here")
        #self.setFixedSize(QSize(400, 100))
        #bt1_action = QAction("Image Analysis", self)
        bt1_action = QAction(QIcon('shibi.png'), "Image Analysis", self)
        bt1_action.setStatusTip("That's see what will happend")
        toolbar.addAction(bt1_action)
        #bt2_action = QAction("Log Analysis", self)
        bt2_action = QAction(QIcon('log.png'), "Log Analysis", self)
        bt2_action.setStatusTip("這個加這個能不能站著掙錢 ")
        toolbar.addAction(bt2_action)

        self.addToolBar(toolbar)
        self.setStatusBar(QStatusBar(self))
        self.setCentralWidget(button)
                

app = QApplication(sys.argv)

window =MainWindow()
window.show()

app.exec_()
