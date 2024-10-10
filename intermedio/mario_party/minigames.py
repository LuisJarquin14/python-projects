class MiniGame:
    def __init__(self):
        self.games = [
            {
                "question": "¿Cuánto es 2 + 2?",
                "options": ["3", "4", "5", "6"],
                "answer": "4"
            },
            {
                "question": "¿Cuál es la capital de Francia?",
                "options": ["Berlín", "Madrid", "París", "Londres"],
                "answer": "París"
            },
            {
                "question": "Adivina el número: Soy un número entre 1 y 10 y soy mayor que 5.",
                "options": ["1", "3", "7", "10"],
                "answer": "7"
            },
            {
                "question": "¿Qué animal es conocido como el mejor amigo del hombre?",
                "options": ["Gato", "Perro", "Caballo", "Pájaro"],
                "answer": "Perro"
            },
            {
                "question": "Completa la adivinanza: En el agua nací, en el agua me crié, pero si tocas mi piel, en el aire me iré. ¿Qué soy?",
                "options": ["Pescado", "Hielo", "Nieve", "Agua"],
                "answer": "Hielo"
            },
            {
                "question": "¿Cuánto es 5 x 6?",
                "options": ["30", "25", "35", "40"],
                "answer": "30"
            },
            {
                "question": "¿Cuál es el océano más grande del mundo?",
                "options": ["Atlántico", "Índico", "Pacífico", "Ártico"],
                "answer": "Pacífico"
            },
            {
                "question": "¿Qué instrumento tiene cuerdas y se toca con un arco?",
                "options": ["Piano", "Guitarra", "Violín", "Batería"],
                "answer": "Violín"
            },
            {
                "question": "¿Quién pintó la Mona Lisa?",
                "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
                "answer": "Leonardo da Vinci"
            },
            {
                "question": "¿Cuántos planetas hay en el sistema solar?",
                "options": ["7", "8", "9", "10"],
                "answer": "8"
            },
            {
                "question": "¿Qué gas respiramos principalmente?",
                "options": ["Oxígeno", "Dióxido de carbono", "Nitrógeno", "Hidrógeno"],
                "answer": "Oxígeno"
            },
            {
                "question": "¿Cuál es el continente más grande?",
                "options": ["África", "Asia", "Europa", "América del Sur"],
                "answer": "Asia"
            },
            {
                "question": "¿Qué es el ADN?",
                "options": ["Ácido desoxirribonucleico", "Ácido ribonucleico", "Proteína", "Carbohidrato"],
                "answer": "Ácido desoxirribonucleico"
            },
            {
                "question": "¿Quién escribió 'Cien años de soledad'?",
                "options": ["Gabriel García Márquez", "Jorge Luis Borges", "Julio Cortázar", "Mario Vargas Llosa"],
                "answer": "Gabriel García Márquez"
            },
            {
                "question": "¿Qué parte del cuerpo se utiliza para oír?",
                "options": ["Ojo", "Nariz", "Oído", "Boca"],
                "answer": "Oído"
            },
            {
                "question": "¿Qué animal es el rey de la selva?",
                "options": ["Elefante", "Tigre", "León", "Gorila"],
                "answer": "León"
            },
            {
                "question": "¿Cuál es el país más poblado del mundo?",
                "options": ["India", "Estados Unidos", "China", "Brasil"],
                "answer": "China"
            },
            # Puedes agregar más preguntas aquí...
        ]

    def get_question(self, index):
        return self.games[index % len(self.games)]
