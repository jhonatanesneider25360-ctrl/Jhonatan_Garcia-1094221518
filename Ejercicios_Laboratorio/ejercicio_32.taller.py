# Ejercico 32 #
# INICIO CODIGO #

print ("Este programa hallara el area de un rectangulo con la longitud y anchura dada")

def Pedir_Longitud():
    Longitud = float(input("Ingrese la longitud del rectángulo: "))
    return Longitud

def Pedir_Ancho():
    Ancho = float(input("Ingrese el ancho del rectángulo: "))
    return Ancho

def Crear_Area(Longitud,Ancho):
    Area = Longitud * Ancho
    return Area
    
def Imprimir_Mensaje(Area):
    print(f"El areea del rectangulo es de {Area}")

    
# ZONA CODIGO FINAL #
Llamar_Longitud=Pedir_Longitud()
Llamar_Ancho=Pedir_Ancho()
Llamar_Proceso=Crear_Area(Llamar_Longitud,Llamar_Ancho)
Imprimir=Imprimir_Mensaje(Llamar_Proceso)
print(Imprimir)