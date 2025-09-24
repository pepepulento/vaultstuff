from entities import Item, Usuario
from utils.pretty_print import print_usuario, print_canasta, print_items

def cargar_items() -> list:
    lista_de_instancias = []
    with open("utils/items.dcc", "r") as archivo:
        items = archivo.read()
        lista_items = items.split("\n")
    for cada_item in lista_items:
        cada_item_lista = cada_item.split(",")
        instancia_item = Item(cada_item_lista[0], int(cada_item_lista[1]), int(cada_item_lista[2]))
        lista_de_instancias.append(instancia_item)
    return lista_de_instancias
def crear_usuario(tiene_suscripcion: bool) -> Usuario:
    instancia_usuario = Usuario(tiene_suscripcion)
    print_usuario(instancia_usuario)
    return instancia_usuario

if __name__ == "__main__":
    usuario_creado = crear_usuario(True)
    los_items = cargar_items()
    print_items(los_items)
    for item in los_items:
        usuario_creado.agregar_item(item)
    print_canasta(usuario_creado)
    usuario_creado.comprar()
    print_usuario(usuario_creado)
