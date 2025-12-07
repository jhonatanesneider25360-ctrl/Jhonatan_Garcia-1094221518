# Ejercico 19 #
# INICIO CODIGO #

print("Este programa hallara el columen de un prisma triangular")

def Pedir_Base():
    Base=float(input("Ingresa la base del prisma: "))
    return Base

def Pedir_Longitud():
    Longitud=float(input("Ingresa la Longitud del prisma: "))
    return Longitud

def Pedir_Altura():
    Altura=float(input("Ingresa la altura del prisma: "))
    return Altura

def Calcular_Area(Base,Altura):
    Area_Triangulo= (Base*Altura/2)
    return Area_Triangulo

def Calcular_Volumen(Longitud,Area_Triangulo):
    Volumen= (Area_Triangulo*Longitud)
    return Volumen
def Imprimir(Volumen):
    print("El volumen de el prisma es de: ", Volumen)

# ZONA CODIGO FINAL #
Llamar_Base=Pedir_Base()
Llamar_Longitud=Pedir_Longitud()
Llamar_Altura=Pedir_Altura()
Llamar_Area=Calcular_Area(Llamar_Base,Llamar_Altura)
Llamar_Volumen=Calcular_Volumen(Llamar_Longitud,Llamar_Area)
Imprimir_Mensaje=Imprimir(Llamar_Volumen)
print(Imprimir_Mensaje)