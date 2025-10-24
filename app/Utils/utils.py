import random
import readchar
import os
from app.Utils.Constants import DIFICULTADES as opciones_dificultad
from datetime import datetime


RECORDS_FILE = os.path.join(os.path.dirname(__file__), "logs.txt")


# Generador de números aleatorios en diferentes bases
def generador_de_numeros(base, digitos_inicial, digitos_final):
    extension = 10**digitos_final
    numero_decimal = random.randint(10 ** (digitos_inicial - 1), extension - 1)

    if base == 2:
        return str(bin(numero_decimal)[2:])
    elif base == 8:
        return str(oct(numero_decimal)[2:])
    elif base == 16:
        return str(hex(numero_decimal)[2:].upper())
    else:
        return str(numero_decimal)


# Conversor de números entre bases
def convertir_numero(numero, base_inicial, base_final):
    numero_decimal = int(numero, base_inicial)

    if base_final == 2:
        return str(bin(numero_decimal)[2:])
    elif base_final == 8:
        return str(oct(numero_decimal)[2:])
    elif base_final == 16:
        return str(hex(numero_decimal)[2:].upper())
    else:
        return str(numero_decimal)


# Selección de dificultad con la funcion de moverse con las flechas y el ENTER
def seleccionar_dificultad_ConFlechas():
    opciones = [v["nombre"] for v in opciones_dificultad.values()] + ["Salir"]
    indice = 0

    while True:
        print("\033c", end="")  # Limpiar pantalla

        for i, opcion in enumerate(opciones):
            if i == indice:
                print(f"> {opcion}")
            else:
                print(f"  {opcion}")

        tecla = readchar.readkey()

        if tecla == readchar.key.UP:
            indice = (indice - 1) % len(opciones)
        elif tecla == readchar.key.DOWN:
            indice = (indice + 1) % len(opciones)
        elif tecla == readchar.key.ENTER:
            print(f"Seleccionaste: {opciones[indice]}")
            if opciones[indice] == "Salir":
                return 0  # Retornamos 0 para salir
            input("Presiona Enter para continuar...")
            return indice + 1


# Gestión de records, para que el usuario pueda ver los mejores puntajes
def cargar_records():
    # Carga los records desde el archivo TXT.
    if not os.path.exists(RECORDS_FILE):
        return []
    records = []
    with open(RECORDS_FILE, "r") as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                try:
                    nombre, puntaje, fecha = linea.split("|")
                    records.append({
                        "nombre": nombre,
                        "puntaje": int(puntaje),
                        "fecha": fecha
                    })
                except ValueError:
                    continue  # ignorar líneas mal formateadas
    # Ordenar por puntaje descendente y quedarse con top 5
    return sorted(records, key=lambda x: x["puntaje"], reverse=True)[:5]


# Guarda los records en el archivo TXT.
def guardar_records(records):
    with open(RECORDS_FILE, "w") as f:
        for r in records:
            linea = f"{r['nombre']}|{r['puntaje']}|{r['fecha']}\n"
            f.write(linea)


# Agrega un nuevo record y mantiene solo los 5 mejores.
def agregar_record(nombre, puntaje):
    records = cargar_records()
    records.append({
        "nombre": nombre,
        "puntaje": puntaje,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    # Ordenar y mantener solo top 5
    records = sorted(records, key=lambda x: x["puntaje"], reverse=True)[:5]
    guardar_records(records)


# Muestra los 5 mejores puntajes.
def mostrar_top5():
    records = cargar_records()
    print("\n🏆  TOP 5 JUGADORES  🏆")
    print("=======================")
    if not records:
        print("Aún no hay puntajes registrados.")
        return
    for i, r in enumerate(records, start=1):
        print(f"{i}. {r['nombre']:<10} {r['puntaje']} pts  ({r['fecha']})")
    print("=======================\n")
