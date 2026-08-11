# PYQT5 BUTTONS CREATOR IN PYTHON

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MY FIRST GUI!")
        self.setWindowIcon(QIcon("profile.jpg"))
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("Submit", self)
        self.label = QLabel("Welcome!", self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(120, 200, 250, 100)
        self.button.setStyleSheet("background-color: green;"
                                   "font-size: 30px;"
                                  "font-weight: bold;"
                                  "border: 1px solid black;"
                                   "border-radius: 50px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150, 300, 320, 100)
        self.label.setStyleSheet("font-size: 30px;")

    def on_click(self):
        self.label.setText("Submitted Successfully!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
