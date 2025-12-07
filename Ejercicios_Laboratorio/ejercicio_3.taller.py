## Calcular Area rectangulo #3
## INICIO CODIGO ##

def Ingresar_Lado_A():
    Lado_A=float(input("ingresa el Lado_Altura del Rectangulo: \n"))
    return Lado_A
def Ingresar_Lado_B():
    Lado_B=float(input("ingresa el Lado_Base del Rectangulo: \n"))
    return Lado_B

def Calcular_area(Lado_A, Lado_B):
    area= (Lado_A*Lado_B)
    return area

def Mostrar_mensaje(area):
    mensaje= (f"El area del Rectangulo es: ", area)
    return mensaje


#zona de codigo
Llamar_dato=Ingresar_Lado_A()
Llamar_dato_1=Ingresar_Lado_B()
Llamar_area=Calcular_area(Llamar_dato, Llamar_dato_1)
Llamar_mensaje=Mostrar_mensaje(Llamar_area)

print(Llamar_mensaje)