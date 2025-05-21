from src.main import Window,QApplication, Landing
from sys import argv
app = QApplication(argv)
win=Window()
landing = Landing()
landing.show()
app.exec()