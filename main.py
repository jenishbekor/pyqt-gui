import sys
from PyQt6.QtWidgets import QApplication
from mywindow import MyWindow

if __name__ == '__main__':
   app = QApplication(sys.argv)

   with open("Irrorater.qss", "r") as f:
      app.setStyleSheet(f.read())

   window = MyWindow()
   window.show()
   app.exec()


