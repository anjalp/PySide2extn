import sys
from PySide2 import QtCore, QtWidgets, QtGui
#IMPORTING THE MODULE
from PySide2extn.RoundProgressBar import roundProgressBar

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        
        #CLASS INSTANCE
        self.rpb = roundProgressBar()
        self.rpb2 = roundProgressBar()
        
        #CHANGING THE DIRECTION
        self.rpb.rpb_setDirection('Clockwise')
        self.rpb2.rpb_setDirection('AntiClockwise')
        
        #SETTING THE VALUE
        self.rpb.rpb_setValue(56)
        self.rpb2.rpb_setValue(88)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.rpb)
        self.layout.addWidget(self.rpb2)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
        sys.exit(app.exec_())