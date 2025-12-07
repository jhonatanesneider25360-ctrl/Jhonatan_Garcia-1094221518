## Calcular Volumen de Cono ##
## INICIO CODIGO ##

import math
def Ingresar_radio():
    radio=float(input("ingresa el radio del Cono: \n"))
    return radio
def Ingresar_Altura():
    altura=float(input("ingresa la altura del Cono: \n"))
    return altura

def Calcular_area(radio, altura):
    volumen= (1/3) * math.pi * (radio**2) * altura
    return volumen

def Mostrar_mensaje(volumen):
    mensaje= (f"El Volumen del Cono es : ", volumen)
    return mensaje


#zona de codigo
Llamar_dato=Ingresar_radio()
Llamar_dato_1=Ingresar_Altura()
Llamar_area=Calcular_area(Llamar_dato, Llamar_dato_1)
Llamar_mensaje=Mostrar_mensaje(Llamar_area)
print(Llamar_mensaje)