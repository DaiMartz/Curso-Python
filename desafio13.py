persona = {
    "nombre": [],
    "apellido": [],
    "edad": []
}
for i in range (4):
    nombre= input("Ingrese el nombre:")
    persona ["nombre"]. append(nombre)
    apellido= input("Ingrese el apellido:")
    edad=input("Ingrese su edad:")
# abrir un archivo
contenido=open("persona.txt","w")

#Guardar datos del diccionario en el archivo
for i in range (4):
    contenido.write(persona["nombre"][i]+",")
    contenido.write(persona["apellido"][i]+",")
    contenido.write(persona["edad"][i]+"/n")
contenido.close()

#Mostrar los datos
print("*** Datos cargados en el archivo***")
for i in range(4):
    print(persona["nombre"][i]","+persona["apellido"][i]+","+persona["edad"][i])
    