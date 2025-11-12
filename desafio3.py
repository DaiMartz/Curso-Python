# Pedimos al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Verificamos si es par
if numero % 2 == 0:
    print(f"El número {numero} es PAR.")
else:
    print(f"El número {numero} es IMPAR.")

input("Presiona Enter para salir...") 