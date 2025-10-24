import time
import sys


# Utilidades visuales para el juego de conversiones entre bases numéricas


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


# def time_con_thread(segundos, stop_event):
#     for i in range(segundos, 0, -1):
#         if stop_event.is_set():
#             return
#         print(f"\r⏳ Tiempo restante: {i} seg \t Respuesta:\t", end="")
#         time.sleep(1)
#     print("\n🕒 ¡Se acabó el tiempo!\n")
#     stop_event.set()


# Funcion para ver el timer en vivo en la terminal, para que el usuario siempre sepa cuanto tiempo le queda
def time_con_thread(segundos, stop_event):
    for i in range(segundos, 0, -1):
        if stop_event.is_set():
            return

        sys.stdout.write("\0337")
        sys.stdout.flush()

        sys.stdout.write("\033[1A")
        sys.stdout.write("\r")
        sys.stdout.write(f"⏳ Tiempo restante: {i:02d} seg   ")
        sys.stdout.flush()

        sys.stdout.write("\0338")
        sys.stdout.flush()

        time.sleep(1)

    print("\n🕒 ¡Se acabó el tiempo!\n")
    stop_event.set()


# Función para limpiar la pantalla de la terminal
def clear_screen():
    print("\033[H\033[J", end="")
