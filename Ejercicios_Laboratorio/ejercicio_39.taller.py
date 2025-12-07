# Ejercico 39 #
# INICIO CODIGO #

print("El programa calculara el promedio de ambos numeros.")

def Pedir_Numero_1():
    Numero_1 = int(input("Ingresar 1er numero: "))
    return Numero_1

def Pedir_Numero_2():
    Numero_2 = int(input("Ingresar 2do numero: "))
    return Numero_2

def Calcular_Promedio(Numero_1,Numero_2):
    print (f"El promedio de ambos numeros es: {(Numero_1+Numero_2)/2}")


# ZONA CODIGO FINAL #
Llamar_Numero_1=Pedir_Numero_1()
Llamar_Numero_2=Pedir_Numero_2()
Llamar_Promedio=Calcular_Promedio(Llamar_Numero_1,Llamar_Numero_2)
print(Llamar_Promedio)