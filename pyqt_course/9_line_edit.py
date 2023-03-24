from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont
import sys

# object oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 400)  # x, y, width, height
        self.setWindowTitle('line edit')
        self.setWindowIcon(QIcon('data_files/python.png'))

        line_edit = QLineEdit(self)
        line_edit.move(10, 10)
        line_edit.setFont(QFont('Arial', 10))
        #line_edit.setText('Type here') # default text
        line_edit.setPlaceholderText('Please type here...') # guidance text
        #line_edit.setEnabled(False)
        line_edit.setEchoMode(QLineEdit.EchoMode.Password) # setting code


app = QApplication(sys.argv)

#setting icon for app
icon = QIcon("data_files/python.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())

