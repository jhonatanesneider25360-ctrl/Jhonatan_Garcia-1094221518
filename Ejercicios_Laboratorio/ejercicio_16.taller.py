# Ejercico 16 #
# INICIO CODIGO #

print("Este programa hallara el area de un Cubo.")

def Pedir_Lado():
    Lado=float(input("Ingresa un lado del Cubo: "))
    return Lado

def Hallar_Volumen(Lado):
    Volumen= (Lado*Lado*Lado)
    return Volumen

def Imprimir_Volumen(Volumen):
    print("El Volumen del cubo es de: ",Volumen)
    
# ZONA CODIGO FINAL #
Llamar_Lado=Pedir_Lado()
Calcular_Volumen=Hallar_Volumen(Llamar_Lado)
Imprimir=Imprimir_Volumen(Calcular_Volumen)
print(Imprimir)