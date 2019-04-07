from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)

        self.label.setGeometry(160, 40, 200, 100)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):
        self.label.setText(str(value))
        self.label.setFont(QFont("Roman times", value, QFont.Bold))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())