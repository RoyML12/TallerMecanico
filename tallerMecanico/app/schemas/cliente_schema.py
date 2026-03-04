from pydantic import BaseModel, EmailStr

class ClienteCreate(BaseModel):
    nombre: str
    telefono: str
    email: EmailStr