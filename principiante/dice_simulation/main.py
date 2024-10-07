import tkinter as tk
from PIL import Image, ImageTk
import random

class DiceSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de Dados")

        # Cargar imágenes de los dados
        self.dice_images = [
            ImageTk.PhotoImage(Image.open(f"images/dice{i}.png"))
            for i in range(1, 7)
        ]

        # Crear etiqueta para mostrar la imagen del dado
        self.dice_label = tk.Label(root)
        self.dice_label.pack()

        # Botón para lanzar el dado
        self.roll_button = tk.Button(root, text="Lanzar Dado", command=self.roll_dice)
        self.roll_button.pack()

        # Mensaje de bienvenida
        self.message_label = tk.Label(root, text="Haz clic en el botón para lanzar el dado")
        self.message_label.pack()

        # Evento de clic en el dado
        self.dice_label.bind("<Button-1>", self.roll_dice)

        # Lanzar el dado por primera vez para mostrar una imagen inicial
        self.roll_dice()

    def roll_dice(self, event=None):
        # Generar un número aleatorio entre 1 y 6
        dice_number = random.randint(1, 6)
        # Mostrar la imagen correspondiente
        self.dice_label.config(image=self.dice_images[dice_number - 1])
        # Actualizar el mensaje
        self.message_label.config(text=f"¡Sacaste un {dice_number}!")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceSimulation(root)
    root.mainloop()
