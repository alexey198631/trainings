from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QDoubleSpinBox
import sys
from PyQt6 import uic


class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('18_spin_box_with_designer.ui', self)

        # accessing to object on the widget generated through ui loading 
        self.linePrice = self.findChild(QLineEdit, 'lineEdit')
        self.doublespin = self.findChild(QDoubleSpinBox, 'doubleSpinBox')
        self.result = self.findChild(QLineEdit, 'lineEdit_total')

        # changing increment value from standard 1 to 0.01
        self.doublespin.setSingleStep(0.01)

        self.doublespin.valueChanged.connect(self.spin_selected)

    def spin_selected(self):
        if self.linePrice != 0:
            price = int(self.linePrice.text())
            total_price = self.doublespin.value() * price

            self.result.setText(str(total_price))
        else:
            print('Wrong value!')


app = QApplication(sys.argv)
window = UI()
window.show()

sys.exit(app.exec())
