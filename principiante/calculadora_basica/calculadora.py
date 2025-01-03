import tkinter as tk
from tkinter import messagebox


class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.resultado = tk.StringVar()

        # Crear la entrada para mostrar el resultado
        self.entrada = tk.Entry(master, textvariable=self.resultado, font=(
            "Arial", 16), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entrada.grid(row=0, column=0, columnspan=4)

        # Crear botones
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('CE', 5, 0)  # Cambiado a CE
        ]

        for (texto, fila, columna) in botones:
            self.crear_boton(texto, fila, columna)

    def crear_boton(self, texto, fila, columna):
        if texto == 'C':
            boton = tk.Button(self.master, text=texto, padx=20, pady=20, font=("Arial", 16),
                              command=self.eliminar_todo)
        elif texto == 'CE':
            boton = tk.Button(self.master, text=texto, padx=20, pady=20, font=("Arial", 16),
                              command=self.eliminar_ultimo)
        else:
            boton = tk.Button(self.master, text=texto, padx=20, pady=20, font=("Arial", 16),
                              command=lambda: self.click_boton(texto))
        boton.grid(row=fila, column=columna)

    def eliminar_todo(self):
        self.resultado.set("")

    def eliminar_ultimo(self):
        entrada_actual = self.resultado.get()
        self.resultado.set(entrada_actual[:-1])

    def click_boton(self, texto):
        if texto == 'C':
            self.resultado.set("")
        elif texto == '=':
            try:
                resultado = eval(self.resultado.get())
                self.resultado.set(resultado)
            except Exception as e:
                messagebox.showerror("Error", "Entrada no válida")
                self.resultado.set("")
        else:
            self.resultado.set(self.resultado.get() + texto)


if __name__ == "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()
