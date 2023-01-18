
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QToolBar, QAction, QStatusBar
import cv2 
from PySide2.QtCore import QSize, Qt 
from PySide2.QtGui import QIcon
import sys


class CustomLabel(QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False

    def mousePressEvent(self, event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.x()

    def mouseReleaseEvent(self, event):
        self.flag = False
    def mouseMoveEvent(self, event):
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()

    def paintEvent(self,event):
        super().paintEvent(event)
        rect = QRect(self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))
        painter.drawRect(rect)
        pqscreen = QGuiApplication.primaryScreen()
        pixmap2 = pqscreen.grabWindow(self.winId(), self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
        pixmap2.save('55.png')

        class Example(QWidget):
            def __init__(self):
                super().__init__()
                self.initUI()
            def initUI(self):
                self.resize(675, 300)
                self.setWindowTitle('This is cv and qt practice window')
                img = cv2.imread('path sould be listed here')
                h, w, d = img.shape
                BPL = 3 * w
                cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
                QImg = QImage(img.data, w, h, BPL, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(QImg)
                self.lb.setPixmap(pixmap)
                self.lb.setCursor(Qt.CrossCursor)
                self.show()
                

