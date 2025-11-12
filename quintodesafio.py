# Ingresamos los datos
limite_inferior = int(input("Ingrese el límite inferior del intervalo: "))
limite_superior = int(input("Ingrese el límite superior del intervalo: "))
valor = int(input("Ingrese un valor entero: "))

# Verificamos si el valor está dentro del intervalo
if limite_inferior <= valor <= limite_superior:
    print(f"✅ El número {valor} está dentro del intervalo [{limite_inferior}, {limite_superior}].")
else:
    print(f"❌ El número {valor} NO está dentro del intervalo [{limite_inferior}, {limite_superior}].")