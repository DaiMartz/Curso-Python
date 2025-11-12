persona = {
    "nombre": [],
    "apellido": [],
    "edad": []
}

# Cargar datos de 4 personas
for i in range(4):
    nombre = input("Ingrese el nombre: ")
    persona["nombre"].append(nombre)

    apellido = input("Ingrese el apellido: ")
    persona["apellido"].append(apellido)

    edad = input("Ingrese su edad: ")
    persona["edad"].append(edad)

# Guardar datos del diccionario en un archivo
with open("persona.txt", "w") as contenido:
    for i in range(4):
        contenido.write(persona["nombre"][i] + ",")
        contenido.write(persona["apellido"][i] + ",")
        contenido.write(persona["edad"][i] + "\n")

# Mostrar los datos
print("\n*** Datos cargados en el archivo ***")
for i in range(4):
    print(persona["nombre"][i] + ", " + persona["apellido"][i] + ", " + persona["edad"][i])