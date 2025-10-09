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


# class app:
def main():
    global bases
    print("Bienvenido al juego de conversiones entre bases numericas!")
    dificultad = seleccionar_dificultad()

    if dificultad == 1:
        dificultad_str = "Fácil"
    elif dificultad == 2:
        dificultad_str = "Normal"
    elif dificultad == 3:
        dificultad_str = "Difícil"
    elif dificultad == 4:
        dificultad_str = "Imposible"

    print(f"!!!!La Dificultad seleccionada fue: {dificultad_str}!!!")

    numero, base_inicial = numero_a_convertir(dificultad)

    while True:
        base_final = random.choice(bases)
        if base_final != base_inicial:
            break

    numero_final = convertir_numero(numero, base_inicial, base_final)
    print(numero_final)

    numero_usuario = input(f"Conviertelo a base {base_final}:")

    if numero_usuario == numero_final:
        print("Bien")
    else:
        print("Mal")
