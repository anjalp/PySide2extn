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
        self.rpb3 = roundProgressBar()

        #SETTING THE RANGE : MIN-0 & MAX:360
        self.rpb.rpb_setMaximum(720)
        self.rpb2.rpb_setRange(0, 720)
        self.rpb3.rpb_setRange(0, 1000)
        
        #SETTING THE VALUE
        self.rpb.rpb_setValue(456)
        self.rpb2.rpb_setValue(456)
        self.rpb3.rpb_setValue(890)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.rpb)
        self.layout.addWidget(self.rpb2)
        self.layout.addWidget(self.rpb3)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())