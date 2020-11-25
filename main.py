import random
from PyQt5.QtGui import QBrush, QPainter, QColor, QPalette, QFont
from PyQt5.QtCore import Qt, QRect, QMetaObject, QCoreApplication
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.num = random.randint(10, 150)
        self.show()

    def run(self):
        self.num = random.randint(10, 150)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        qp.setBrush(QColor('Yellow'))
        qp.drawEllipse(100 + self.num, 100 + self.num, self.num, self.num)
        self.update()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
