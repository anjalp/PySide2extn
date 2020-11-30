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

        #CHANGING THE PROGRESSABR STYLE
        self.rpb.rpb_setBarStyle('Hybrid1')

        #CHANGING THE LINE COLOR AND WIDTH
        self.rpb.rpb_setLineWidth(3)
        self.rpb2.rpb_setLineWidth(8)

        #PATH WIDTH
        self.rpb.rpb_setPathWidth(15)
        self.rpb2.rpb_setPathWidth(2)

        #CHANGING THE PATH COLOR
        self.rpb.rpb_setPathColor((125, 255, 255))
        self.rpb2.rpb_setPathColor((0, 0, 0))
        
        #SETTING THE VALUE
        self.rpb.rpb_setValue(85)
        self.rpb2.rpb_setValue(85)


        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.rpb)
        self.layout.addWidget(self.rpb2)

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())