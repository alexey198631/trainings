import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QSizePolicy
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys
import random

words = pd.read_excel('data_files/init_words.xlsx', sheet_name='words')
w = {}
for i in range(50):
    w[words.loc[i, 'word']] = words.loc[i, 'translation']

choice = random.sample(list(w.items()), 25)

# object oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 400)  # x, y, width, height
        self.setWindowTitle('labels')
        self.setWindowIcon(QIcon('data_files/icons8-netherlands-48.png'))
        #self.setFixedWidth(800)
        #self.setFixedHeight(400)
        self.setStyleSheet('background-color:lightblue')
        self.setWindowOpacity(0.99)

        grid = QGridLayout()
        for i, p in enumerate(choice):
            print(i,p)
            label = QLabel(f'{p[0]}\n{p[1]}', self)
            label.move(50, 0)
            label.setStyleSheet("color: black;")
            font = QFont("Arial", 16)  # create a QFont object
            label.setFont(font)  # set the font for the label
            row = (i - 1) // 5  # calculate the row index
            col = (i - 1) % 5  # calculate the column index
            grid.addWidget(label, row, col)

        self.setLayout(grid)


        #label.clear() #clear the text





app = QApplication(sys.argv)

#setting icon for app
icon = QIcon("data_files/icons8-netherlands-48.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())




