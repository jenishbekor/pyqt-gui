from PyQt6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel
import os
from PyQt6 import uic
from model import SumModel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)
        self.label3 =  QLabel(self)
        self.button1 = QPushButton(self)

        self.summodel = SumModel()

        ui_path = os.path.join(os.path.dirname(__file__), "mygui.ui")
        uic.loadUi(ui_path, self)
        self.button1.clicked.connect(self.on_click)

    def on_click(self):
        val1 = int(self.input1.text())
        val2 = int(self.input2.text())

        self.summodel.set_operands(val1, val2)
        sum = self.summodel.calculate()

        self.label3.setText("Sum = " + str(sum))