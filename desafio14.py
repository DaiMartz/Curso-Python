def dividir(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        resultado = num1 / num2
        return resultado
    except ValueError:
        print("Error: Debe ingresar solo números.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

# Programa principal
n1 = input("Ingrese el primer número: ")
n2 = input("Ingrese el segundo número: ")

resultado = dividir(n1, n2)

if resultado is not None:
    print("El resultado de la división es:", resultado)