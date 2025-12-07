# Ejercico 12 #
# INICIO CODIGO #

print("Este programa hallara el area de un cuadrado.")
def Pedir_Lado():
    Lado=float(input("Ingresa el lado del cuadrado: "))
    return Lado
def Calcular_Area(Lado):
    Area= (Lado*Lado)
    return Area
def Imprimir_Resultado(Area):
    Mensaje= (f"El Area del cuadrado es: {Area}")
    return Mensaje

# ZONA CODIGO FINAL #
Llamar_Dato=Pedir_Lado()
Llamar_Calculo=Calcular_Area(Llamar_Dato)
Llamar_Mensaje=Imprimir_Resultado(Llamar_Calculo)
print(Llamar_Mensaje)