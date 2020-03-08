# This is a comment
import os
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.Qt3DExtras import Qt3DExtras
from PySide2.Qt3DCore import Qt3DCore
from PySide2.QtGui import QVector3D, QColor
from PySide2.Qt3DRender import Qt3DRender
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import QObject, Signal, Slot

import numpy as np


class MainWindow(QMainWindow):
    def __init__(self, simulator):
        super(MainWindow, self).__init__()
        self.simulator = simulator

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.echo)

    @Slot()
    def echo(self):
        self.simulator.run()

class Simulator(object):
    def __init__(self):
        pass

    def run(self):
        print('Running simulation')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    simulator = Simulator()
    window = MainWindow(simulator)
    window.show()

    sys.exit(app.exec_())
