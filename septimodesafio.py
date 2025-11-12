notas = []

print("Ingrese las notas de los exámenes (-1 para terminar):")

nota = int(input("Ingrese una nota: "))
while (nota < -1 or nota > 10):
    nota = int(input("Error: Ingrese una nota entre 0 y 10: "))
while nota != -1:
    notas.append(nota)
    nota = int(input("Ingrese una nota: "))
    while ((nota < -1 or nota > 10)):
        nota = int(input("Error: Ingrese una nota entre 0 y 10: "))

print("\nLas notas ingresadas fueron:")
for n in notas:
    print(n)
    