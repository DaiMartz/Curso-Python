personas = []

with open("recursosPython (1).csv", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

encabezados = lineas[0].strip().split(",")

for linea in lineas[1:]:
    valores = linea.strip().split(",")
    persona = {}
    for i in range(len(encabezados)):
        persona[encabezados[i]] = valores[i]
    personas.append(persona)

print("Personas con apellido Gomez:")
for p in personas:
    if p["Apellido"].lower() == "gomez":
        print(p)

with open("personas_filtradas.csv", "w", encoding="utf-8") as nuevo_archivo:
    nuevo_archivo.write(",".join(encabezados) + "\n")
    
    for p in personas:
        if p["Lugar de residencia"].lower() in ["santa fe", "cordoba"]:
            fila = [p[c] for c in encabezados]
            nuevo_archivo.write(",".join(fila) + "\n")

print("\nArchivo 'personas_filtradas.csv' creado con éxito.")

filtrados = []

for p in personas:
    if p["Lugar de residencia"].lower() in ["santa fe", "cordoba"]:
        filtrados.append(p)

with open("personas_filtradas.csv", "w", encoding="utf-8") as nuevo:
    nuevo.write(",".join(encabezados) + "\n")
    for p in filtrados:
        fila = [p[c] for c in encabezados]
        nuevo.write(",".join(fila) + "\n")
