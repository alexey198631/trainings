# it is possible to convert file through terminal
#pyuic6 -x file_name.ui -o 5_py_file_name.py

from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic


class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('5_test_designer.ui', self)


app = QApplication(sys.argv)
window = UI()
window.show()

sys.exit(app.exec())
