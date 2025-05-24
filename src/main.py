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
        self.scrollArea.setWidgetResizable(True)
        self.show()
        self.deSelect()
        self.selected = False
        self.pushSelect.clicked.connect(self.parcoChanger)
        self.comboParchi.currentTextChanged.connect(self.deSelect)
    
    def deSelect(self):
        self.selected = False
        self.label.setText("")
        self.pushFlora.clicked.connect(self.alert)
        self.pushFauna.clicked.connect(self.alert)
        self.pushActivity.clicked.connect(self.alert)
        self.pushRegole.clicked.connect(self.alert)
        self.comboParchi.setStyleSheet("QComboBox { background-color: #ffffff}")

    def alert(self):
        msg = QMessageBox()
        self.label.setText("")
        msg.setWindowTitle("Attenzione!")
        msg.setText("Il parco non è stato selezionato!")
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec()


    def parcoChanger(self):
        self.selected = True
        self.comboParchi.setStyleSheet("QComboBox { background-color: #bbf78f}")
        if self.comboParchi.currentText()=="Parco Nazionale del Gran Paradiso" and self.selected==True:
            self.granParadiso()
        elif self.comboParchi.currentText()=="Parco Nazionale del Cilento, Vallo di Diano e Alburni" and self.selected==True:
            self.parcoCilento()
        elif self.comboParchi.currentText()=="Parco Nazionale delle Cinque Terre" and self.selected==True:
            self.parcoCinqueTerre()
        else:
            self.alert()

    def granParadiso(self):
        self.pushFlora.clicked.disconnect(self.alert)
        self.pushFauna.clicked.disconnect(self.alert)
        self.pushActivity.clicked.disconnect(self.alert)
        self.pushRegole.clicked.disconnect(self.alert)
        self.pushFlora.clicked.connect(lambda: self.label.setText(floraGranParadiso))
        self.pushFauna.clicked.connect(lambda: self.label.setText(faunaGranParadiso))
        self.pushActivity.clicked.connect(lambda: self.label.setText(activityGranParadiso))
        self.pushRegole.clicked.connect(lambda: self.label.setText(regoleGranParadiso))
    def parcoCilento(self):
        self.pushFlora.clicked.disconnect(self.alert)
        self.pushFauna.clicked.disconnect(self.alert)
        self.pushActivity.clicked.disconnect(self.alert)
        self.pushRegole.clicked.disconnect(self.alert)
        self.pushFlora.clicked.connect(lambda: self.label.setText(floraCilento))
        self.pushFauna.clicked.connect(lambda: self.label.setText(faunaCilento))
        self.pushActivity.clicked.connect(lambda: self.label.setText(activityCilento))
        self.pushRegole.clicked.connect(lambda: self.label.setText(regoleCilento))
    def parcoCinqueTerre(self):
        self.pushFlora.clicked.disconnect(self.alert)
        self.pushFauna.clicked.disconnect(self.alert)
        self.pushActivity.clicked.disconnect(self.alert)
        self.pushRegole.clicked.disconnect(self.alert)
        self.pushFlora.clicked.connect(lambda: self.label.setText(floraCinqueTerre))
        self.pushFauna.clicked.connect(lambda: self.label.setText(faunaCinqueTerre))
        self.pushActivity.clicked.connect(lambda: self.label.setText(activityCinqueTerre))
        self.pushRegole.clicked.connect(lambda: self.label.setText(regoleCinqueTerre))

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