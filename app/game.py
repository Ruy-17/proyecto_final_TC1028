import random
import threading
from timedinput import timedinput
from app.Utils.data import BASES as bases
from app.Utils.utils import (
    generador_de_numeros,
    convertir_numero,
    seleccionar_dificultad,
    seleccionar_dificultad_ConFlechas,
)
from app.assets import loading_screen, time_con_thread

_baseInicial = 0
_baseFinal = 0


def numero_a_convertir(dificultad):
    base = random.choice(bases)

    if dificultad == 1:
        digitos_inicial, digitos_final = 1, 1
    elif dificultad == 2:
        digitos_inicial, digitos_final = 1, 2
    elif dificultad == 3:
        digitos_inicial, digitos_final = 2, 3
    else:
        digitos_inicial, digitos_final = 3, 4

    numero = generador_de_numeros(base, digitos_inicial, digitos_final)

    base_str = {
        2: "Binaria (2)",
        8: "Octal (8)",
        10: "Decimal (10)",
        16: "Hexadecimal (16)",
    }[base]

    global _baseInicial
    _baseInicial = base_str.split("(")[1].split(")")[0]
    return numero, base, base_str


# class app:
def main():
    global bases
    print("Bienvenido al juego de conversiones entre bases numericas!")
    dificultad = seleccionar_dificultad_ConFlechas()

    if dificultad == 1:
        dificultad_str = "Fácil"
        tiempo = 60
    elif dificultad == 2:
        dificultad_str = "Normal"
        tiempo = 45
    elif dificultad == 3:
        dificultad_str = "Difícil"
        tiempo = 35
    elif dificultad == 4:
        dificultad_str = "Imposible"
        tiempo = 30
    else:
        print("Saliendo del juego...")
        return

    print(f"!!!!La Dificultad seleccionada fue: {dificultad_str}!!!")

    numero, base_inicial, base_str = numero_a_convertir(dificultad)

    while True:
        _baseFinal = random.choice(bases)
        if _baseFinal != base_inicial:
            break

    loading_screen(_baseInicial, _baseFinal)

    print(f"Tu número está en base: {base_str} y es: {numero}")

    numero_final = convertir_numero(numero, base_inicial, _baseFinal)
    print(f"Conviértelo a base {_baseFinal}: ", end="", flush=True)
    print(f"\nTienes {tiempo} segundos para responder\n")

    stop_event = threading.Event()

    hilo_tiempo = threading.Thread(
        target=time_con_thread, args=(tiempo, stop_event))
    hilo_tiempo.start()

    try:
        numero_usuario = input().strip()
    except KeyboardInterrupt:
        print("\nSe acabó el juego.")
        print(f"La respuesta correcta era: {numero_final}")
        stop_event.set()
        return

    stop_event.set()
    hilo_tiempo.join()

    if stop_event.is_set() and numero_usuario == "":
        print("⏰ Se te acabó el tiempo.")
    elif numero_usuario == numero_final:
        print("✅ Correcto, bien hecho!")
    else:
        print(f"❌ Incorrecto. La respuesta era: {numero_final}")
