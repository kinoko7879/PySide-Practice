"""
1. Correct layout
2. open file properly
reference site
r1. how to open file with qt => https://steam.oxxostudio.tw/category/python/pyqt5/qfiledialog.html 
"""
from PySide2.QtWidgets import (QMainWindow, QWidget, 
        QLabel, QVBoxLayout, QHBoxLayout, QPushButton,
        QAction, QMenu, QMessageBox,QScrollArea, QSizePolicy)
from PySide2.QtGui import QIcon, QPixmap, QImage, QPalette
from PySide2.QtCore import QSize,QDir
from PySide2.QtWidgets import QFileDialog as QFD
class ImageViewer(QMainWindow):
    def __init__(self):
        super(ImageViewer, self).__init__()
        self.setWindowTitle("ImageAnalysis ")
        self.img1 = QImag()
        self.fileName = ''
        self.scelFactor = 1.778

        self.imgLabel = QLabel()
        self.imgLabel.setBackgroundRole(QPalette.Base)
        mp = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imgLabel.setSizePolicy(mp)
        self.imgLabel.setScaledContents(True)

        self.scrollArea = QScrollArea()
        self.scrollArea.setBackgroundRole(QPalette.Shadow())
        self.scrollAreaWidget(self.imgLabel)
        self.setCentralWidget(self.imgLabel)

        self.createAction()
        self.createMenus()

        self.statusBar().showMessage("Welcome to ImageViewer")
        self.setWindowTitle("ImageViewer")
        w, h = 400,  int(400/ self.scelFactor)
        self.resize(w, h)
        self.move(0,0)

    def resizeEvent(self, event):
        if not self.img1.isNull():
            self.updateView()

    def updateView(self):
        if self.scelFactor < 1:
            self.imgLabel.resize(self.h() * self.scelFactor, self.h())
        else:
            self.imgLabel.resize(self.w(), round(self.w()/ self.scelFactor) )
        self.statusBar().showMessage




       """ 
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
       """

        
