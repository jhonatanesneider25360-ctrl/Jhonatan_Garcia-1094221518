# Ejercico 33 #
# INICIO CODIGO #

print("Este programa pasara los kilometros a millas.")

def Pedir_Kilometros():
    Kilometros = float(input("Ingrese la distancia en kilómetros: "))
    return Kilometros

def Convertir_Kilometros(Kilometros):
    millas = 0.621371
    Resultado=Kilometros*millas
    return Resultado

def Imprimir(Resultado):
    print(f"La conversion de kilometros a millas es de {Resultado}")
    
# ZONA CODIGO FINAL #
Llamar_Kilometros=Pedir_Kilometros()
Llamar_Conversion=Convertir_Kilometros(Llamar_Kilometros)
Llamar_Impresion=Imprimir(Llamar_Conversion)
print(Llamar_Impresion)