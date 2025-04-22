import sys
from PyQt6.QtWidgets import QApplication, QWidget


class Ventana_vacia(QWidget):


    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100,100,250,250)
        self.setWindowTitle('VENTANA')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana_vacia()
    sys.exit(app.exec())
