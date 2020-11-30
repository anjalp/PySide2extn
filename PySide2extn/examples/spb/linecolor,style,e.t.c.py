import sys
from PySide2 import QtCore, QtWidgets, QtGui

from PySide2extn.SpiralProgressBar import spiralProgressBar #IMPORT THE EXTENSION LIBRARY

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.hello = 'Spiral Progress Bar'
        
        self.spbN = spiralProgressBar()    #SPIRAL PROGRESSBAR OBJECT
        self.spbN.spb_setNoProgressBar(4)
        
        #LINE WIDTH: 15px
        self.spbN.spb_lineWidth(15)
        self.spbN.spb_setGap(17)

        #LINE COLOR
        self.spbN.spb_lineColor(((0, 125, 125), (125, 0, 125), (125, 255, 0), (125, 125, 125)))

        #LINE STYLE
        self.spbN.spb_lineStyle(('SolidLine', 'DotLine', 'DashLine', 'SolidLine'))

        #LINE CAP
        self.spbN.spb_lineCap(('SquareCap', 'RoundCap', 'RoundCap', 'SquareCap'))

        self.spbN.spb_setValue((55, 55, 55, 55))

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.spbN)
        self.setLayout(self.layout)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())