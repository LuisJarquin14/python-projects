# Web Crawler con Interfaz Gráfica y PostgreSQL

Este proyecto es un web crawler (rastreador web) con una interfaz gráfica construida usando `tkinter` que permite al usuario especificar URLs para extraer información y almacenarla en una base de datos PostgreSQL.

## Requisitos

- Python 3.6 o superior
- PostgreSQL 12 o superior

### Librerías de Python

Para instalar las dependencias necesarias, ejecuta:

```bash
pip install -r requirements.txt
```

## Lista de Dependencias

- tkinter: Para la interfaz gráfica.
- requests: Para realizar solicitudes HTTP.
- beautifulsoup4: Para analizar y extraer datos del HTML.
- psycopg2: Para conectarse y realizar operaciones en PostgreSQL.

## Configuración de la Base de Datos

1. Asegúrate de tener PostgreSQL instalado y ejecutándose en tu máquina.
2. Crea una base de datos llamada web_crawler_db.
3. Dentro de web_crawler_db, crea una tabla scraped_data con la siguiente estructura:

```sql
CREATE TABLE scraped_data (
    id SERIAL PRIMARY KEY,
    url TEXT NOT NULL,
    title TEXT,
    content TEXT
);
```

4. Actualiza los detalles de conexión a la base de datos en database.py con tus propias credenciales de PostgreSQL.

```python
import psycopg2
from psycopg2 import sql

def connect_db():
    """Establece una conexión a la base de datos PostgreSQL"""
    conn = psycopg2.connect(
        host="localhost",
        database="web_crawler_db",
        user="postgres",  # Usuario de PostgreSQL
        password="tu_contraseña",  # Contraseña del usuario de PostgreSQL
        port="5432"  # Puerto de PostgreSQL
    )
    return conn
```

### Estructura del proyecto

```plaintext
web_crawler/
├── main.py         # Archivo principal para ejecutar el crawler
├── gui.py          # Archivo para la interfaz gráfica
├── crawler.py      # Archivo para la lógica de scraping
├── database.py     # Archivo para la conexión y manejo de la base de datos
└── requirements.txt # Dependencias del proyecto
```

## Ejecución del Crawler

Para ejecutar el proyecto, simplemente ejecuta el archivo main.py:

```bash
python main.py
```
