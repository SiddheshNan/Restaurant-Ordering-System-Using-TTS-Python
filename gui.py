import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time


class App(QWidget):
    def __init__(self, parent=None):
        super(App, self).__init__(parent=parent)  # these values change where the main window is placed
        self.title = 'Payment System'
        self.left = 600
        self.top = 400
        self.width = 600
        self.height = 400
        self.setStyleSheet("QLabel {font: 30pt Roboto}")
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createGridLayout()
        self.time_label.text = 'Welcome to Payment System'
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()  # this sets the main window to the screen size

    def createGridLayout(self):
        self.time_label = QLabel("Welcome here", self)
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.addWidget(self.time_label, 0, 2)
        self.horizontalGroupBox.setLayout(layout)


    def updateTime(self):
        time = self.thing
        self.time_label.setText(time)
        return time


def main():

    app = QApplication(sys.argv)
    ex = App()
    timer = QTimer()
    timer.timeout.connect(ex.updateTime)
    timer.start(1000)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()