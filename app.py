"""
Programa: Suma de dos números
Autor: Mateo Ramírez
Descripción:
Este programa solicita dos números al usuario, valida que la entrada
sea correcta y muestra el resultado de la suma. Además, permite repetir
la operación las veces que el usuario desee.
"""

def solicitar_numero(mensaje):
    """
    Solicita un número al usuario y valida que la entrada sea correcta.
    """
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.\n")


def sumar(numero1, numero2):
    """
    Retorna la suma de dos números.
    """
    return numero1 + numero2


def main():
    print("=" * 40)
    print("      CALCULADORA DE SUMA")
    print("=" * 40)

    while True:
        # Solicitar datos
        num1 = solicitar_numero("Ingrese el primer número: ")
        num2 = solicitar_numero("Ingrese el segundo número: ")

        # Realizar operación
        resultado = sumar(num1, num2)

        # Mostrar resultado
        print(f"\n✅ La suma de {num1} + {num2} = {resultado}\n")

        # Preguntar si desea continuar
        repetir = input("¿Desea realizar otra suma? (S/N): ").strip().lower()

        if repetir != "s":
            print("\nGracias por utilizar el programa. ¡Hasta pronto!")
            break

        print()


# Punto de entrada del programa
if __name__ == "__main__":
    main()