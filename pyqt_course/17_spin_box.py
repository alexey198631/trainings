from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QSpinBox, QLineEdit
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


# object oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 100)  # x, y, width, height
        self.setWindowTitle('Spin Box')
        self.setWindowIcon(QIcon('data_files/python.png'))

        hbox = QHBoxLayout()

        label = QLabel('Product # 1: ', self)
        label.setFont(QFont('Arial', 16))

        self.lineedit = QLineEdit()
        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.spin_selected)
        self.total = QLineEdit()

        hbox.addWidget(label)
        hbox.addWidget(self.lineedit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.total)


        self.setLayout(hbox)


    def spin_selected(self):
        if self.lineedit != 0:
            price = int(self.lineedit.text())
            total_price = self.spinbox.value() * price

            self.total.setText(str(total_price))
        else:
            print('Wrong value!')


app = QApplication(sys.argv)

# setting icon for app
icon = QIcon("data_files/python.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())
