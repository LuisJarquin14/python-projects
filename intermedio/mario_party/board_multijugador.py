import tkinter as tk
import random
from player import Player
from minigames import MiniGame  # Importamos la clase MiniGame
import tkinter.messagebox  # Para mostrar mensajes emergentes

class BoardMultijugador:
    def __init__(self, root, players, level):
        self.players = players
        self.board_size = 20  # Ejemplo de tamaño del tablero
        self.current_player_index = 0
        self.steps_remaining = 0
        self.current_player = None
        self.mini_game = MiniGame()  # Creamos una instancia de MiniGame

        # Establecer el fondo del tablero
        self.canvas = tk.Canvas(root, width=600, height=600, bg="#e0f7fa")
        self.canvas.pack()

        # Botón para lanzar el dado con estilo
        self.roll_dice_button = tk.Button(root, text="Lanzar dado", command=self.roll_dice, font=("Arial", 14), bg="#4caf50", fg="white", padx=10, pady=5)
        self.roll_dice_button.pack(pady=10)

        # Etiqueta para mostrar información
        self.info_label = tk.Label(root, text="", font=("Arial", 14), bg="#e0f7fa")
        self.info_label.pack(pady=10)

        root.bind("<Right>", self.move_player)  # Vinculamos la tecla derecha a la función move_player

        self.draw_board()
        self.update_board()

    def draw_board(self):
        # Dibuja el tablero
        for i in range(self.board_size):
            x = (i % 5) * 120
            y = (i // 5) * 120
            self.canvas.create_rectangle(x, y, x + 120, y + 120, fill="#ffffff", outline="#9e9e9e", width=2)
            self.canvas.create_text(x + 60, y + 60, text=str(i + 1), font=("Arial", 12))

    def roll_dice(self):
        if self.steps_remaining == 0:  # Solo lanzar el dado si no hay pasos restantes
            self.steps_remaining = random.randint(1, 6)
            self.current_player = self.players[self.current_player_index]
            self.info_label.config(text=f"Turno de {self.current_player.name}. Pasos disponibles: {self.steps_remaining}")
            self.update_board()
        else:
            self.info_label.config(text=f"{self.current_player.name} aún tiene pasos restantes.")

    def move_player(self, event=None):  # Aceptar un argumento opcional para la tecla
        if self.steps_remaining > 0:
            if self.current_player.position < self.board_size - 1:  # Verificar si no ha llegado al final
                self.current_player.move(1)  # Mueve al jugador un paso
                self.steps_remaining -= 1
                self.update_board()

                # Verificar si el jugador ha llegado a la casilla final
                if self.current_player.position >= self.board_size - 1:
                    self.end_game(self.current_player)
                elif self.steps_remaining == 0:  # Si ya no hay pasos restantes
                    self.play_mini_game(self.current_player, self.current_player.position)

    def play_mini_game(self, player, position):
        question_data = self.mini_game.get_question(position)
        question = question_data["question"]
        options = question_data["options"]
        answer = question_data["answer"]

        # Deshabilitar el botón de lanzar dado
        self.roll_dice_button.config(state=tk.DISABLED)

        # Crear una nueva ventana para el minijuego
        mini_game_window = tk.Toplevel()
        mini_game_window.title("Mini Juego")
        mini_game_window.geometry("800x300")

        question_label = tk.Label(mini_game_window, text=question, font=("Arial", 14))
        question_label.pack(pady=10)

        for option in options:
            button = tk.Button(mini_game_window, text=option, command=lambda opt=option: self.check_answer(opt, answer, mini_game_window), font=("Arial", 12), bg="#2196f3", fg="white", padx=10, pady=5)
            button.pack(pady=5)

    def check_answer(self, selected_answer, correct_answer, mini_game_window):
        if selected_answer == correct_answer:
            tk.messagebox.showinfo("Respuesta Correcta", "¡Has respondido correctamente! Puedes lanzar el dado nuevamente.")
            mini_game_window.destroy()  # Cerrar la ventana del mini juego
            self.steps_remaining = 0  # Permitir al jugador lanzar el dado nuevamente
            self.roll_dice_button.config(state=tk.NORMAL)  # Habilitar el botón de lanzar dado
            self.info_label.config(text=f"Es el turno de {self.players[self.current_player_index].name}.")
        else:
            tk.messagebox.showinfo("Respuesta Incorrecta", "Respuesta incorrecta. Es el turno del siguiente jugador.")
            mini_game_window.destroy()  # Cerrar la ventana del mini juego
            self.next_turn()

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.steps_remaining = 0  # Reiniciar los pasos
        self.info_label.config(text=f"Es el turno de {self.players[self.current_player_index].name}.")
        self.roll_dice_button.config(state=tk.NORMAL)  # Habilitar el botón de lanzar dado

    def end_game(self, player):
        # Deshabilitar el botón de lanzar dado
        self.roll_dice_button.config(state=tk.DISABLED)
    
        # Mostrar el nombre del ganador y un mensaje de felicitación en una ventana emergente
        winner_message = f"{player.name} ha ganado!\n¡Felicidades!"
        winner_window = tk.Toplevel()
        winner_window.title("Fin del Juego")
        
        winner_label = tk.Label(winner_window, text=winner_message, font=("Arial", 24))
        winner_label.pack(pady=20)
    
        return_menu_button = tk.Button(winner_window, text="Regresar al menú", command=lambda: self.return_to_menu(), font=("Arial", 14), bg="#4caf50", fg="white", padx=10, pady=5)
        return_menu_button.pack(pady=10)

    def return_to_menu(self):
        # Llamar a la función del menú principal
        from menu import main_menu
        self.canvas.winfo_toplevel().destroy()  # Cerrar la ventana del tablero
        main_menu()  # Llamar a la función main_menu del archivo menu.py

    def update_board(self):
        self.canvas.delete("player")
        for player in self.players:
            x = (player.position % 5) * 120 + 60
            y = (player.position // 5) * 120 + 60
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=player.color, tags="player")

