from json import dumps, encode
from socket import socket
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QMutex


class BackendCliente(QObject):
    archivos_disponibles = pyqtSignal(list)
    usuario_status = pyqtSignal(bool)
    pyqtSignal
    def __init__(self, host: str, port: int):
        super().__init__()
        self.host = host
        self.puerto = port
        self.socket_cliente = socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Intentando conectar al servidor en {self.host} puerto {self.port}")
        try:
            self.socket_cliente.connect((self.host, self.port))
            respuesta_usuario_b = self.socket_cliente.recv(1)
            respuesta_usuario = bool(int.from_bytes(respuesta_usuario_b, byteorder="big"))
            usuario_status.emit(respuesta_usuario)

        except ConnectionError:
            print("hubo un error en la conexion")

            

#class Cliente(QThread):
#    def __init__()


