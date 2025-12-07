## Calcular area del triangulo ##
## INICIO CODIGO ##

import math

def Ingresar_Radio():
    Radio=float(input("Ingrese el Radio del Cilindro: "))
    return Radio
def Ingresar_Altura(Radio):
    Altura=float(input("Ingrese el Altura del Cilindro: "))
    return Altura

def Calcular_Volumen(Radio, Altura):
    Volumen= math.pi * (Radio*2) * Altura
    return Volumen

def Mostrar_mensaje(Volumen):
    print (f"El volumen de tu Cilindro es: ", Volumen)


## Zona codigo ##
LLamar_dato=Ingresar_Radio()
Llamar_dato_1=Ingresar_Altura(LLamar_dato)
Llamar_Calculo=Calcular_Volumen(LLamar_dato,Llamar_dato_1)
Llamar_Resultado=Mostrar_mensaje(Llamar_Calculo)
print(Llamar_Resultado)