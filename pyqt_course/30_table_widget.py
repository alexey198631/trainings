from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys

# object oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 400)  # x, y, width, height
        self.setWindowTitle('Table Widget')
        self.setWindowIcon(QIcon('data_files/icons8-netherlands-48.png'))
        #self.setFixedWidth(800)
        #self.setFixedHeight(400)
        #self.setStyleSheet('background-color:lightblue')
        self.setWindowOpacity(0.9)

        vbox = QVBoxLayout()

        table_widget = QTableWidget()
        table_widget.setRowCount(3)
        table_widget.setColumnCount(3)

        table_widget.setItem(0, 0, QTableWidgetItem('Language'))
        table_widget.setItem(0, 1, QTableWidgetItem('Course'))
        table_widget.setItem(0, 2, QTableWidgetItem('Duration'))

        table_widget.setItem(1, 0, QTableWidgetItem('English'))
        table_widget.setItem(1, 1, QTableWidgetItem('C1'))
        table_widget.setItem(1, 2, QTableWidgetItem('1 month'))

        table_widget.setItem(2, 0, QTableWidgetItem('English'))
        table_widget.setItem(2, 1, QTableWidgetItem('C2'))
        table_widget.setItem(2, 2, QTableWidgetItem('1 year'))

        vbox.addWidget(table_widget)
        self.setLayout(vbox)


app = QApplication(sys.argv)

# setting icon for app
icon = QIcon("data_files/icons8-netherlands-48.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())