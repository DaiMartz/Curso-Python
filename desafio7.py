def saludo(nombre, numero):
    try:
        numero = int(numero)  # Intentamos convertir el número a entero
        if numero == 0:
            print("Hola", nombre)
        else:
            print("Chau", nombre)
    except ValueError:
        print("Error: el segundo valor debe ser un número entero.")

# Programa principal
nombre_usuario = input("Ingrese el nombre de la persona: ")
valor = input("Ingrese un valor entero: ")

saludo(nombre_usuario, valor)