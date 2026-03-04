import pymysql

def connect_to_database():
    connection = pymysql.connect(
        host='localhost',
        user='admin',
        password='RoyML',
        database='taller_db',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection