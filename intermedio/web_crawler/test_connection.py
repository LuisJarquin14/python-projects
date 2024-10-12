# Prueba de conección a la base de datos

import psycopg2

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

if __name__ == "__main__":
    conn = connect_db()
    if conn:
        print("Conexión a la base de datos exitosa.")
        conn.close()
    else:
        print("No se pudo conectar a la base de datos.")
