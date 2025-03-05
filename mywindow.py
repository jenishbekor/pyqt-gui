from PyQt6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel
import os
from PyQt6 import uic
from model import CalculatorModel

class CalculatorWindow(QMainWindow):

    input : QLineEdit
    button0: QPushButton
    button1 : QPushButton
    button2: QPushButton
    button3: QPushButton
    button4: QPushButton
    buttonc: QPushButton
    buttone :QPushButton
    buttonp : QPushButton
    buttonm : QPushButton
    buttonx : QPushButton
    buttond: QPushButton


    def __init__(self):
        super().__init__()

        ui_path = os.path.join(os.path.dirname(__file__), "calc.ui")
        uic.loadUi(ui_path, self)

        self.calculator = CalculatorModel()
        self.button1.clicked.connect(lambda:self.on_click_digit('1'))
        self.button2.clicked.connect(lambda:self.on_click_digit('2'))
        self.button3.clicked.connect(lambda: self.on_click_digit('3'))
        self.button0.clicked.connect(lambda: self.on_click_digit('0'))

        self.buttonp.clicked.connect(lambda: self.on_click_operator('+'))
        self.buttonm.clicked.connect(lambda: self.on_click_operator('-'))
        self.buttonx.clicked.connect(lambda: self.on_click_operator('*'))
        self.buttond.clicked.connect(lambda: self.on_click_operator('/'))

        self.buttone.clicked.connect(self.on_click_eqaul)

        self.buttonc.clicked.connect(self.on_click_clear)

    def on_click_digit(self, digit):
        self.calculator.add_to_expression(digit)
        self.input.setText(self.calculator.get_expression())

    def on_click_operator(self, op):
        self.calculator.add_to_expression(op)
        self.input.setText(self.calculator.get_expression())

    def on_click_eqaul(self):
        self.calculator.calculate()
        self.input.setText(self.calculator.get_expression())

    def on_click_clear(self):
        self.calculator.clear_expression()
        self.input.setText(self.calculator.get_expression())
