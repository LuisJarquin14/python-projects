# Interfaz grafica

import tkinter as tk
from tkinter import messagebox
from crawler import scrape_and_store_data

def start_scraping():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Advertencia", "Por favor, introduce una URL.")
        return
    
    try:
        scrape_and_store_data(url)
        messagebox.showinfo("Éxito", "Datos extraídos y almacenados exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al extraer y almacenar los datos: {e}")

def exit_application():
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Web Crawler")
root.geometry("500x300")
root.configure(bg='#282c34')

# Crear un marco para el título
title_frame = tk.Frame(root, bg='#61afef')
title_frame.pack(fill=tk.X)

# Etiqueta de título
title_label = tk.Label(title_frame, text="Web Crawler", font=('Helvetica', 18, 'bold'), bg='#61afef', fg='white')
title_label.pack(pady=10)

# Crear un marco para el contenido principal
main_frame = tk.Frame(root, bg='#282c34')
main_frame.pack(pady=20)

# Etiqueta y campo de entrada para la URL
url_label = tk.Label(main_frame, text="Introduce la URL:", font=('Helvetica', 12), bg='#282c34', fg='white')
url_label.pack(pady=10)

url_entry = tk.Entry(main_frame, width=50)
url_entry.pack(pady=5)

# Botón para iniciar el scraping
scrape_button = tk.Button(main_frame, text="Iniciar scraping", command=start_scraping, bg='#98c379', fg='white', font=('Helvetica', 12))
scrape_button.pack(pady=20)

# Botón para salir de la aplicación
exit_button = tk.Button(main_frame, text="Salir", command=exit_application, bg='#e06c75', fg='white', font=('Helvetica', 12))
exit_button.pack(pady=10)

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
