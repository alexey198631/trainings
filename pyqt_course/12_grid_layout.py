from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys


# object oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 400)  # x, y, width, height
        self.setWindowTitle('grid layout')
        self.setWindowIcon(QIcon('data_files/python.png'))

        grid = QGridLayout()
        for i in range(1, 26):
            btn = QPushButton(f'word {i}')
            row = (i - 1) // 5  # calculate the row index
            col = (i - 1) % 5  # calculate the column index
            grid.addWidget(btn, row, col)

        self.setLayout(grid)




app = QApplication(sys.argv)

# setting icon for app
icon = QIcon("data_files/python.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())