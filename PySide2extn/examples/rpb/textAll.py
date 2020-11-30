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
        self.rpb.rpb_setRange(0, 360) 
        self.rpb2.rpb_setRange(0, 360)
        self.rpb3.rpb_setRange(0, 360)
        
        #CHANGING THE STYLE
        self.rpb.rpb_setBarStyle('Pizza')
        self.rpb2.rpb_setBarStyle('Hybrid2')

        #CHANGING THE TEXT TYPE : VALUE OR PERCENTAGE
        self.rpb.rpb_setTextFormat('Value')
        self.rpb2.rpb_setTextFormat('Percentage')

        #CHANGING THE TEXT SIZE
        self.rpb.rpb_setTextRatio(3)
        self.rpb2.rpb_setTextRatio(9)

        #CHANGING THE FONT
        self.rpb.rpb_setTextFont('Arial')
        self.rpb2.rpb_setTextFont('Times New Roman')

        #TEXT HIDDEN
        self.rpb3.rpb_enableText(False)
        
        #SETTING THE VALUE
        self.rpb.rpb_setValue(156)
        self.rpb2.rpb_setValue(156)

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