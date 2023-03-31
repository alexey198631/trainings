from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys

# object oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 400)  # x, y, width, height
        self.setWindowTitle('Learning List Box')
        self.setWindowIcon(QIcon('data_files/icons8-netherlands-48.png'))
        #self.setFixedWidth(800)
        #self.setFixedHeight(400)
        #self.setStyleSheet('background-color:lightblue')
        self.setWindowOpacity(0.9)

        vbox = QVBoxLayout()

        self.list_widget = QListWidget()
        self.list_widget.insertItem(0, 'English')
        self.list_widget.insertItem(1, 'Spanish')
        self.list_widget.insertItem(2, 'Russian')
        self.list_widget.insertItem(3, 'Dutch')

        self.list_widget.itemClicked.connect(self.pick_list_value)

        self.label = QLabel()

        vbox.addWidget(self.list_widget)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def pick_list_value(self):
        value = self.list_widget.currentItem()
        self.label.setText('Your choice: ' + value.text())


app = QApplication(sys.argv)

# setting icon for app
icon = QIcon("data_files/icons8-netherlands-48.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())