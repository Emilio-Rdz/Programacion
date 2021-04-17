import math
class Rectangulo():
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    def area(self):
        area = self.ancho * self.alto
        
        return area
        
    def Prisma(self):
        area=(math.pi*(r**2))
        volumen = b * h
        
        return volumen
        
    def Piramide(self):
        area=(math.pi*(r**2))
        volumen2 = ba * h / 3
        
        return volumen2

b= float(input("Introduzca la base del prisma"))
ba= float(input("Introduzca la base de la piramide"))
r=float(input("Introduzca el valor del Radio:\n"))
r1=float(input("Introduzca el radio del prisma rectangular\n"))
h=float(input("introduzca la altura del prisma rectangular\n"))
h1=float(input("Introduzca la altura de la piramide rectangular"))
r2=float(input("introduzaca el radio del piramide rectangular"))

ar = Rectangulo(4,2)
area = a.area()
volumen = a.volumen()
volumen = a.volumen2()

print("El area del rectnagulo es: ",a.area,"\n")    
print("El volumen del prisma es: ",a.volumen,"\n")   
print("el volumen de la piramide es: ",a.volumen2,"\n")  

