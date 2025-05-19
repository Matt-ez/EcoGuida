from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap,QIcon
from PyQt6.uic import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("GUI/main.ui",self)

