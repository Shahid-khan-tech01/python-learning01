# PYQT5 CHECKBOXES IN PYTHON

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MY FIRST GUI!")
        self.setWindowIcon(QIcon("profile.jpg"))
        self.setGeometry(700, 300, 500, 500)
        self.CheckBox = QCheckBox("Do You like it?", self)
        self.initUI()

    def initUI(self):
        self.CheckBox.setGeometry(10,0,500,100)
        self.CheckBox.setChecked(False)
        self.CheckBox.setStyleSheet("font-size:20px;"
                                    "font-family:Arial;")
        self.CheckBox.stateChanged.connect(self.check)

    def check(self, state):
        if state == Qt.Checked:
            print("Yes! You like it")
        else:
            print("No, You Do Not like it")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
