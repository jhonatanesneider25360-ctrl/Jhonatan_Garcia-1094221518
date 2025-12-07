# Ejercico 20 #
# INICIO CODIGO #

print("Este programa pasara los Litros a Galones.")

def Pedir_Litros():
    Litros=float(input("Ingresar litros: "))
    return Litros

def Convertir_Litros(Litros):
    Galones=float(3.78541)
    Conversion= Litros/Galones
    return Conversion

def Imprimir_Resultado(Conversion):
    print(f"El resultado en Galones es: ",Conversion)

# ZONA CODIGO FINAL #
Llamar_Litros=Pedir_Litros()
Llamar_Conversion=Convertir_Litros(Llamar_Litros)
Llamar_Resultado=Imprimir_Resultado(Llamar_Conversion)
print(Llamar_Resultado)