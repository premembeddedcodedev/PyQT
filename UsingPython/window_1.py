import sys
from PyQt5.QtCore import QSize, Qt
from random import randint

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        self.setFixedSize(QSize(800, 600))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Automation")
        self.setFixedSize(QSize(800, 600))
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()
        self.window3 = AnotherWindow()

        l = QVBoxLayout()
        button1 = QPushButton("1st: Main Door Events")
        button1.clicked.connect(self.toggle_window1)
        l.addWidget(button1)

        button2 = QPushButton("1st: North Door Events")
        button2.clicked.connect(self.toggle_window2)
        l.addWidget(button2)

        button3 = QPushButton("2nd: North Door Events")
        button3.clicked.connect(self.toggle_window3)
        l.addWidget(button3)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    def toggle_window1(self, checked):
        self.setFixedSize(QSize(800, 600))
        if self.window1.isVisible():
            self.window1.hide()

        else:
            self.window1.show()

    def toggle_window2(self, checked):
        self.setFixedSize(QSize(800, 600))
        if self.window2.isVisible():
            self.window2.hide()

        else:
            self.window2.show()

    def toggle_window3(self, checked):
        self.setFixedSize(QSize(800, 600))
        if self.window3.isVisible():
            self.window3.hide()

        else:
            self.window3.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
