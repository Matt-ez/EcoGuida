from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap,QIcon
from PyQt6.uic import *
import time
from src.text import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("GUI/main.ui",self)
        self.setWindowTitle("EcoGuida 2025")
        self.setWindowIcon(QIcon("images/Logo_EcoGuida.png"))
        self.show()
        self.pushSelect.clicked.connect(self.parcoChanger)
        self.comboParchi.currentTextChanged.connect(lambda: self.comboParchi.setStyleSheet("QComboBox { background-color: #ffffff}"))
        
    def parcoChanger(self):
        self.comboParchi.setStyleSheet("QComboBox { background-color: #bbf78f}")
        if self.comboParchi.currentText()=="Parco Nazionale del Gran Paradiso":
            self.granParadiso()
    def granParadiso(self):
        self.pushFlora.clicked.connect(lambda: self.label.setText(floraGranParadiso))
        self.pushFauna.clicked.connect(lambda: self.label.setText(faunaGranParadiso))
        self.pushActivity.clicked.connect(lambda: self.label.setText(activityGranParadiso))
        self.pushRegole.clicked.connect(lambda: self.label.setText(regoleGranParadiso))

class Landing(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("GUI/landing.ui", self)
        self.setWindowTitle("EcoGuida - Benvenuto!")
        self.setWindowIcon(QIcon("images/Logo_EcoGuida.png"))
        self.pushEntra.clicked.connect(self.openApp)

    def openApp(self):
        self.progressBar.setValue(0)
        time.sleep(0.5)
        self.progressBar.setValue(25)
        time.sleep(1)
        self.progressBar.setValue(50)
        time.sleep(0.25)
        self.progressBar.setValue(75)
        time.sleep(0.2)
        self.win = Window()
        self.progressBar.setValue(100)
        time.sleep(0.5)
        self.close()