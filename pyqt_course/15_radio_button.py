from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QRadioButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

# object oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 200, 100)  # x, y, width, height
        self.setWindowTitle('radio button')
        self.setWindowIcon(QIcon('data_files/python.png'))

        self.create_radio()

    def create_radio(self):
        hbox = QHBoxLayout()
        radio_1 = QRadioButton('Python')
        radio_1.setIcon(QIcon('data_files/python.png'))
        radio_1.setIconSize(QSize(40, 40))
        radio_1.setFont(QFont('Arial', 12))
        radio_1.setChecked(True)
        radio_1.toggled.connect(self.radio_selected)
        hbox.addWidget(radio_1)

        self.label = QLabel('Hello')
        self.label.setFont(QFont('Arial', 12))

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def radio_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label.setText(f'You have selected {radio_btn.text()}')



app = QApplication(sys.argv)

#setting icon for app
icon = QIcon("data_files/python.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())