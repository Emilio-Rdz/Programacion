class Vehiculo:
    
    def __init__(self, placa, marca, modelo, kilometraje):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = kilometraje
        
        # Metodos Accesores
        def getUnidad(self):
            while True:
                Unidad = input("Favor ingresar Unidad: ")
                if bool(re.match("^[A-Z]{2}\d{3}", unidad))
                    break
                
                print("La Unidad es: ")
            
        def getMarca(self):
            While True:
                marca = input("Favor ingresar marca: ")
                if bool(re.match("^[A-Z]{20}", marca))
                    break
                
                print("La marca es: ")
        
        def getModelo(self):
            while True:
                modelo = input("Favor ingresar modelo: ")
                if bool(re.match("^\d{4}$", modelo)):
                    break
                
                print("El modelo del auto es: ")
                
        def getkilometraje(self):
            kilometraje = int(input("Cuanto kilometraje ha recorrido?: "))
            
            return self.kilometraje
        
            print("El kilometraje recorrdido es de: ")
            
        def mostrarVehiculo(self):
           print ("\nUnidad: " +self.getUnidad()+ "\nMarca: "+self.getMarca()+"\nModelo: "+self.getModelo()+
                   "\nKilometraje: "+(self.getKilometraje()) )

Unidad = input("Favor ingresar Unidad: ")
marca = input("Favor ingresar marca: ")
modelo = input("Favor ingresar modelo: ")
kilometraje = input("Favor ingresar kilometraje: ")
e = Vehiculo(placa,marca,modelo,kilometraje)
