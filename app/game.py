import os
import random
import threading
from readchar import config
from timedinput import timedinput
from app.Utils.Constants import BASES as bases, RECORD_FILE, DIFICULTADES as opciones_dificultad
from app.Utils.utils import (
    generador_de_numeros,
    convertir_numero,
    seleccionar_dificultad,
    seleccionar_dificultad_ConFlechas,
    mostrar_top5,
    agregar_record
)
from app.Utils.assets import loading_screen, time_con_thread, mostrar_titulo, separador, clear_screen
_baseInicial = 0
_baseFinal = 0


def numero_a_convertir(dificultad):
    base = random.choice(bases)

    rangos = {
        1: (1, 1),
        2: (1, 2),
        3: (2, 3),
        4: (3, 4)
    }
    digitos_inicial, digitos_final = rangos[dificultad]

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
    puntaje_total = 0
    clear_screen()
    mostrar_titulo()
    print("Bienvenido al juego de conversiones entre bases numericas!")
    mostrar_top5()
    nombre = input("Ingresa tu nombre: ").strip() or "Anónimo"

    dificultad = seleccionar_dificultad_ConFlechas()
    while True:

        if dificultad == 0:
            clear_screen()
            print("Saliendo del juego...")
            break

        clear_screen()

        # Config de la dificultad
        config = opciones_dificultad[dificultad]
        dificultad_str = config["nombre"]
        tiempo = config["tiempo"]
        puntos = config["puntos"]

        print(f"\n!!!!La Dificultad seleccionada fue: {dificultad_str}!!!")

        # Generar número a convertir
        numero, base_inicial, base_str = numero_a_convertir(dificultad)
        while True:
            _baseFinal = random.choice(bases)
            if _baseFinal != base_inicial:
                break

        loading_screen(_baseInicial, _baseFinal)
        print(f"Tu número está en base: {base_str} y es: {numero}")

        numero_final = convertir_numero(numero, base_inicial, _baseFinal)
        print(f"\nConviértelo a base {_baseFinal}: ", end="", flush=True)
        print(f"\nTienes {tiempo} segundos para responder\n")

        stop_event = threading.Event()
        hilo_tiempo = threading.Thread(
            target=time_con_thread, args=(tiempo, stop_event))
        print("\n")
        hilo_tiempo.start()

        try:
            numero_usuario = input("Respuesta: ").strip()
        except KeyboardInterrupt:
            print("\nSe acabó el juego.")
            print(f"La respuesta correcta era: {numero_final}")
            stop_event.set()
            break

        stop_event.set()
        hilo_tiempo.join()

        if stop_event.is_set() and numero_usuario == "":
            print("⏰ Se te acabó el tiempo.")
        elif numero_usuario == numero_final:
            print("✅ Correcto, bien hecho!")
            puntaje_total += puntos
            print(f"\n🏅 Puntaje actual: {puntaje_total} pts\n")
            input("Presiona Enter para continuar...")
            clear_screen()
        else:
            print(f"❌ Incorrecto. La respuesta era: {numero_final}")
            print(f"\n🎉 Juego terminado. Puntaje total: {puntaje_total} pts")
            agregar_record(nombre, puntaje_total)
            mostrar_top5()
            continuar = input("¿Quieres de nuevo (y/n): ").strip().lower()
            if continuar != "y":
                clear_screen()
                break
