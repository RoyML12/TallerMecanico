from fastapi import FastAPI
from app.routers.cliente_router import router as cliente_router

app = FastAPI()
app.include_router(cliente_router)