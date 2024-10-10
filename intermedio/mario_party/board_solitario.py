import tkinter as tk
import random
from player import Player
from minigames import MiniGame
import tkinter.messagebox

class BoardSolitario:
    def __init__(self, root, players, level):
        self.players = players
        self.board_size = 20
        self.current_player_index = 0
        self.steps_remaining = 0
        self.current_player = None
        self.mini_game = MiniGame()
        self.lives = self.set_lives(level)

        self.canvas = tk.Canvas(root, width=600, height=600, bg="#f0f0f0")
        self.canvas.pack(pady=20)
        self.draw_board()

        self.roll_dice_button = tk.Button(root, text="Lanzar dado", command=self.roll_dice, font=("Arial", 14), bg="#4CAF50", fg="white")
        self.roll_dice_button.pack(pady=10)

        self.info_label = tk.Label(root, text="", font=("Arial", 16), bg="#f0f0f0")
        self.info_label.pack(pady=10)

        self.lives_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
        self.lives_label.pack(pady=10)

        root.bind("<Right>", self.move_player)

        self.update_board()

    def set_lives(self, level):
        if level == "fácil":
            return 5
        elif level == "intermedio":
            return 2
        elif level == "difícil":
            return 1

    def draw_board(self):
        for i in range(self.board_size):
            x = (i % 5) * 120
            y = (i // 5) * 120
            self.canvas.create_rectangle(x, y, x + 120, y + 120, fill="white", outline="#888888", width=2)
            self.canvas.create_text(x + 60, y + 60, text=str(i + 1), font=("Arial", 12), fill="#333333")

    def roll_dice(self):
        if self.steps_remaining == 0:
            self.steps_remaining = random.randint(1, 6)
            self.current_player = self.players[self.current_player_index]
            self.info_label.config(text=f"Turno de {self.current_player.name}. Pasos disponibles: {self.steps_remaining}")
            self.lives_label.config(text=f"Oportunidades restantes: {self.lives}")  # Actualizar la etiqueta de vidas
            self.update_board()
        else:
            self.info_label.config(text=f"{self.current_player.name} aún tiene pasos restantes.")

    def move_player(self, event=None):
        if self.steps_remaining > 0:
            if self.current_player.position < self.board_size - 1:
                self.current_player.move(1)
                self.steps_remaining -= 1
                self.update_board()

                if self.current_player.position >= self.board_size - 1:
                    self.end_game(self.current_player)
                elif self.steps_remaining == 0:
                    self.play_mini_game(self.current_player, self.current_player.position)

    def play_mini_game(self, player, position):
        question_data = self.mini_game.get_question(position)
        question = question_data["question"]
        options = question_data["options"]
        answer = question_data["answer"]

        self.roll_dice_button.config(state=tk.DISABLED)

        mini_game_window = tk.Toplevel()
        mini_game_window.title("Mini Juego")
        mini_game_window.geometry("800x300")
        mini_game_window.configure(bg="#f0f0f0")

        question_label = tk.Label(mini_game_window, text=question, font=("Arial", 14), bg="#f0f0f0")
        question_label.pack(pady=10)

        for option in options:
            button = tk.Button(mini_game_window, text=option, command=lambda opt=option: self.check_answer(opt, answer, mini_game_window), font=("Arial", 12), bg="#2196F3", fg="white")
            button.pack(pady=5)

    def check_answer(self, selected_answer, correct_answer, mini_game_window):
        if selected_answer == correct_answer:
            tk.messagebox.showinfo("Respuesta Correcta", "¡Has respondido correctamente! Puedes lanzar el dado nuevamente.")
            mini_game_window.destroy()
            self.steps_remaining = 0
            self.roll_dice_button.config(state=tk.NORMAL)
            self.info_label.config(text=f"Es el turno de {self.players[self.current_player_index].name}.")
        else:
            self.lives -= 1
            mini_game_window.destroy()
            if self.lives <= 0:
                self.game_over()
            else:
                tk.messagebox.showinfo("Respuesta Incorrecta", f"Respuesta incorrecta. Te quedan {self.lives} oportunidades.")
                self.next_turn()

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.steps_remaining = 0
        self.info_label.config(text=f"Es el turno de {self.players[self.current_player_index].name}.")
        self.lives_label.config(text=f"Oportunidades restantes: {self.lives}")  # Actualizar la etiqueta de vidas
        self.roll_dice_button.config(state=tk.NORMAL)

    def end_game(self, player):
        self.roll_dice_button.config(state=tk.DISABLED)
        winner_message = f"{player.name} ha ganado!\n¡Felicidades!"
        winner_window = tk.Toplevel()
        winner_window.title("Fin del Juego")

        winner_label = tk.Label(winner_window, text=winner_message, font=("Arial", 24))
        winner_label.pack(pady=20)

        return_menu_button = tk.Button(winner_window, text="Regresar al menú", command=lambda: self.return_to_menu(), font=("Arial", 14), bg="#FF5722", fg="white")
        return_menu_button.pack(pady=10)

    def game_over(self):
        self.roll_dice_button.config(state=tk.DISABLED)
        game_over_window = tk.Toplevel()
        game_over_window.title("Fin del Juego")

        game_over_label = tk.Label(game_over_window, text="¡Has perdido! No te quedan oportunidades.", font=("Arial", 24))
        game_over_label.pack(pady=20)

        return_menu_button = tk.Button(game_over_window, text="Regresar al menú", command=lambda: self.return_to_menu(), font=("Arial", 14), bg="#FF5722", fg="white")
        return_menu_button.pack(pady=10)

    def return_to_menu(self):
        from menu import main_menu
        self.canvas.winfo_toplevel().destroy()
        main_menu()

    def update_board(self):
        self.canvas.delete("player")
        for player in self.players:
            x = (player.position % 5) * 120 + 60
            y = (player.position // 5) * 120 + 60
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=player.color, tags="player")
