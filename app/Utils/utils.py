import random
import readchar
from app.data import DIFICULTADES as opciones_dificultad
# from app.data import BASES as bases


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


def seleccionar_dificultad():
    while True:
        try:
            print("¡Seleccione la dificultad!")
            dificultad = int(
                input("Fácil (1) - Normal (2) - Difícil (3) - Imposible (4): ")
            )
            if dificultad in [1, 2, 3, 4]:
                return dificultad
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Error, ingrese un número entero del 1 al 4.")


def seleccionar_dificultad_ConFlechas():
    opciones = opciones_dificultad + ["Salir"]
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
                break
            input("Presiona Enter para continuar...")
            break
    print("\033c", end="")  # Limpiar pantalla al salir

    return indice + 1
