## Calcular Area de Circulo##
## INICIO CODIGO ##

import math
def Ingresar_radio():
    radio=float(input("ingresa el radio del circulo: \n"))
    return radio

def Calcular_area(radio):
    area= math.pi * (radio**2)
    return area

def Mostrar_mensaje(area):
    mensaje= (f"El area del circulo es: ", area)
    return mensaje
def Imprimir_Mensaje(mensaje):
    print (mensaje)

#zona de codigo
Llamar_dato=Ingresar_radio()
Llamar_area=Calcular_area(Llamar_dato)
Llamar_mensaje=Mostrar_mensaje(Llamar_area)
Imprimir=Imprimir_Mensaje(Llamar_mensaje)
print(Imprimir)