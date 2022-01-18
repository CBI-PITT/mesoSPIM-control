import cv2
import numpy as np
import pyqtgraph as pg

import logging
logger = logging.getLogger(__name__)

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.uic import loadUi
from PyQt5.QtMultimedia import QCameraInfo, QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder


class WebcamWindow(QtWidgets.QWidget):
    sig_state_request = QtCore.pyqtSignal(dict)
    sig_move_absolute = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None):
        '''Parent must be an mesoSPIM_MainWindow() object'''
        super().__init__()
        self.parent = parent # the mesoSPIM_MainWindow() object
        loadUi('gui/WebcamWindow.ui', self)
        self.setWindowTitle('Webcam view')
        self.show()
        self.start_capture()

    def start_capture(self):
        webcams = QCameraInfo.availableCameras()
        print(f"Webcams found: {len(webcams)}")
        if len(webcams) > 0:
            self.webcam = QCamera(webcams[0])
            self.webcam.setCaptureMode(QCamera.CaptureViewfinder)
            #self.viewfinder = QCameraViewfinder() # this object is defined inside the WebcamWindow.ui file
            self.webcam.setViewfinder(self.viewfinder)
            self.webcam.start()
            self.viewfinder.show()
