import tkinter as tk
import random
from player import Player
from board_solitario import BoardSolitario
from board_multijugador import BoardMultijugador


def start_single_player(root):
    root.destroy()
    select_character_mode("single", 1)

def start_multiplayer(root):
    root.destroy()
    select_number_of_players()

def select_number_of_players():
    def set_num_players(num):
        select_num_players_window.destroy()
        select_character_mode("multi", num)

    select_num_players_window = tk.Tk()
    select_num_players_window.title("Seleccionar número de jugadores")
    select_num_players_window.configure(bg="#f0f0f0")

    tk.Label(select_num_players_window, text="Selecciona el número de jugadores:", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)
    for i in range(2, 7):  # De 2 a 6 jugadores
        tk.Button(select_num_players_window, text=str(i), command=lambda i=i: set_num_players(i), font=("Arial", 14), bg="#4CAF50", fg="white").pack(pady=5)

    select_num_players_window.mainloop()

def select_character_mode(mode, max_players, current_player=1, players=None):
    if players is None:
        players = []

    def add_player():
        name = name_entry.get()
        character = char_var.get()
        players.append(Player(name, character))
        select_char_window.destroy()
        if len(players) < max_players:
            select_character_mode(mode, max_players, current_player + 1, players)
        else:
            if mode == "single":
                select_level(players)
            else:
                start_game(players)

    select_char_window = tk.Tk()
    select_char_window.title(f"Seleccionar personaje - Jugador {current_player}")
    select_char_window.configure(bg="#f0f0f0")

    tk.Label(select_char_window, text=f"Nombre del jugador {current_player}:", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)
    name_entry = tk.Entry(select_char_window, font=("Arial", 14))
    name_entry.pack(pady=5)

    tk.Label(select_char_window, text="Selecciona un personaje:", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)
    char_var = tk.StringVar(value="Mario")
    characters = ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Bowser"]
    for character in characters:
        tk.Radiobutton(select_char_window, text=character, variable=char_var, value=character, font=("Arial", 14), bg="#f0f0f0").pack(anchor=tk.W)

    tk.Button(select_char_window, text="Seleccionar", command=add_player, font=("Arial", 14), bg="#4CAF50", fg="white").pack(pady=10)

    select_char_window.mainloop()

def select_level(players):
    def set_level(level):
        level_var.set(level)
        level_window.destroy()
        start_game(players, level_var.get())

    level_window = tk.Tk()
    level_window.title("Seleccionar nivel de juego")
    level_window.configure(bg="#f0f0f0")

    level_var = tk.StringVar(value="fácil")
    tk.Label(level_window, text="Selecciona el nivel de juego:", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)

    tk.Radiobutton(level_window, text="Fácil", variable=level_var, value="fácil", font=("Arial", 14), bg="#f0f0f0").pack(anchor=tk.W)
    tk.Radiobutton(level_window, text="Intermedio", variable=level_var, value="intermedio", font=("Arial", 14), bg="#f0f0f0").pack(anchor=tk.W)
    tk.Radiobutton(level_window, text="Difícil", variable=level_var, value="difícil", font=("Arial", 14), bg="#f0f0f0").pack(anchor=tk.W)

    tk.Button(level_window, text="Seleccionar", command=lambda: set_level(level_var.get()), font=("Arial", 14), bg="#4CAF50", fg="white").pack(pady=10)

    level_window.mainloop()

def start_game(players, level="fácil"):
    root = tk.Tk()
    root.configure(bg="#f0f0f0")

    if len(players) == 1:  # Si solo hay un jugador
        board = BoardSolitario(root, players, level)
    else:
        board = BoardMultijugador(root, players, level)

    root.mainloop()


if __name__ == "__main__":
    main_menu()
