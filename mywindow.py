from PyQt6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel
import os
from PyQt6 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)
        self.label3 =  QLabel(self)
        self.button1 = QPushButton(self)

        ui_path = os.path.join(os.path.dirname(__file__), "mygui.ui")
        uic.loadUi(ui_path, self)
        self.button1.clicked.connect(self.on_click)

    def on_click(self):
        val1 = self.input1.text()
        val2 = self.input2.text()
        sum = int(val1) + int(val2)
        self.label3.setText("Sum = " + str(sum))