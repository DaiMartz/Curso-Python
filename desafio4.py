# Pedimos al usuario que ingrese dos números enteros
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Verificamos si num1 es múltiplo de num2
if num2 != 0:  # evitamos división por cero
    if num1 % num2 == 0:
        print(f"✅ El número {num1} es múltiplo de {num2}.")
    else:
        print(f"❌ El número {num1} NO es múltiplo de {num2}.")
else:
    print("⚠️ No se puede dividir por cero. Ingrese un segundo número distinto de 0.") 