# Ejercico 10 #
# INICIO CODIGO #

print("Este programa hallara el Volumen de un prisma rectangular.")

def Pedir_Longitud():
    Longitud=float(input("Ingresa la Longitud del prisma: "))
    return Longitud
def Pedir_Anchura():
    Ancho=float(input("Ingresa el Ancho del prisma: "))
    return Ancho
def Pedir_Altura():
    Altura=float(input("Ingresa la Altura del Prisma: "))
    return Altura

def Hallar_Volumen( Longitud,Ancho,Altura ):
    print (f"El Volumen del Prisma es: {(Longitud*Ancho*Altura)}")





# ZONA DE CODIGO #
Llamar_Longitud=Pedir_Longitud()
Llamar_Anchura=Pedir_Anchura()
Llamar_Altura=Pedir_Altura()
Llamar_Volumen=Hallar_Volumen(Llamar_Longitud,Llamar_Anchura,Llamar_Altura)
print (Llamar_Volumen)