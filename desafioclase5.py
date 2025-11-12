mi_lista= ["Phyton", "C", "C++", "Javascript","Ruby, Cobol", "Pascal", "Klotin","HTML","CSS"]
try: 
    indice= int(input("Ingrese un numero y te devuelvo un lenguaje de programación"))
    print("el lenguaje elegido es:", mi_lista[indice])
except IndexError:
    print ("el indice no existe")
except ValueError:
    print ("No se pueden ingresar letras o signos!") 