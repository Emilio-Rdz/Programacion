import csv

class  Participante:
      def __init__(self,CORREO,NOMBRE,NACIMIENTO, MOMENTO):
            self.CORREO = CORREO
            self.NOMBRE = NOMBRE
            self.NACIMIENTO = NACIMIENTO
            self.MOMENTO = MOMENTO

with open('participantes.csv') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    contador_lineas = 0
     lista_participante = []
     for linea_datos in lector_csv:
        if contador_lineas == 0:
            # Si es la primer línea, muestro los nombres de campo y no guardo nada
            # en la lista.
            print(f'Los participantes son {", ".join(linea_datos)}')
        else:
            objeto_temporal = participante({linea_datos[0]},{linea_datos[1]},{linea_datos[2]},{linea_datos[3]})
            lista_participante.append(objeto_temporal)
            
     print(f'Procesadas {len(lista_participante)} líneas.')
     
