import sys
from PyQt6.QtWidgets import QApplication
from mywindow import CalculatorWindow

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = CalculatorWindow()
   window.show()
   app.exec()


