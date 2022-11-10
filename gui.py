# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self, x1, x2, y1, y2, title):
        super().__init__()

        self.setGeometry(x1, x2, y1, y2)
        self.setWindowTitle(title)
        self.show()


class Set_Password(QMainWindow):
    pass


app = QApplication(sys.argv)
window = Window(300, 300, 600, 400, 'Password Manager')
window1 = Window(250, 250, 400, 300, 'Select Database')
sys.exit(app.exec())
