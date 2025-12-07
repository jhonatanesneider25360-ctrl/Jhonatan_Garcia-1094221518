# Ejercico 11 #
# INICIO CODIGO #

print("Este programa pasara los kilometros a millas.")
def Pedir_Kilometros():
    Kilometros=float(input("Ingresa los Kilometros: "))
    return Kilometros
def Convertir_Kilometros(Kilometros):
    Millas=int(9.621371)
    Convercion= (Kilometros*Millas)
    return Convercion
def Imprimir_Resultado(Conversion):
    print(f"El resultado en Millas es :{Conversion}")

# ZONA CODIGO #
Llamar_Kilometros=Pedir_Kilometros()
Llamar_Conversion=Convertir_Kilometros(Llamar_Kilometros)
Llamar_Resultado=Imprimir_Resultado(Llamar_Conversion)
print(Llamar_Resultado)