from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QSlider, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys

# object oriented concept
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 400)  # x, y, width, height
        self.setWindowTitle('learning Sliders')
        self.setWindowIcon(QIcon('data_files/icons8-netherlands-48.png'))
        #self.setFixedWidth(800)
        #self.setFixedHeight(400)
        #self.setStyleSheet('background-color:lightblue')
        self.setWindowOpacity(0.99)

        hbox = QHBoxLayout()

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.setMaximum(100)
        self.slider.setMinimum(0)
        self.slider.setSingleStep(5)  # set the step size to 1
        self.slider.valueChanged.connect(self.changed_slider)
        self.label = QLabel()
        self.label.setFont(QFont('Arial', 16))
        self.label.setText('0')


        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def changed_slider(self):
        value = self.slider.value()
        self.label.setText(str(value))


app = QApplication(sys.argv)

# setting icon for app
icon = QIcon("data_files/icons8-netherlands-48.png")
app.setWindowIcon(icon)

window = Window()
window.show()
sys.exit(app.exec())