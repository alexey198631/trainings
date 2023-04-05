from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys

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

        label = QLabel('My first label', self)
        font = QFont("Arial", 16)  # create a QFont object
        label.setFont(font)  # set the font for the label

        # set the text color to white
        label.setStyleSheet("color: white;")
        #label.setText('The second text')
        label.move(10, 10)
        #label.setNum(100) #setting text in int
        #label.clear() #clear the text

        label_2 = QLabel(self)
        pixmap = QPixmap('data_files/python.png')

        scaled_pixmap = pixmap.scaled(pixmap.width() // 3,
                                      pixmap.height() // 3)  # decrease the size of the pixmap by a factor of 2
        label_2.setPixmap(scaled_pixmap)
        label_2.setFixedSize(scaled_pixmap.size())
        label_2.move(10, 30)

app = QApplication(sys.argv)

#setting icon for app
icon = QIcon("data_files/icons8-netherlands-48.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())