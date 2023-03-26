from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QCheckBox
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

# object oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 200, 100)  # x, y, width, height
        self.setWindowTitle('Ckeck Box')
        self.setWindowIcon(QIcon('data_files/python.png'))

        hbox = QHBoxLayout()
        options = ['Python', 'Dutch', 'Sport', 'Movie']

        self.check_1 = QCheckBox(f'{options[0]}')
        self.check_1.setIcon(QIcon('data_files/python.png'))
        self.check_1.setFont(QFont('Arial', 20))
        self.check_1.setIconSize(QSize(32, 32))
        self.check_1.stateChanged.connect(self.item_selected)
        hbox.addWidget(self.check_1)

        self.check_2 = QCheckBox(f'{options[1]}')
        self.check_2.setIcon(QIcon('data_files/python.png'))
        self.check_2.setFont(QFont('Arial', 20))
        self.check_2.setIconSize(QSize(32, 32))
        self.check_2.stateChanged.connect(self.item_selected)
        hbox.addWidget(self.check_2)



        self.label = QLabel('')
        self.label.setFont(QFont('Arial', 24))
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


    def item_selected(self):
        value = ''
        if self.check_1.isChecked():
            value = self.check_1.text()
        elif self.check_2.isChecked():
            value = self.check_2.text()

        self.label.setText('You have selected: ' + value)







app = QApplication(sys.argv)

#setting icon for app
icon = QIcon("data_files/python.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())