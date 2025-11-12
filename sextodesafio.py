suma = 0  # acumulador

# Pedimos 5 números usando un bucle for
for i in range(1, 6):
    numero = float(input(f"Ingrese el número {i}: "))
    suma += numero  # sumamos cada número

# Calculamos el promedio
promedio = suma / 5

# Mostramos el resultado
print(f"📊 El promedio de los números ingresados es: {promedio}")
