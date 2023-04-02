from PyQt6.QtWidgets import QApplication, QDialog, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QInputDialog
from PyQt6.QtGui import QIcon, QFont
import sys

# object oriented concept
class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 400)  # x, y, width, height
        self.setWindowTitle('Dialogue Input')
        self.setWindowIcon(QIcon('data_files/icons8-netherlands-48.png'))

        self.create_dialog()

    def create_hobby_input(self, btn_func, initial_text):

        hbox = QHBoxLayout()

        self.label = QLabel()
        self.lineedit = QLineEdit()
        self.btn = QPushButton()

        self.label.setFont(QFont('Arial', 16))
        self.label.setText('Choose your hobby: ')
        self.btn.setText('Enter')
        self.btn.setFont(QFont('Arial', 16))
        self.lineedit.setFont(QFont('Arial', 16))
        self.lineedit.setText(initial_text)


        hbox.addWidget(self.label)
        hbox.addWidget(self.lineedit)
        hbox.addWidget(self.btn)

        self.btn.clicked.connect(btn_func)

        return hbox

    def show_dialogue(self, options):
        temp = ''
        hobby, ok = QInputDialog.getItem(self, 'Input Data', 'List of hobbies', options, 0, False)
        if hobby and ok:
            temp = hobby
        return temp

    def get_text(self, label_text):
        temp = ''
        name, ok = QInputDialog.getText(self, label_text, f'Enter {label_text}: ')
        if name and ok:
            temp = name
        return temp

    def get_int(self, label_text):
        temp = ''
        int_n, ok = QInputDialog.getInt(self, label_text, f'Enter {label_text}: ')
        if int_n and ok:
            temp = str(int_n)
        return temp

    def create_dialog(self):
        vbox = QVBoxLayout()
        # get initial text for each hobby input
        hobbies = ['Python', 'Sport', 'English', 'Dutch']
        hobby_input_text = self.show_dialogue(hobbies)
        name_input_text = self.get_text('Your Name')
        number_input_text = self.get_int('Your Number')
        # define lambda functions for button callbacks
        hobby_callback = lambda: self.show_dialogue(hobbies)
        name_callback = lambda: self.get_text('Your Name')
        number_callback = lambda: self.get_int('Your Number')

        hbox1 = self.create_hobby_input(hobby_callback, hobby_input_text)
        hbox2 = self.create_hobby_input(name_callback, name_input_text)
        hbox3 = self.create_hobby_input(number_callback, number_input_text)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)


app = QApplication(sys.argv)

# setting icon for app
icon = QIcon("data_files/icons8-netherlands-48.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())