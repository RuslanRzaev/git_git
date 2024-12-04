import io
import sys
from random import randint

from PyQt6 import uic
from PyQt6.QtCore import QRectF, Qt
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog

with open('ui.ui', encoding='utf-8') as f:
    template1 = f.read()

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template1)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.button_handler)

    def button_handler(self):
        diameter = randint(10, 100)
        x = 300
        y = 300
        self.rect = QRectF(x, y, diameter, diameter)
        self.color = QColor(QColor('yellow'))
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
