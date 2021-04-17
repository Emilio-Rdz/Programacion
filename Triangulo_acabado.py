import math
class Triangulo():
    def __init__(self):
        self.radio = radio
        self.altura = altura
        
    def area(self):
        area = base * altura / 2
     
        return area
        
    def Prisma(self):
        area=(math.pi*(r**2))
        volumen = area * h
        
        return volumen
        
    def Piramide(self):
        area=(math.pi*(r**2))
        volumen2 = area * h / 3
       
        return volumen2
    
b= float(input("Introduzca la base del prisma"))
ba= float(input("Introduzca la base de la piramide"))
r=float(input("Introduzca el valor del Radio:\n"))
r1=float(input("Introduzca el radio del cilindro\n"))
h=float(input("introduzca la altura del cilindro\n"))
h1=float(input("Introduzca la altura del cono"))
r2=float(input("introduzaca el radio del cono"))

area = Triangulo(5,7)

print("El area del triangulo es: ",a.area,"\n")    
print("El volumen del prisma es: ",a.volumen,"\n")   
print("el volumen de la piramide es: ",a.volumen2,"\n")  
