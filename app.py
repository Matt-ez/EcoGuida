from src.main import QApplication, Landing
from sys import argv
app = QApplication(argv)
landing = Landing()
landing.show()
app.exec()