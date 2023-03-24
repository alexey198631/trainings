from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont
import sys

# object oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 400)  # x, y, width, height
        self.setWindowTitle('horizontal box layout')
        self.setWindowIcon(QIcon('data_files/python.png'))

        hbox = QHBoxLayout()
        for i in range(1, 5):
            btn = QPushButton(f'Click {i}')
            hbox.addWidget(btn)

        #hbox.addSpacing(100)
        hbox.addStretch(5)
        self.setLayout(hbox)


app = QApplication(sys.argv)

#setting icon for app
icon = QIcon("data_files/python.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())