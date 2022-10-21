from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
from PyQt6 import uic

from controller import Controller


class View(QMainWindow):
    """
    Zeigt die GUI an und kümmert sich um Änderungen
    """

    def __init__(self, c: Controller):
        super().__init__()
        uic.loadUi("/home/phillip/PycharmProjects/the_opssat_case_starter_kit/human_classifier/client/mainwindow.ui", self)
        self.pb_agricultural.clicked.connect(c.agr)
        self.pb_cloud.clicked.connect(c.clo)
        self.pb_mountain.clicked.connect(c.mou)
        self.pb_natural.clicked.connect(c.nat)
        self.pb_none.clicked.connect(c.non)
        self.pb_river.clicked.connect(c.riv)
        self.pb_sea_ice.clicked.connect(c.sea)
        self.pb_snow.clicked.connect(c.sno)
        self.pb_water.clicked.connect(c.wat)

    def setNextImage(self, next_image: str):
        if next_image is None:
            self.p1Choice.setText('You are done classifieing')
        pix = QPixmap()
        pix.load(next_image)
        self.p1Choice.setPixmap(pix)

