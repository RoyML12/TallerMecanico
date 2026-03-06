from fastapi import APIRouter
from app.database import connect_to_database
from app.schemas.cliente_schema import ClienteVehiculoOrden

router = APIRouter()

@router.get("/ordenes")
def obtener_ordenes():

    conexion = connect_to_database()

    try:
        with conexion.cursor() as cursor:

            sql = """
           SELECT 
                c.id_cliente,
                c.nombre,
                c.telefono,
                c.email,
                v.id_vehiculos,
                v.placa,
                v.modelo,
                o.id_orden,
                o.descripcion,
                o.estado,
                o.fecha_ingreso
            FROM cliente c
            LEFT JOIN vehiculos v 
            ON c.id_cliente = v.id_cliente
            LEFT JOIN ordenes_servicio o
            ON v.id_vehiculos = o.id_vehiculo;
            """

            cursor.execute(sql)

            resultados = cursor.fetchall()

            return resultados

    finally:
        conexion.close()

@router.post("/clientes")
def crear_cliente(data: ClienteVehiculoOrden):

    conexion = connect_to_database()

    try:
        with conexion.cursor() as cursor:

            sql_cliente = """
            INSERT INTO cliente (nombre, telefono, email)
            VALUES (%s,%s,%s)
            """

            cursor.execute(sql_cliente, (
                data.cliente.nombre,
                data.cliente.telefono,
                data.cliente.email
            ))

            id_cliente = cursor.lastrowid


            sql_vehiculo = """
            INSERT INTO vehiculos (placa, modelo, id_cliente)
            VALUES (%s,%s,%s)
            """

            cursor.execute(sql_vehiculo, (
                data.vehiculo.placa,
                data.vehiculo.modelo,
                id_cliente
            ))

            id_vehiculo = cursor.lastrowid


            sql_orden = """
            INSERT INTO ordenes_servicio
            (id_cliente, id_vehiculo, descripcion)
            VALUES (%s,%s,%s)
            """

            cursor.execute(sql_orden, (
                id_cliente,
                id_vehiculo,
                data.orden.descripcion
            ))

            id_orden = cursor.lastrowid

            conexion.commit()

            return {
                "mensaje": "Cliente, vehículo y orden creados",
                "cliente_id": id_cliente,
                "vehiculo_id": id_vehiculo,
                "orden_id": id_orden
            }

    finally:
        conexion.close()