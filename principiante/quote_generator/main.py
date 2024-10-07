import tkinter as tk
import random

def load_quotes(filename):
    quotes = {'amor': [], 'vida': []}
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        category, quote = line.strip().split('|')
        if category in quotes:
            quotes[category].append(quote)
    return quotes

def get_random_quote(quotes, category):
    return random.choice(quotes[category]) if quotes[category] else "No hay citas disponibles."

def show_quote():
    selected_category = category_var.get()
    quote = get_random_quote(quotes, selected_category)
    quote_display.config(state='normal')
    quote_display.delete('1.0', tk.END)
    quote_display.insert(tk.END, quote)
    quote_display.config(state='disabled')
    
# Cargar citas
quotes = load_quotes('quotes.txt')

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Citas")

# Variable para la categoria
category_var = tk.StringVar(value='amor')

# Etiqueta y opciones de categorias
category_label = tk.Label(root, text="Seleccione una categoria:")
category_label.pack()

category_options = ['amor', 'vida']
category_menu = tk.OptionMenu(root, category_var, *category_options)
category_menu.pack()

#Boton para generar la cita
generate_button = tk.Button(root, text="Generar Cita", command=show_quote)
generate_button.pack()

# Campo para mostrar la cita
quote_display = tk.Text(root, height=5, width=50, state='disabled', wrap='word')
quote_display.pack()

# Iniciar el bucle principal de la aplicacion
root.mainloop()