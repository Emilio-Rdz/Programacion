import csv

class  Participante:
      def __init__(self,CORREO, NOMBRE, NACIMIENTO, MOMENTO):
            self.CORREO = CORREO
            self.NOMBRE = NOMBRE
            self.NACIMIENTO = NACIMIENTO
            self.MOMENTO = MOMENTO
            
Participantes = []

with open('participantes.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    for e in lector_csv:
        Participantes.append(Participante(e[0],e[1],e[2],e[3]))
        
for o in Participantes:
    print(o.CORREO)
    print(o.NOMBRE)
    print(o.NACIMIENTO)
    print(o.MOMENTO) 