# Conexion a la base de datos

import psycopg2
from psycopg2 import sql

def connect_db():
    """Establece una conexión a la base de datos PostgreSQL"""
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="web_crawler_db",
            user="postgres",  # Usuario de PostgreSQL
            password="tu_password",  # Contraseña del usuario de PostgreSQL
            port="5432"  # Puerto de PostgreSQL
        )
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def insert_data(url, title, content):
    """Inserta los datos extraídos en la base de datos"""
    conn = connect_db()
    if conn is None:
        print("No se pudo establecer conexión a la base de datos.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute(
            sql.SQL(
                "INSERT INTO scraped_data (url, title, content) VALUES (%s, %s, %s)"
            ),
            (url, title, content),
        )
        conn.commit()
        print("Datos insertados exitosamente.")
    except Exception as e:
        print(f"Error al insertar los datos: {e}")
    finally:
        cursor.close()
        conn.close()
