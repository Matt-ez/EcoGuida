from src.main import Window,QApplication
from sys import argv
app = QApplication(argv)
win=Window()
win.show()
app.exec()