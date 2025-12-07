# Ejercico 28 #
# INICIO CODIGO #

print("El programa hallara el area de un triangulo segun su base y altura dada.")

def Pedir_Base():
    Base=float(input("Ingresa la Base del triangulo: "))
    return Base
def Pedir_Altura():
    Altura=float(input("Ingresa la Altura del triangulo: "))
    return Altura

def Calcular_Area(Base,Altura):
    print(f"El area del triangulo es: {Base*Altura/2}")

# ZONA CODIGO FINAL #
Llamar_Base=Pedir_Base()
Llamar_Altura=Pedir_Altura()
Llamar_Resultado=Calcular_Area(Llamar_Base,Llamar_Altura)
print(Llamar_Resultado)