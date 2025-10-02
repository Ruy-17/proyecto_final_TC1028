#Base 1 vs Base 2
import random

def generador_de_numeros(base, digitos_inicial, digitos_final):
    extension = (10**digitos_final)
    numero_decimal = random.randint(10**(digitos_inicial-1),extension-1)
    if base == 2:
        return bin(numero_decimal)[2:]
    elif base == 8:
        return oct(numero_decimal)[2:]
    elif base == 16:
        return hex(numero_decimal)[2:]
    else:
        return numero_decimal

def seleccionar_dificultad():
    while True:
        try:
            dificultad = int(input("Facil (1) - Normal (2) - Dificil (3) - Imposible (4): "))
            if dificultad in [1, 2, 3, 4]:
                return dificultad
            else:
                print("Opcion invalida. Intente de nuevo.")
        except ValueError:
            print("Error, ingrese un numero entero del 1 al 4.")

def main():
    print(generador_de_numeros(10,1,2))

main()