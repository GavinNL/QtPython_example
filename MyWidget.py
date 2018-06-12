import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore

import time

__all__ = ['MyWidget']

WindowTemplate, TemplateBaseClass = pg.Qt.loadUiType( 'mywidget.ui')


class MyWidget(TemplateBaseClass):
    """

    PlotWindow widget is used to display plots for a stream.

    It allows you to enable/disable reference measurements for the processing script

    Also allows you to take measurements

    """
    def __init__(self):

        TemplateBaseClass.__init__(self)

        # Create the main window
        self.ui = WindowTemplate()
        self.ui.setupUi(self)


        # ==== Setup any Signal/Slots
        self.ui.horizontalSlider.valueChanged.connect( self.slider_slot )
        self.ui.lineEdit.textChanged.connect( self.ui.pushButton.setText )


    def slider_slot(self, value):
        self.ui.lineEdit.setText( "%d"%value )
        print(value)


