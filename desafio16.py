try:
    with open("personas.csv", "r", encoding="latin-1") as archivo:
        for linea in archivo:
            linea = linea.strip()       # elimina saltos de línea
            datos = linea.split(",")    # separa por coma
            print(datos)
except FileNotFoundError:
    print("Error: no se encontró el archivo 'personas.csv'.")
except UnicodeDecodeError:
    print("Error de codificación al leer el archivo.")