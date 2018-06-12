#!/usr/bin/env python3

import sys
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore

from MyWidget import MyWidget
from widget1 import Widget1

# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':

    app = QtGui.QApplication([])


    main_window = QtGui.QMainWindow()
    main_window.resize(1024, 768)
    central_widget = QtGui.QWidget()
    central_widget.setLayout(QtGui.QVBoxLayout())
    main_window.setCentralWidget(central_widget)


    main_window.show()

    w = Widget1()
    central_widget.layout().addWidget( w )
    w = Widget1()
    central_widget.layout().addWidget( w )

    #myWidget1 = MyWidget()
    #myWidget2 = MyWidget()

    #central_widget.layout().addWidget(myWidget1)
    #central_widget.layout().addWidget(myWidget2)
    #myWidget2.show()
    #main_window.show()

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
