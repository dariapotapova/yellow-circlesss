import sys
from random import randint

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


SCREEN_SIZE = (600, 650)


class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui.ui", self)
        self.resize(*SCREEN_SIZE)
        self.initUi()

    def initUi(self):
        self.flag = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(250, 255, 0))
            x, y = randint(0, SCREEN_SIZE[0]),\
                         randint(0, SCREEN_SIZE[1])
            w = h = randint(0, SCREEN_SIZE[0])
            qp.drawEllipse(x, y, w, h)
            qp.end()
            self.flag = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())