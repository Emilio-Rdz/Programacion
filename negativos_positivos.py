import random

A = [None] * 5
for i in range(0,5):
    A[i] = [None] * 5
    
sumaPositivos = 0
productoNegativo = 1

for i in range(0,5):
    for j in range(0,5):
        A[i][j] = random.randit(1, 100) - 50
    
for i in range(0,5):
    for j in range(0,5):
        if (A[i][j] < 0):
             productoNegativo = productoNegativo * A[i][j]
        else:
             sumaPositivos = sumaPositivos + [i][j]
           
print ("La suma de los datos positivos es de: ", sumaPositivos)
print ("El producto de los datos negativos es de: ", productoNegativo)
           
           
