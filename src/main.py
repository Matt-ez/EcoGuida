from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap,QIcon
from PyQt6.uic import *
import time
from src.text import * # importa i testi dei parchi


class Window(QWidget): # Classe della finestra principale
    def __init__(self):
        super().__init__()
        loadUi("GUI/main.ui",self)
        self.setWindowTitle("EcoGuida 2025")
        self.setWindowIcon(QIcon("images/Logo_EcoGuida.png"))
        self.show()
        self.pushcnt=0
        self.selected = False
        self.pushSelect.clicked.connect(self.parcoChanger)
        self.comboParchi.currentTextChanged.connect(self.deSelect) # Ogni volta che si cambia il parco selezionato, si deseleziona quello precedente
        self.deSelect()
    
    def deSelect(self):
        """ Metodo per deselezionare il parco selezionato e collegare i bottoni alla funzione di alert """
        self.pushcnt=0
        self.selected = False
        self.label.setText("")
        self.deselecter()
        self.pushFlora.clicked.connect(self.alert)
        self.pushFauna.clicked.connect(self.alert)
        self.pushActivity.clicked.connect(self.alert)
        self.pushRegole.clicked.connect(self.alert)
        self.comboParchi.setStyleSheet("QComboBox { background-color: #ffffff}")

    def deselecter(self):
        """ Metodo per disconnettere i bottoni dalle funzioni precedenti """
        for btn in [self.pushFlora,self.pushFauna,self.pushActivity,self.pushRegole]:
            try: 
                btn.clicked.disconnect()
            except TypeError:
                pass

    def alert(self):
        """ Metodo per mostrare un alert se non è stato selezionato un parco """
        msg = QMessageBox()
        self.label.setText("")
        msg.setWindowTitle("Attenzione!")
        msg.setText("Il parco non è stato selezionato!")
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec()

    def parcoChanger(self):
        """ Metodo per cambiare il parco selezionato, collega i bottoni al parco corrispettivo """
        self.pushcnt+=1
        if self.pushcnt>1:
            alrt=QMessageBox()
            alrt.setText("Basta premere ricchione")
            alrt.setWindowTitle(">:(")
            alrt.exec()
            return
        self.selected = True
        self.comboParchi.setStyleSheet("QComboBox { background-color: #bbf78f}")
        """ Chiama le funzioni specifche di ogni parco """
        if self.comboParchi.currentText()=="Parco Nazionale del Gran Paradiso" and self.selected==True:
            self.granParadiso()
        elif self.comboParchi.currentText()=="Parco Nazionale del Cilento, Vallo di Diano e Alburni" and self.selected==True:
            self.parcoCilento()
        elif self.comboParchi.currentText()=="Parco Nazionale delle Cinque Terre" and self.selected==True:
            self.parcoCinqueTerre()

    def granParadiso(self):
        """ Metodo per collegare i bottoni ai setText del parco Gran Paradiso """
        self.deselecter()
        self.pushFlora.clicked.connect(lambda: self.label.setText(floraGranParadiso))
        self.pushFauna.clicked.connect(lambda: self.label.setText(faunaGranParadiso))
        self.pushActivity.clicked.connect(lambda: self.label.setText(activityGranParadiso))
        self.pushRegole.clicked.connect(lambda: self.label.setText(regoleGranParadiso))
    def parcoCilento(self):
        """ Metodo per collegare i bottoni ai setText del parco Nazionale del Cilento, vallo di Diano e Alburni """
        self.deselecter()
        self.pushFlora.clicked.connect(lambda: self.label.setText(floraCilento))
        self.pushFauna.clicked.connect(lambda: self.label.setText(faunaCilento))
        self.pushActivity.clicked.connect(lambda: self.label.setText(activityCilento))
        self.pushRegole.clicked.connect(lambda: self.label.setText(regoleCilento))
    def parcoCinqueTerre(self):
        """ Metodo per collegare i bottoni ai setText del parco Nazionale delle Cinque Terre """
        self.deselecter()
        self.pushFlora.clicked.connect(lambda: self.label.setText(floraCinqueTerre))
        self.pushFauna.clicked.connect(lambda: self.label.setText(faunaCinqueTerre))
        self.pushActivity.clicked.connect(lambda: self.label.setText(activityCinqueTerre))
        self.pushRegole.clicked.connect(lambda: self.label.setText(regoleCinqueTerre))
        

class Landing(QWidget): # Classe della Landing Page
    def __init__(self):
        super().__init__()
        loadUi("GUI/landing.ui", self)
        self.setWindowTitle("EcoGuida - Benvenuto!")
        self.setWindowIcon(QIcon("images/Logo_EcoGuida.png"))
        self.pushEntra.clicked.connect(self.openApp) # Collega il pulsante "Entra" alla funzione openApp
        self.progressBar.hide()  # All'inizio la progress bar è nascosta

    def openApp(self):
        """ Metodo per mostrare la progress bar, creare la classe Window, aprire la finestra e chiudere la landing page """
        self.progressBar.show()
        """ Finto caricamento della progress bar """
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