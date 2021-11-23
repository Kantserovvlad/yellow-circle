import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from random import randint


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setFixedSize(400, 400)
        self.is_draw = False
        self.pushButton.move(250, 300)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.is_draw = True
        self.update()

    def paintEvent(self, event):
        if self.is_draw:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        a = randint(1, 100)
        x, y = randint(1, 400 - a), randint(1, 400 - a)
        self.qp.setBrush(QColor('yellow'))
        self.qp.drawEllipse(x, y, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
