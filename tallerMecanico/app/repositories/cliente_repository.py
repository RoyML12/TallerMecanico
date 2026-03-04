from app.database import connect_to_database

def get_clientes():
    conexion = connect_to_database()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM cliente")
            return cursor.fetchall()
    finally:
        conexion.close()

def create_cliente(nombre, telefono, email):
    conexion = connect_to_database()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO cliente (nombre, telefono, email) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nombre, telefono, email))
            conexion.commit()
            return {"message": "Cliente creado"}
    finally:
        conexion.close()