class Comida(): 
    
    def  __init__ ( yo , nombre , precio ) : 
        yo . nombre = nombre
        yo . precio = precio
    
    def obtenerPrecio ( self ) : 
        return self . precio
    
    def  __str__ ( self ) : 
        return self.nombre+':'+str(self.obtenerPrecio() )
  
# Definiendo una función para construir un Menú 
# que genera una lista de Food     
def Construirmenu (nombres,costos): 
    menu =  [ ] 
    for i in  range ( len ( nombre ) ) : 
        menu . añadir ( Alimentos ( nombres [ i ] , costos [ i ] ) ) 
    regresar menú

# items 
nombres =  [ 'Café' ,  'Té' ,  'Pizza' ,  'Hamburguesa' ,  'Papas fritas' ,  'Manzana' ,  'Donas' ,  'Pastel' ]

# precios 
costos =  [ 25 ,  30 ,  100 ,  80 ,  65 ,  15 ,  15 ,  60 ]

# menú de construcción de alimentos 
Alimentos = menú de construcción ( nombres , costos )

n =  1 
for el en Alimentos : 
    print ( n , '.' , el ) 
    n = n +  1