from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys


# object oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 400)  # x, y, width, height
        self.setWindowTitle('event handling')
        self.setWindowIcon(QIcon('data_files/python.png'))

        self.create_widget()

    def create_widget(self):
        hbox = QHBoxLayout()
        btn = QPushButton('Change text')
        btn.clicked.connect(self.clicked_btn)
        self.label = QLabel('Default text')
        hbox.addWidget(btn)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def clicked_btn(self):  # new text after clicking button
        self.label.setText('New text')
        self.label.setFont(QFont('Arial', 16))
        self.label.setStyleSheet('color:blue')


app = QApplication(sys.argv)

# setting icon for app
icon = QIcon("data_files/python.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())
