import sys
import PyQt5.QtWidgets as PyQT
from PyQt5 import uic

class principal(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGuit()

    def initGuit(self):
        uic.loadUi('calculadora.ui',self)
        self.show()

        self.pushButton.clicked.connect(self.calcular)
        self.actionSalir.triggered.connect(exit) 

    def calcular(self):
        texto1=float(self.num1.text())
       

        if self.dec2bin.isChecked()==True:
            resul=[]
            if num1 % 2==0:
                resul.append()
            
            self.resultado.setText(str(texto1))
        elif self.dec2hex.isChecked()==True:
            self.resultado.setText(str(texto1))
        elif self.bin2dec.isChecked()==True:
            self.resultado.setText(str(texto1))
        else:
            self.resultado.setText(str(texto1))


        #self.resultado.setText(str(float(texto1)+float(texto2)))


def main():
    app = PyQT.QApplication([])
    window = principal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
