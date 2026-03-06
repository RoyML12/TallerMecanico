from pydantic import BaseModel


class Cliente(BaseModel):
    nombre: str
    telefono: int
    email: str


class Vehiculo(BaseModel):
    placa: str
    modelo: str


class Orden(BaseModel):
    descripcion: str


class ClienteVehiculoOrden(BaseModel):
    cliente: Cliente
    vehiculo: Vehiculo
    orden: Orden