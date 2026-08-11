#  PYQT5 CASCADING STYLE SHEETS IN PYTHON (SET STYLE SHEETS)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MY FIRST GUI!")
        self.setWindowIcon(QIcon("profile.jpg"))
        self.b1 = QPushButton("#1")
        self.b2 = QPushButton("#2")
        self.b3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        c_widget = QWidget()
        self.setCentralWidget(c_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.b1)
        hbox.addWidget(self.b2)
        hbox.addWidget(self.b3)

        c_widget.setLayout(hbox)

        self.b1.setObjectName("b1")
        self.b2.setObjectName("b2")
        self.b3.setObjectName("b3")

        self.setStyleSheet("""
        QPushButton {
                       font-size: 40px;
                       font-family: Arial;
                       padding: 15px 75px;
                       margin: 25px;
                       border: 3px solid black;
                       border-radius: 30px;             
        }
        QPushButton#b1{
        background-color: hsl(63, 98%, 55%);
        }
        QPushButton#b2 {
        background-color: hsl(126, 98%, 55%);
        }
        QPushButton#b3 {
        background-color: hsl(214, 96%, 50%);
        }
        QPushButton#b1:hover {
        background-color: hsl(150, 90%, 80%);
        }
        QPushButton#b2:hover {
        background-color: hsl(300, 90%, 80%);
        }
        QPushButton#b3:hover {
        background-color: hsl(0, 90%, 80%);
        }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
