## Convertir Celcius a Fahrenheit ##
# INICIO DE CODIGO #

def Ingresar_Grados_Celcius():
    Celcius=float(input("ingresa los grados en celcius: "))
    return Celcius


def Calcular_Celcius_a_Fahrenheit(Celcius):
    Fahrenheit= (Celcius*9/5)+32
    return Fahrenheit

def Mostrar_mensaje(Fahrenheit):
    mensaje= (f"Los grados convertidos de Celcius a Fahrenheit son : ", Fahrenheit)
    return mensaje


# zona de codigo #
Llamar_Celcius=Ingresar_Grados_Celcius()
Llamar_Calculo=Calcular_Celcius_a_Fahrenheit(Llamar_Celcius)
Llamar_mensaje=Mostrar_mensaje(Llamar_Calculo)
print(Llamar_mensaje)