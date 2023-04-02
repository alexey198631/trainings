from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu, QMessageBox
from PyQt6.QtGui import QIcon, QFont, QAction
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

        # add the "Copy" action to the menu
        copy_action = QAction('Copy', self)
        copy_action.triggered.connect(self.handle_copy_action)
        menu.addAction(copy_action)

        # add the "Cut" action to the menu
        cut_action = QAction('Cut', self)
        cut_action.triggered.connect(self.handle_cut_action)
        menu.addAction(cut_action)

        # add the "Paste" action to the menu
        paste_action = QAction('Paste', self)
        paste_action.triggered.connect(self.handle_paste_action)
        menu.addAction(paste_action)

        btn.setMenu(menu)

    def handle_copy_action(self):
        QMessageBox.warning(self, 'Copy', 'You selected Copy')

    def handle_cut_action(self):
        QMessageBox.information(self, 'Cut', 'You selected Cut')

    def handle_paste_action(self):
        QMessageBox.about(self, 'Paste', 'You selected Paste')


app = QApplication(sys.argv)

# setting icon for app
icon = QIcon("data_files/python.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())
