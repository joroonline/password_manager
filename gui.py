# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Password Manager")
        self.show()

class Set_password:
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window1 = Window()
    sys.exit(app.exec())
