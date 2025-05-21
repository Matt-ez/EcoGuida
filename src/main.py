from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap,QIcon
from PyQt6.uic import *
import time



class Window(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("GUI/main.ui",self)
    
    def apertura(self):
        self.setWindowTitle("EcoGuida - Benvenuto!")
        self.setWindowIcon(QIcon("GUI/Logo.png"))
        self.show()

class Landing(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("GUI/Landing.ui", self)
        self.setWindowTitle("EcoGuida - Benvenuto!")
        self.setWindowIcon(QIcon("GUI/Logo.png"))
        self.show()
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
        Window.apertura(self)
        self.progressBar.setValue(100)
        time.sleep(0.5)
        self.close()

