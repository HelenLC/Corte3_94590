import sys
import PyQt5.QtWidgets as PyQT
from PyQt5 import uic

class principal(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGuit()

    def initGuit(self):
        uic.loadUi('PrimerEjercicio.ui',self)
        self.show()

        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        texto1=float(self.num1.text())
        texto2=float(self.num2.text())

        if self.sumar.isChecked()==True:
            self.resultado.setText(str(texto1+texto2))
        elif self.restar.isChecked()==True:
            self.resultado.setText(str(texto1-texto2))
        elif self.multiplicar.isChecked()==True:
            self.resultado.setText(str(texto1*texto2))
        else:
            self.resultado.setText(str(texto1/texto2))


        #self.resultado.setText(str(float(texto1)+float(texto2)))


def main():
    app = PyQT.QApplication([])
    window = principal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
