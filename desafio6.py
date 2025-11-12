# Creamos un diccionario vacío
personas = {}

# Ingresamos datos de 3 personas
for i in range(3):
    print(f"\nPersona {i+1}:")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    dni = input("Ingrese el DNI: ")

    # Guardamos los datos en el diccionario
    personas[dni] = {
        "nombre": nombre,
        "apellido": apellido
    }

# Mostramos el contenido del diccionario
print("\n--- Lista de personas registradas ---")
for dni, datos in personas.items():
    print(f"DNI: {dni} - Nombre: {datos['nombre']} {datos['apellido']}")

# Contar cuántos DNI superan los 40 millones
contador = 0
for dni in personas.keys():
    if int(dni) > 40000000:
        contador += 1

print(f"\nCantidad de personas con DNI mayor a 40 millones: {contador}")