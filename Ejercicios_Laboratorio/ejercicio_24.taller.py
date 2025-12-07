# Ejercico 24 #
# INICIO CODIGO #

print("Este programa calculara el cuadrado de un numero usando la multiplicacion. ")

def Pedir_Num():
    Numero=int(input("Ingresa el numero: "))
    return Numero

def calcular_cuadrado(Numero):
    Resultado=(Numero*Numero)
    return Resultado

def Imprimir(Resultado):
    print(f"El numero al cuadrado es {Resultado}")
    
# ZONA CODIGO FINAL #
Llamar_Numero=Pedir_Num()
Llamar_Resultado=calcular_cuadrado(Llamar_Numero)
Imprimir_Resultado=Imprimir(Llamar_Resultado)
print(Llamar_Resultado)