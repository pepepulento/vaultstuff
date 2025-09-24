from PyQt5.QtGui import QFont, QMouseEvent, QKeyEvent
from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QWidget, QLabel, QPushButton,
QApplication, QLineEdit)
from os.path import abspath
from sys import __excepthook__, exit
from parametros_frontend import (
        MAX_CARACT_USER, MIN_CARACT_USER, MSG_ERROR_LARGO,MSG_ERROR_CARACT)

class VentanaDeInicio(QWidget):
    
    senal_conectar_usuario = pyqtSignal(str)
    senal_ingresar_usuario = pyqtSignal(str)
    

    def __init__(self) -> None:

        super().__init__()

        self.iniciar_main()
        
    def iniciar_main(self) -> None:

        self.setGeometry(200, 200, 640, 640)
        self.setWindowTitle("DCComparte Archivos")

        self.label_caja_usuario = QLabel("Ingresa tu nombre de usuario", self)
        self.label_advertencia = QLabel("", self)
        self.caja_usuario = QLineEdit("", self)
        self.boton_ingreso = QPushButton("Ingresar", self)

        layout = QVBoxLayout()
        layout.addWidget(self.label_caja_usuario)
        layout.addWidget(self.caja_usuario)
        layout.addWidget(self.label_advertencia)
        layout.addWidget(self.boton_ingreso)
        self.setLayout(layout)
        self.show()
        self.boton_ingreso.clicked.connect(self.checkeo_user)
    def checkeo_user(self) -> None:
        usuario = self.caja_usuario.text()
        if len(usuario) > MAX_CARACT_USER or len(usuario) < MIN_CARACT_USER:
            self.label_advertencia.setText(MSG_ERROR_LARGO)
        else:
            hay_mayus = False
            hay_minus = False
            hay_num = False

            for c in usuario:
                if c.islower():
                    hay_minus = True
               elif c.isupper():
                    hay_mayus = True
                elif c.isdigit():
                    hay_num = True

            if hay_mayus and hay_minus and hay_num:
                    self.label_advertencia.setText("")
                    self.senal_ingresar_usuario.emit(usuario)
            else:
                self.label_advertencia.setText(MSG_ERROR_CARACT)

class VentanaDescargas(QWidget):

    def __init__(self) -> None:
        super().__init__()
    
    def iniciar_ventana(self) -> None:
        self.setGeometry(200, 100, 640, 640)
        self.setWindowTitle("Mis Descargas")
        
        layout_archivos = QVBoxLayout()

    def layout_por_archivo(self, nombre_archivo) -> QHBoxLayout:
        layout_general = QHBoxLayout()


if __name__ == "__main__":
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    __excepthook__ = hook

    app = QApplication([])
    ventana = VentanaDeInicio()
    exit(app.exec())
