# Ejercico 38 #
# INICIO CODIGO #

print("El programa mostrara que numero es mayor entre dos numeros ingresados, usando opreadores aritmeticos.")

def Pedir_Numero_1():
    Numero_1 = int(input("Ingresar 1er numero: "))
    return Numero_1

def Pedir_Numero_2():
    Numero_2 = int(input("Ingresar 2do numero: "))
    return Numero_2

def Comprobar_Numero_Mayor(Numero_1,Numero_2):
    if Numero_1 - Numero_2 > 0:
        print("El número mayor es el primer numero ingresasdo:", Numero_1)
    elif Numero_2 - Numero_1 > 0:
        print("El número mayor es el segundo numero ingresado:", Numero_2)
    else:
        print("Ambos números son iguales")

# ZONA CODIGO FINAL #
Llamar_Numero_1=Pedir_Numero_1()
Llamar_Numero_2=Pedir_Numero_2()
Llamar_Resultado=Comprobar_Numero_Mayor(Llamar_Numero_1,Llamar_Numero_2)
print(Llamar_Resultado)