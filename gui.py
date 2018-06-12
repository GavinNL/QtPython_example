#!/usr/bin/env python3

import sys
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore

from MyWidget import MyWidget

# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':

    app = QtGui.QApplication([])

    # Create a main window
    main_window = QtGui.QMainWindow()
    main_window.resize(1024, 768)

    # Create the central widget which will store all child widgets
    central_widget = QtGui.QWidget()
    central_widget.setLayout(QtGui.QVBoxLayout()) # We want to use a VBoxLayout
    main_window.setCentralWidget(central_widget)

    # show the main window
    main_window.show()

    # Add 2 widgets to the main window.
    myWidget1 = MyWidget()
    myWidget2 = MyWidget()
    central_widget.layout().addWidget(myWidget1)
    central_widget.layout().addWidget(myWidget2)

    main_window.show()


    # Create a new widget by itself as a new window
    myWidget3 = MyWidget()
    myWidget3.show()


    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
