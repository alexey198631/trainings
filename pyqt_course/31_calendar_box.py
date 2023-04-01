from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt6.QtGui import QIcon, QFont
import sys

# object oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 400)  # x, y, width, height
        self.setWindowTitle('Calendar Widget')
        self.setWindowIcon(QIcon('data_files/icons8-netherlands-48.png'))
        #self.setFixedWidth(800)
        #self.setFixedHeight(400)
        self.setStyleSheet('background-color:red')
        self.setWindowOpacity(0.99)

        vbox = QVBoxLayout()

        self.calendar_widget = QCalendarWidget()
        self.calendar_widget.setGridVisible(True)
        self.calendar_widget.selectionChanged.connect(self.set_date)
        self.label = QLabel()



        vbox.addWidget(self.calendar_widget)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def set_date(self):
        dateSelected = self.calendar_widget.selectedDate()
        date_string = str(dateSelected.toPyDate())
        self.label.setText(date_string)



app = QApplication(sys.argv)

# setting icon for app
icon = QIcon("data_files/icons8-netherlands-48.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())