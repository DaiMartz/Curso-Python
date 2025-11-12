# Abrir el archivo personas.csv
with open("personas.csv", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        # Quitar salto de línea y dividir por comas
        datos = linea.strip().split(",")
        print(datos)