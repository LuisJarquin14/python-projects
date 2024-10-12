# Lógica de Scraping

import requests
from bs4 import BeautifulSoup
from database import insert_data

def scrape_and_store_data(url):
    try:
        # Realizar la solicitud HTTP GET a la URL
        response = requests.get(url)  # Corregido: 'reponse' a 'response'
        
        # Verificar si la respuesta fue exitosa
        if response.status_code != 200:
            raise Exception(f"Error al acceder a la URL: {response.status_code}")
        
        # Parsear el contenido HTML en un objeto BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extraer el título del sitio web
        title = soup.title.string if soup.title else 'Sin título'
        
        # Extraer el contenido (Puedes personalizar esta parte según tus necesidades)
        content = soup.get_text()
        
        # Almacenar los datos en la base de datos
        insert_data(url, title, content)

    except Exception as e:
        print(f"Error al extraer y almacenar los datos: {e}")

