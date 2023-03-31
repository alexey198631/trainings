from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QComboBox
import sys
from PyQt6 import uic


class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi('23_combo_box_from_designer.ui', self)
        self.label_ch = self.findChild(QLabel, 'label_ch')
        self.combo = self.findChild(QComboBox, 'comboBox')
        self.combo.currentTextChanged.connect(self.combo_changed)

    def combo_changed(self):
        item = self.combo.currentText()
        self.label_ch.setText('Your Language: ' + item)


app = QApplication(sys.argv)
window = UI()
window.show()

sys.exit(app.exec())