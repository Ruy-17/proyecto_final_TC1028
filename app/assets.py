import time


def mostrar_titulo():
    print("\033[1;34m")  # azul negrita
    print("==============================")
    print("       Base 1  VS  Base 2")
    print("==============================")
    print("\033[0m")  # reset color


def loading_screen(base1, base2):
    print("\033[1;34m")  # azul negrita
    print("==============================")
    print(f"       Base {base1}  VS  Base {base2}")
    print("==============================")
    print("\033[0m")  # reset color


def separador(tamano=40):
    print("-" * tamano)


def cuenta_regresiva(segundos):
    for i in range(segundos, 0, -1):
        print(f"\rTiempo restante: {i} seg", end="")
        time.sleep(1)
    print("\n¡Se acabó el tiempo!\n")
