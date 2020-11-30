import sys
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2extn.RoundProgressBar import roundProgressBar

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.rpb = roundProgressBar()
        self.rpb.rpb_setBarStyle('Pizza') #CHANGE THE BAR STYLE TO : 'Pizza'

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.rpb)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())