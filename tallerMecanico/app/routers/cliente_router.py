from fastapi import APIRouter
from app.services.cliente_service import obtener_clientes, crear_cliente
from app.schemas.cliente_schema import ClienteCreate

router = APIRouter()

@router.get("/clientes")
def get_clientes_route():
    return obtener_clientes()

@router.post("/clientes")
def create_cliente_route(cliente: ClienteCreate):
    return crear_cliente(cliente)