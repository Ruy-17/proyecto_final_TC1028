import random
from app.data import BASES as bases
from app.utils import (
    generador_de_numeros,
    convertir_numero,
    seleccionar_dificultad,
)


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

    print(f"Tu número está en base: {base_str} y es: {numero}")
    return numero, base


def main():
    print("Bienvenido al juego de conversiones entre bases numéricas!")
    dificultad = seleccionar_dificultad()

    dificultad_str = ["Fácil", "Normal", "Difícil", "Imposible"][dificultad - 1]
    print(f"!!! La dificultad seleccionada fue: {dificultad_str} !!!")

    numero, base_inicial = numero_a_convertir(dificultad)
    base_final = random.choice([b for b in bases if b != base_inicial])

    numero_final = convertir_numero(numero, base_inicial, base_final)
    numero_usuario = input(f"Convierte el número a base {base_final}: ")

    if numero_usuario.strip().lower() == numero_final.lower():
        print("✅ ¡Correcto!")
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: {numero_final}")
