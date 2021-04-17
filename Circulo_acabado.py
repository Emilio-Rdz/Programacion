import math
class Circulo():
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
        
    def area(self):
        area = (math.pi*(r**2))
     
        return area
        
    def Prisma(self):
        area = (math.pi*(r1**2))
        volumen = b * h
        
        return volumen
        
    def Piramide(self):
        area = (math.pi*(r2**2))
        volumen2 = ba * h1 / 3
       
        return volumen2
    
r = float(input("Introduzca el valor del Radio"))
r1 = float(input("Introduzca el radio del cilindro"))
h = float(input("introduzca la altura del cilindro"))
h1 = float(input("Introduzca la altura del cono"))
r2 = float(input("introduzaca el radio del cono"))
b= float(input("Introduzca la base del prisma"))
ba= float(input("Introduzca la base de la piramide"))

ar = Circulo(5,7)
area = a.area()
volumen = a.volumen()
volumen = a.volumen2()

print("El area del circulo es: ", area,"\n")    
print("El volumen del prisma es: ", volumen,"\n")   
print("el volumen de la piramide es: ", volumen2,"\n") 
