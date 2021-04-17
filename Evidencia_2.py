from math import pi

class Circulo:
    def __init__(self, radio=0.0, altura=0.0):
        self.radio = radio
        self.altura = altura

    def area(self):
        resultado = pi*self.radio**2

        return resultado

a = Circulo()
radio = float(input("Cual es la medida del radio de la base: "))
altura = float (input("Cual es la medida de la altura del prisma: "))
print = ("El area del circulo es:", a.area())



 