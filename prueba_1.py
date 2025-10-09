# Base 1 vs Base 2
import random

bases = [10, 2, 8, 16]


def generador_de_numeros(base, digitos_inicial, digitos_final):
    extension = 10**digitos_final
    numero_decimal = random.randint(10 ** (digitos_inicial - 1), extension - 1)
    if base == 2:
        return str(bin(numero_decimal)[2:])
    elif base == 8:
        return str(oct(numero_decimal)[2:])
    elif base == 16:
        return str(hex(numero_decimal)[2:])
    else:
        return str(numero_decimal)


def seleccionar_dificultad():
    while True:
        try:
            print("¡Seleccione la dificultad!")
            dificultad = int(
                input("Facil (1) - Normal (2) - Dificil (3) - Imposible (4): ")
            )
            if dificultad in [1, 2, 3, 4]:
                return dificultad
            else:
                print("Opcion invalida. Intente de nuevo.")
        except ValueError:
            print("Error, ingrese un numero entero del 1 al 4.")


def numero_a_convertir(dificultad):
    global bases
    base = random.choice(bases)
    if dificultad == 1:
        digitos_inicial = 1
        digitos_final = 1
    elif dificultad == 2:
        digitos_inicial = 1
        digitos_final = 2
    elif dificultad == 3:
        digitos_inicial = 2
        digitos_final = 3
    elif dificultad == 4:
        digitos_inicial = 3
        digitos_final = 4

    numero = generador_de_numeros(base, digitos_inicial, digitos_final)

    if base == 2:
        base_str = "Binaria (2)"
    elif base == 8:
        base_str = "Octal (8)"
    elif base == 10:
        base_str = "Decimal (10)"
    elif base == 16:
        base_str = "Hexadecimal (16)"
    print(f"Tu número está en base: {base_str} y es: {numero}")
    return numero, base


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


class app:
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

        while base_final != base_inicial:
            base_final = random.choice(bases)

        numero_final = convertir_numero(numero, base_inicial, base_final)
        print(numero_final)

        numero_usuario = input(f"Conviertelo a base {base_final}:")

        if numero_usuario == numero_final:
            print("Bien")
        else:
            print("Mal")

