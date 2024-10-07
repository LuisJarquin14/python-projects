import tkinter as tk
import random

class NumberGuessingGame:
  def __init__(self, root):
    self.root = root
    self.root.title("Adivina el Número")

    # Difficulty Selection (Radio Buttons)
    difficulty_frame = tk.Frame(root)
    difficulty_frame.pack()
    self.difficulty_var = tk.IntVar()
    self.difficulty_var.set(1)  # Default difficulty (1-100)
    difficulty_radio1 = tk.Radiobutton(difficulty_frame, text="Fácil (1-50)", variable=self.difficulty_var, value=1)
    difficulty_radio2 = tk.Radiobutton(difficulty_frame, text="Normal (1-100)", variable=self.difficulty_var, value=2)
    difficulty_radio3 = tk.Radiobutton(difficulty_frame, text="Difícil (1-200)", variable=self.difficulty_var, value=3)
    difficulty_radio1.pack()
    difficulty_radio2.pack()
    difficulty_radio3.pack()

    self.label = tk.Label(root, text="Estoy pensando en un número...")
    self.label.pack()

    self.entry = tk.Entry(root)
    self.entry.pack()

    self.button = tk.Button(root, text="Adivinar", command=self.check_guess)
    self.button.pack()

    self.result_label = tk.Label(root, text="")
    self.result_label.pack()

    self.attempts_label = tk.Label(root, text="")
    self.attempts_label.pack()

    self.reset_game()

  def reset_game(self):
    # Set difficulty based on selection
    difficulty = self.difficulty_var.get()
    if difficulty == 1:
      self.number_to_guess = random.randint(1, 50)
    elif difficulty == 2:
      self.number_to_guess = random.randint(1, 100)
    else:
      self.number_to_guess = random.randint(1, 200)

    self.attempts = 0
    self.update_attempts_label()
    self.entry.delete(0, tk.END)
    self.result_label.config(text="¡Nuevo juego! Adivina el número:")

  def update_attempts_label(self):
    self.attempts_label.config(text=f"Intentos restantes: {10 - self.attempts}")  # Assuming 10 attempts

  def check_guess(self):
    guess = self.entry.get()

    if not guess.isdigit():
      self.result_label.config(text="Por favor, introduce un número válido.")
      return

    guess = int(guess)
    self.attempts += 1
    self.update_attempts_label()

    difference = guess - self.number_to_guess

    if difference < 0:
      hint = "Demasiado bajo."
    elif difference > 0:
      hint = "Demasiado alto."
    else:
      hint = f"¡Felicidades! Adivinaste el número en {self.attempts} intentos."
      self.root.after(5000, self.reset_game)  # Reset after 5 seconds

    self.result_label.config(text=hint)

if __name__ == "__main__":
  root = tk.Tk()
  game = NumberGuessingGame(root)
  root.mainloop()
