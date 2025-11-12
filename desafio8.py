notas = []

print("Ingrese las notas de los exámenes (-1 para terminar):")

nota = int(input("Ingrese una nota: "))
while nota != -1:
    if 6 <= nota <= 10:     # solo guardo notas válidas
        notas.append(nota)
    nota = int(input("Ingrese una nota: "))

while ((nota < -1 or nota > 10)):
        nota = int(input("Error: Ingrese una nota entre -1 y 10: "))

if len(notas) == 0:
    print("\nNo se ingreso ninguna nota válida")    
else:
    print("\nLas notas válidas ingresadas fueron:")
    for n in notas:
        print(n)

   