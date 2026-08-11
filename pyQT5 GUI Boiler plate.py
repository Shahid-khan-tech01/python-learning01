# INTRODUCTION TO PYQT5 GUI

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MY FIRST GUI!")
        self.setWindowIcon(QIcon("profile.jpg"))
        self.setGeometry(700, 300, 500, 500)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
