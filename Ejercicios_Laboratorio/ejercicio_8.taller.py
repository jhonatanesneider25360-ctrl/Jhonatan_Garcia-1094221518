## Convertir Dolares a Euros ##
## INICIO CODIGO ##

def Ingresar_Dolares():
    Dolares=int(input("Ingrese cuantos dolares vas a convertir: "))
    return Dolares
def Ingresar_Tasa_de_Cambio(Dolares):
    Tasa_Cambio=int(input("Ingrese en cuanto esta el valor de la Tasa de cambio: "))
    return Tasa_Cambio

def Convertir_a_Euros(Dolares,Tasa_Cambio):
    Euros= Dolares*Tasa_Cambio
    return Euros

def Mostrar_Mensaje(Euros):
    mensaje= (f"Has convertido tus Dolares =  {Dolares} a Euros=  {Euros}  ")
    return mensaje


## Zona de codigo ##
Llamar_dato_Dolares=Ingresar_Dolares()
Llamar_dato_Tasa_de_Cambio=Ingresar_Tasa_de_Cambio(Llamar_dato_Dolares)
Llamar_Conversion=Convertir_a_Euros(Llamar_dato_Tasa_de_Cambio)
Imprimir_en_terminal=Mostrar_Mensaje(Llamar_Conversion)
print (Imprimir_en_terminal)