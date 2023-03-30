from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLCDNumber
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTime, QTimer
import sys


# object oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 400)  # x, y, width, height
        self.setWindowTitle('LCD number')
        self.setWindowIcon(QIcon('data_files/python.png'))

        self.showLCD()

    def showLCD(self):
        vbox = QVBoxLayout()
        lcd = QLCDNumber()
        lcd.setDigitCount(8)  # set the number of digits to 8 to display hh:mm:ss
        lcd.setStyleSheet('background-color: lightblue')
        vbox.addWidget(lcd)

        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')
        lcd.display(text)

        # update the time every second
        timer = QTimer(self)
        timer.timeout.connect(lambda: lcd.display(QTime.currentTime().toString('hh:mm:ss')))
        timer.start(1000)

        self.setLayout(vbox)


app = QApplication(sys.argv)

# setting icon for app
icon = QIcon("data_files/python.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())
