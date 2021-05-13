import csv

import os

ruta_archivo=os.path.abspath(os.getcwd())
archivo_respaldo=ruta_archivo+"\\participantes.bak"
archivo_normal=ruta_archivo+"\\participantes.csv"

print(archivo_respaldo)
print(archivo_normal)

if os.path.exists(archivo_normal):
    # verifica si hay respaldo, y lo elimina
    if os.path.exists(archivo_respaldo):
        os.remove(archivo_respaldo)
    # Pasa el archivo normal, para que sea archivo de respaldo
    os.rename(archivo_normal,archivo_respaldo)

f = open(archivo_normal,"w+")
# Escribir el encabezado.
f.write("NOMBRE|CORREO|NACIMIENTO|MOMENTO")
# Cierro el archivo.
f.close()
