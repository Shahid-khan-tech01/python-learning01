#  PYQT5 LAYOUTS

import sys
from tkinter import Grid

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MY FIRST GUI!")
        self.setWindowIcon(QIcon("profile.jpg"))
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        c_widget = QWidget()
        self.setCentralWidget(c_widget)

        label1 = QLabel("Hello World")
        label2 = QLabel("Hello World")
        label3 = QLabel("Hello World")
        label4 = QLabel("Hello World")
        label5 = QLabel("Hello World")
        label6 = QLabel("Hello World")

        label1.setStyleSheet("background-color: blue;"
                             "font-size:20px;")
        label2.setStyleSheet("background-color: green;"
                             f"font-size:20px;")
        label3.setStyleSheet("background-color: yellow;"
                             "font-size:20px;")
        label4.setStyleSheet("background-color: purple;"
                             "font-size:20px;")
        label5.setStyleSheet("background-color: red;"
                             "font-size:20px;")
        label6.setStyleSheet("background-color: orange;"
                             "font-size:20px;")
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)
        vbox.addWidget(label6)
        c_widget.setLayout(vbox)

#       hbox = QHBoxLayout()
#       hbox.addWidget(label1)
#       hbox.addWidget(label2)
#       hbox.addWidget(label3)
#       hbox.addWidget(label4)
#       hbox.addWidget(label5)
#       hbox.addWidget(label6)
#       c_widget.setLayout(hbox)

#       Grid = QGridLayout()
#       Grid.addWidget(label1, 0, 0)
#       Grid.addWidget(label2, 0, 1)
#       Grid.addWidget(label3, 0, 2)
#       Grid.addWidget(label4, 1, 0)
#       Grid.addWidget(label5, 1, 1)
#       Grid.addWidget(label6, 1, 2)
#       c_widget.setLayout(Grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
