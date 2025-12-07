# Ejercico 11 #
# INICIO CODIGO #

print("Este programa pasara las Pulgadas a Centimetroas.")
def Pedir_Pulgadas():
    Pulgadas=float(input("Ingresa Pulgadas: "))
    return Pulgadas
def Convertir_Pulgadas(Pulgadas):
    Centimetros=int(2.54)
    Convercion= (Pulgadas*Centimetros)
    return Convercion

def Imprimir_Resultado(Conversion):
    print(f"El resultado en Centimetros es :{Conversion}")

# ZONA CODIGO FINAL #
Llamar_Pulgadas=Pedir_Pulgadas()
Llamar_Conversion=Convertir_Pulgadas(Llamar_Pulgadas)
Llamar_Resultado=Imprimir_Resultado(Llamar_Conversion)
print(Llamar_Resultado)