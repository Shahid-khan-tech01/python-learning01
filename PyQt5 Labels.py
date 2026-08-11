# PYQT5 LABELS : WHERE WE CAN EDIT OR MODIFY THE TETXS USING THE STYLE SHEETS


import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Labels")
        self.setWindowIcon(QIcon("profile.jpg"))
        self.setGeometry(700, 300, 500, 500)

        label = QLabel("Hello World!", self)
        #  label.setFont(QFont("Arial", 30))     # It is editing of text without the style sheets
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color : #262626;"
                            "background-color : #82f0fa;"
                            "font-weight : bold;"
                            "font-size : 40px;"
                            "font-style : italic;"
                            "text-decoration : underline;")

       #  VERTICALLY ALIGNMENT TEXT
       # label.setAlignment(Qt.AlignTop)       # TOP
       # label.setAlignment(Qt.AlignBottom)    # BOTTOM
       # label.setAlignment(Qt.AlignVCenter)   # CENTER

       #  HORIZONTALLY ALIGNMENT TEXT
       # label.setAlignment(Qt.AlignRight)     # RIGHT
       # label.setAlignment(Qt.AlignLeft)      # LEFT
       # label.setAlignment(Qt.AlignHCenter)   # CENTER


       # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
       # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
       # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
       # label.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
       # label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
