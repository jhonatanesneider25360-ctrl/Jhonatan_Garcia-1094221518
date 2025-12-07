# Ejercico 17 #
# INICIO CODIGO #

print("Este programa pasara las Libras a Kilogramos.")

def Pedir_Libras():
    Libras=float(input("Ingresar libras: "))
    return Libras

def Convertir_Libras(Libras):
    Kilogramos=float(0.453592)
    Convercion= Libras*Kilogramos
    return Convercion

def Imprimir_Resultado(Convercion):
    print(f"El resultado en Kilogramos es: ",Convercion)

# ZONA CODIGO FINAL #
Llamar_Libras=Pedir_Libras()
Llamar_Conversion=Convertir_Libras(Llamar_Libras)
Llamar_Resultado=Imprimir_Resultado(Llamar_Conversion)
print(Llamar_Resultado)
