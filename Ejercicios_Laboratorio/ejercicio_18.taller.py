# Ejercico 17 #
# INICIO CODIGO #

print("Este programa hallara el area de un Hexagono regular.")

import math 
def Pedir_Lado():
    Lado=float(input("Ingresa un lado del Hexagono: "))
    return Lado

def Hallar_Area(Lado):
    Area= (3*math.sqrt(3)/2)*(Lado**2)
    return Area

def Imprimir_Area(Area):
    print("El Area del Hexagono es de: ",Area)
    

# ZONA CODIGO FINAL #
Llamar_Lado=Pedir_Lado()
Llamar_Area=Hallar_Area(Llamar_Lado)
Llamar_Resultado=Imprimir_Area(Llamar_Area)
print(Llamar_Resultado)