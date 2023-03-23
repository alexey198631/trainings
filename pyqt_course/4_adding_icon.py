from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

# object oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 400)  # x, y, width, height
        self.setWindowTitle('learning GUI')
        self.setWindowIcon(QIcon('data_files/icons8-netherlands-48.png'))
        #self.setFixedWidth(800)
        #self.setFixedHeight(400)
        self.setStyleSheet('background-color:blue')
        self.setWindowOpacity(0.99)


app = QApplication(sys.argv)

#setting icon for app
icon = QIcon("data_files/icons8-netherlands-48.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())