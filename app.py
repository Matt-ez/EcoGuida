from src.main import QApplication, Landing # Importa le classi necesarie dal main
from sys import argv
app = QApplication(argv) # Crea la QApplication
landing = Landing() # Crea la Landing Page
landing.show() # Mostra la Landing Page
app.exec() # Esegue l'applicazione