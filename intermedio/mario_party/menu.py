import tkinter as tk
from tkinter import messagebox
from game import start_single_player, start_multiplayer

def show_rules():
    rules = """
    Reglas del juego:
    1. Cada jugador selecciona un personaje.
    2. Los jugadores se turnan para lanzar el dado y moverse por el tablero.
    3. Los minijuegos se juegan después de ciertos turnos.
    4. El objetivo es recoger tantas estrellas como sea posible.
    5. El jugador que llegue al final es el ganador.
    """
    messagebox.showinfo("Reglas del juego", rules)

def main_menu(root=None):
    if root is None:
        root = tk.Tk()  # Solo crear una nueva ventana si no se pasa una existente
    root.title("Mario Party Clone")
    root.geometry("600x400")
    root.config(bg="#f7f7f7")  # Cambia el color de fondo

    # Limpiar el contenido de la ventana antes de agregar nuevos widgets
    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(root, text="Mario Party Clone", font=("Arial", 30, "bold"), bg="#f7f7f7", fg="#ff5722")
    title.pack(pady=20)

    # Botones con un estilo más atractivo
    play_button = tk.Button(root, text="Modo Solitario", command=lambda: start_single_player(root), font=("Arial", 14), bg="#4caf50", fg="white", padx=20, pady=10)
    play_button.pack(pady=10)

    multiplayer_button = tk.Button(root, text="Modo Multijugador", command=lambda: start_multiplayer(root), font=("Arial", 14), bg="#2196f3", fg="white", padx=20, pady=10)
    multiplayer_button.pack(pady=10)

    rules_button = tk.Button(root, text="Reglas", command=show_rules, font=("Arial", 14), bg="#ffc107", fg="black", padx=20, pady=10)
    rules_button.pack(pady=10)

    exit_button = tk.Button(root, text="Salir", command=root.quit, font=("Arial", 14), bg="#f44336", fg="white", padx=20, pady=10)
    exit_button.pack(pady=10)

    # Añadir un marco para un efecto visual
    frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.RAISED)
    frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    # Opcional: agregar una imagen de fondo (si tienes una)
    # bg_image = tk.PhotoImage(file="path/to/image.png")
    # bg_label = tk.Label(frame, image=bg_image)
    # bg_label.place(relwidth=1, relheight=1)

    root.mainloop()

if __name__ == "__main__":
    main_menu()  # Inicia el menú principal
