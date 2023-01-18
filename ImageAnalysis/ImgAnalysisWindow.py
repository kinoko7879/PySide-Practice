"""
1. Correct layout
2. open file properly
reference site
r1. how to open file with qt => https://steam.oxxostudio.tw/category/python/pyqt5/qfiledialog.html 
"""
from PySide2.QtWidgets import (QMainWindow, QWidget, 
        QLabel, QVBoxLayout, QHBoxLayout, QPushButton)
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QFileDialog as QFD
class ImgAnalysisWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ImageAnalysis ")
        #self.label = QLabel("Image Analysis")
        self.layout = QHBoxLayout()
        self.pic1 = QLabel('This is default pic1')
        defaultImagePath = 'D:\projects\PysideForLazy\griffith.jpg'
        self.pic1.setPixmap(QPixmap(defaultImagePath))
        self.layout.addWidget(self.pic1)
        btn1 = QPushButton("Open files")
        btn1.clicked.connect(self.fileOpen)
        self.layout.addWidget(btn1)
        w = QWidget()
        w.setLayout(self.layout)
        self.setCentralWidget(w)
        self.setFixedSize(QSize(1400,1500))
    def fileOpen(self):
        filePth, fileType = QFD.getOpenFileNames( filter='JPG (*.jpg)')
        print(filePth, fileType)
        self.pic1.setPixmap(QPixmap(filePth))
        self.layout.addWidget(self.pic1)
        

        
