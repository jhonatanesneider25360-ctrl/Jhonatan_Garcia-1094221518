# Ejercico 9 #
# INICIO CODIGO #

print("Este programa hallara el area de un trapecio, ingresa sus lados y altura")

def Pedir_Altura():
    Altura=float(input("Ingresa la altura del trapecio: "))
    return Altura
def Pedir_Base_Menor():
    Base_Menor=float(input("Ingresa la Base menor del trapecio: "))
    return Base_Menor
def Pedir_Base_Mayor():
    Base_Mayor=float(input("Ingresa la Base mayor del trapecio: "))
    return Base_Mayor

def Hallar_Area(Altura, Base_Menor, Base_Mayor):
    print (f"El area de tu trapecio es: {Base_Mayor + Base_Menor * Altura / 2}")



# ZONA DE CODIGO #
Llamar_Altura=Pedir_Altura()
Llamar_Base_Menor=Pedir_Base_Menor()
Llamar_Base_Mayor=Pedir_Base_Mayor()
Llamar_area=Hallar_Area(Llamar_Altura,Llamar_Base_Menor,Llamar_Base_Mayor)
print(Llamar_area)