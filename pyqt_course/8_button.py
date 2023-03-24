from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


# object-oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 400)  # x, y, width, height
        self.setWindowTitle('learning buttons')
        self.setWindowIcon(QIcon('data_files/python.png'))
        self.create_button()

    def create_button(self):
        btn = QPushButton('Push me', self)
        btn.setGeometry(10, 10, 150, 100)
        btn.setFont(QFont('Times New Roman', 14, QFont.Weight.ExtraBold))
        btn.setIcon(QIcon('data_files/python.png'))
        btn.setIconSize(QSize(24, 24))

        # menu
        menu = QMenu()
        menu.setFont(QFont('Times New Roman', 14, QFont.Weight.ExtraLight))
        menu.setStyleSheet('background-color:lightblue')
        menu.addAction('Copy')
        menu.addAction('Cut')
        menu.addAction('Paste')
        btn.setMenu(menu)


app = QApplication(sys.argv)

# setting icon for app
icon = QIcon("data_files/python.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())
