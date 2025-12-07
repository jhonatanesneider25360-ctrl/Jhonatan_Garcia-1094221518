## Calcular area del triangulo ##
## INICIO CODIGO ##

def Ingresar_base():
    base=float(input("ingresa la base del Tringulo : \n"))
    return base
def Ingresar_altura():
    altura=float(input("ingresa la altura del Triangulo : \n"))
    return altura

def Calcular_area(base, altura):
    area= (base*altura) /2
    return area

def Mostrar_mensaje(area):
    mensaje= (f"El area del triangulo es: ", area)
    return mensaje
def Imprimir_Mensaje(mensaje):
    print (mensaje)

#zona de codigo
Llamar_dato=Ingresar_base()
Llamar_dato_1=Ingresar_altura()
Llamar_area=Calcular_area(Llamar_dato, Llamar_dato_1)
Llamar_mensaje=Mostrar_mensaje(Llamar_area)
Imprimir=Imprimir_Mensaje(Llamar_mensaje)
print(Imprimir)