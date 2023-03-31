from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys


# object oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.combo = None
        self.setGeometry(100, 100, 500, 200)  # x, y, width, height
        self.setWindowTitle('combo box')
        self.setWindowIcon(QIcon('data_files/python.png'))

        self.create_combo()

    def create_combo(self):
        hbox = QHBoxLayout()
        label = QLabel('Select Account Type')
        label.setFont(QFont('Arial', 16))
        self.combo = QComboBox()
        self.combo.addItem('')
        self.combo.addItem('Key Account')
        self.combo.addItem('Regional Account')
        self.combo.addItem('Channel Partner')
        self.combo.currentTextChanged.connect(self.combo_changed)

        vbox = QVBoxLayout()
        self.label_result = QLabel()
        self.label_result.setFont(QFont('Arial', 16))
        vbox.addWidget(self.label_result)
        vbox.addLayout(hbox)


        hbox.addWidget(label)
        hbox.addWidget(self.combo)

        self.setLayout(vbox)

    def combo_changed(self):
        item = self.combo.currentText()
        self.label_result.setText('Your Account Type is: ' + item)






app = QApplication(sys.argv)

# setting icon for app
icon = QIcon("data_files/python.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())