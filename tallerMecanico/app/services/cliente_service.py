from app.repositories.cliente_repository import get_clientes, create_cliente

def obtener_clientes():
    return get_clientes()

def crear_cliente(cliente):
    return create_cliente(cliente.nombre, cliente.telefono, cliente.email)