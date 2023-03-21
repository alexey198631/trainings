from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar
import sys


app = QApplication(sys.argv)

window = QMainWindow()
window.statusBar().showMessage('I am learning PyQt') #QWidget doesn't have status bar
file_menu = window.menuBar().addMenu("File")
file_menu.addAction("New")
file_menu.addAction("Open")
file_menu.addAction("Save")
file_menu.addAction('Finish')


window.show()

sys.exit(app.exec())