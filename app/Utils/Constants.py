BASES = [10, 2, 8, 16]  # Bases numéricas soportadas por el juego
DIFICULTADES = {  # Niveles de dificultad con sus respectivos tiempos y puntos para una mejor estructura
    1: {"nombre": "Fácil", "tiempo": 60, "puntos": 10},
    2: {"nombre": "Normal", "tiempo": 45, "puntos": 20},
    3: {"nombre": "Difícil", "tiempo": 35, "puntos": 40},
    4: {"nombre": "Imposible", "tiempo": 30, "puntos": 80},
}

# Ruta de archivo para almacenar los récords del juego
RECORD_FILE = "app/Utils/logs.txt"
