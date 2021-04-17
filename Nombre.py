import re
nombre = ""

while not re.match("^[A-Za-záéíóúÁÉÍÓÚüÜ]+$", nombre):
    nombre =input("Nombre: ")

print("Muchas gracias!!")