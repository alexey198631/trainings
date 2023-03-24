from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys


# object oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 400)  # x, y, width, height
        self.setWindowTitle('vertical box layout')
        self.setWindowIcon(QIcon('data_files/python.png'))

        vbox = QVBoxLayout()
        for i in range(1, 5):
            btn = QPushButton(f'Click {i}')
            vbox.addWidget(btn)

        #vbox.addSpacing(100)
        vbox.addStretch(5)
        self.setLayout(vbox)


app = QApplication(sys.argv)

# setting icon for app
icon = QIcon("data_files/python.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())