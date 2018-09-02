'''
mesoSPIM CameraWindow

'''
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.uic import loadUi

import pyqtgraph as pg
import numpy as np

class mesoSPIM_CameraWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        '''Set up the UI'''
        loadUi('gui/mesoSPIM_CameraWindow.ui', self)
        self.setWindowTitle('mesoSPIM-Control: Camera Window')

        ''' Set histogram Range '''
        self.graphicsView.setLevels(100,4000)

        self.imageItem = self.graphicsView.getImageItem()

        self.histogram = self.graphicsView.getHistogramWidget()
        self.histogram.setMinimumWidth(250)
        self.histogram.item.vb.setMaximumWidth(250)

        ''' Initialize crosshairs '''
        self.crosspen = pg.mkPen({'color': "r", 'width': 1})
        self.vLine = pg.InfiniteLine(pos=1024, angle=90, movable=False, pen=self.crosspen)
        self.hLine = pg.InfiniteLine(pos=1024, angle=0, movable=False, pen=self.crosspen)
        self.graphicsView.addItem(self.vLine, ignoreBounds=True)
        self.graphicsView.addItem(self.hLine, ignoreBounds=True)

    @QtCore.pyqtSlot(str)
    def display_status_message(self, string, time=0):
        '''
        Displays a message in the status bar for a time in ms

        If time=0, the message will stay.
        '''

        if time == 0:
            self.statusBar().showMessage(string)
        else:
            self.statusBar().showMessage(string, time)

    def draw_crosshairs(self):
        self.graphicsView.addItem(self.vLine, ignoreBounds=True)
        self.graphicsView.addItem(self.hLine, ignoreBounds=True)

    @QtCore.pyqtSlot(np.ndarray)
    def set_image(self, image):
        self.graphicsView.setImage(image, autoLevels=False, autoHistogramRange=False, autoRange=False)
        self.draw_crosshairs()