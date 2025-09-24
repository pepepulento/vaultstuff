from socket import socket
from json import loads, dumps
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from sys import exit, argv

class ServidorPrincipal(QObject):

    senal_usuario_ocupado = pyqtSignal(bool)
    def __init__(self, host: str, port: int) -> None:
        super().__init__()
        self.host = host
        self.port = port
        self.socket_server = socket(socket.AF_INET, SOCK_STREAM)
        self.usuarios_conectados = [] #aca guarda los QTHREADS de los usuarios
        self.socket_server.bind(self.host, self.port)
        self.socket_server.listen()
        
    def check_users(self, nombre_user_soli: str) -> bool:
        usuario_ocupado = False
        for user in self.usuarios_conectados:
            if user.nombre == nombre_user_soli:
                usuario_ocupado = True
        return usuario_ocupado

    def cola_de_clientes(self) -> None:

        print(f"servidor recibiendo en host:{self.host}, puerto{self.port}")
        while True:
            try:
                socket_cliente, info_cliente = self.socket_server.accept()
                nombre_user = self.socket_server.recv(16).decode("utf-8")
                estado_username = self.check_users(nombre_user)
                if not estado_username:
                    self.usuarios_conectados.append(nombre_user)
                    print(self.usuarios_conectados)
                elif estado_username:
                    respuesta = estado_username.to_bytes(1, byteorder="big")
                    self.socket_cliente.send(respuesta)
                    self.socket_cliente.close()

                
            except ConnectionError:
                print("hubo un problema al conectar un cliente")
                


if __name__ == "__main__":
    server = ServidorPrincipal(localhost, 4444)
    server.cola_de_clientes()

#class Cliente(QThread):
#    def __init__(self, socket_cliente) -> None:
#        super().__init__()
#        self.port = port
#        self.host = host
#        self.socket_cliente = socket(socket.AF_INET, socket.SOCK_STREAM)
#        try:
#            self.socket.connect((self.host, self.port))

        
#        except ConnectionError:
#            print("ERROR DE CONEXION")
#            self.socket.close()
#            exit()

