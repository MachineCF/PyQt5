import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication,qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        exitAct = QAction(QIcon('../res/exit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)


        saveAct = QAction(QIcon('../res/save.png'), 'Save', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.triggered.connect(qApp.aboutQt)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.toolbar = self.addToolBar('Save')
        self.toolbar.addAction(saveAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())