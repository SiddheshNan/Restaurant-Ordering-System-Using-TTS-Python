import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QFrame
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot


def window(text):
   w = 900; h = 600
   app = QApplication(sys.argv)
   widget = QWidget()

   textLabel = QLabel(widget)
   textLabel.setFont(QFont('Arial', 30))
   textLabel.setText(text)
   textLabel.move(175,130)
   widget.setGeometry(50,50,500,500)
   widget.setWindowTitle("Payment System")
   widget.show()
   sys.exit(app.exec_())
   return text

if __name__ == '__main__':
   thing = window("gyo")
   inp = input("somthin")
   new = thing + " " + inp
   print(new)
   thing = window(new)
   sys.exit(app.exec_())