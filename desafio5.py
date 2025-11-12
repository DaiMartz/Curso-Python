# Programa que realiza una división entre dos números

try:
    # Ingreso de datos por teclado
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Operación de división
    resultado = num1 / num2

    # Mostrar el resultado
    print("El resultado de la división es:", resultado)

except ZeroDivisionError:
    # Captura el error si el divisor es cero
    print("Error: No se puede dividir por cero.")
