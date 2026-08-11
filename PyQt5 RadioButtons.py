# PYQT5 RADIO BUTTONS IN PYTHON

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup, QGroupBox
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MY FIRST GUI!")
        self.setWindowIcon(QIcon("profile.jpg"))
        self.setGeometry(700, 300, 500, 500)
        self.Radio1 = QRadioButton("Credit Card", self)
        self.Radio2 = QRadioButton("Debit Card", self)
        self.Radio3 = QRadioButton("Online Payments", self)
        self.Radio4 = QRadioButton("In-Store", self)
        self.Radio5 = QRadioButton("Offline Payments", self)
        self.g1 = QButtonGroup(self)
        self.g2 = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.Radio1.setGeometry(0, 0, 300, 50)
        self.Radio2.setGeometry(0, 50, 300, 50)
        self.Radio3.setGeometry(0, 100, 300, 50)
        self.Radio4.setGeometry(0, 150, 300, 50)
        self.Radio5.setGeometry(0, 200, 300, 50)
        self.setStyleSheet("QRadioButton{""font-size: 30px;"
                           "font-family: Arial;"
                           "padding: 10px;"
                           "}")
        self.g1.addButton(self.Radio1)
        self.g1.addButton(self.Radio2)
        self.g1.addButton(self.Radio3)
        self.g2.addButton(self.Radio4)
        self.g2.addButton(self.Radio5)

        self.Radio1.toggled.connect(self.radio_changed)
        self.Radio2.toggled.connect(self.radio_changed)
        self.Radio3.toggled.connect(self.radio_changed)
        self.Radio4.toggled.connect(self.radio_changed)
        self.Radio5.toggled.connect(self.radio_changed)

    def radio_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
