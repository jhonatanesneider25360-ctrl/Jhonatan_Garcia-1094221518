# Ejercico 15 #
# INICIO CODIGO #
print("Este programa hallara el area de un Paralelogramo.")
def Pedir_Base():
    Base=float(input("Ingresa la base del paralelogramo: "))
    return Base

def Pedir_Altura():
    Altura=float(input("Ingresa la altura del paralelogramo: "))
    return Altura

def Hallar_Area( Base,Altura ):
    print (f"La Area del paralelogramo es de: {Base*Altura}")
    
# ZONA CODIGO FINAL #
Llamar_Base=Pedir_Base()
Llamar_Altura=Pedir_Altura()
Calcular_Area=Hallar_Area(Llamar_Base, Llamar_Altura)
print(Calcular_Area)