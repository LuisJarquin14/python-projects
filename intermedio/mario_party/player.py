class Player:
    def __init__(self, name, character):
        self.name = name
        self.character = character
        self.stars = 0
        self.position = 0
        self.color = self.assign_color(character)

    def move(self, steps):
        self.position += steps

    def assign_color(self, character):
        colors = {
            "Mario": "red",
            "Luigi": "darkgreen",
            "Peach": "pink",
            "Yoshi": "limegreen",
            "Toad": "yellow",
            "Bowser": "orange"
        }
        return colors.get(character, "blue")  # Color por defecto es negro si no se encuentra el personaje
