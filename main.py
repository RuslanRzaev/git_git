import io
import random
import sys
from random import randint

from PyQt6.QtCore import QRectF
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog
from ui import Ui_MainWindow

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_handler)

    def button_handler(self):
        diameter = randint(10, 100)
        x = 300
        y = 300
        self.rect = QRectF(x, y, diameter, diameter)
        self.color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.update()

    def paintEvent(self, event):
        if hasattr(self, "color"):
            painter = QPainter(self)
            painter.setBrush(self.color)
            painter.drawEllipse(self.rect)
            painter.end()

def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)

if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
