# Ejercico 13 #
# INICIO CODIGO #

print("Este programa  hallara el Volumen de una piramide cuadrada.")
def Pedir_Longitud():
    Longitud=float(input("Ingresa la longitud de la piramide: "))
    return Longitud
def Pedir_Anchura():
    Ancho=float(input("Ingresa el ancho de la piramide: "))
    return Ancho
def Pedir_Altura():
    Altura=float(input("Ingresa la altura de la piramide: "))
    return Altura

def Hallar_Volumen( Longitud,Ancho,Altura ):
    print (f"El Volumen de la piramide cuadrada es: {(Longitud*Ancho*Altura/3)}")



# ZONA CODIGO FINAL #
Llamar_Longitud=Pedir_Longitud()
Llamar_Anchura=Pedir_Anchura()
Llamar_Altura=Pedir_Altura()
Llamar_Volumen=Hallar_Volumen(Llamar_Longitud,Llamar_Anchura,Llamar_Altura)
print (Llamar_Volumen)