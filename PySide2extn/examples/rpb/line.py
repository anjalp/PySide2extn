import sys
from PySide2 import QtCore, QtWidgets, QtGui
#IMPORTING THE MODULE
from RoundProgressBar import roundProgressBar

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        
        #CLASS INSTANCE
        self.rpb = roundProgressBar()
        self.rpb2 = roundProgressBar()
        self.rpb3 = roundProgressBar()

        #LINE WIDTH 
        self.rpb.rpb_setLineWidth(10)

        #LINE CAP
        self.rpb.rpb_setLineCap('RoundCap')
        self.rpb2.rpb_setLineCap('SquareCap')
        self.rpb3.rpb_setLineCap('RoundCap')

        #LINE STYLE
        self.rpb3.rpb_setLineStyle('DotLine')
        self.rpb2.rpb_setLineStyle('DashLine')
        
        #SETTING THE VALUE
        self.rpb.rpb_setValue(85)
        self.rpb2.rpb_setValue(85)
        self.rpb3.rpb_setValue(85)

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