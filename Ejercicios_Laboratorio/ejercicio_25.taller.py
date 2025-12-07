# Ejercico 25 #
# INICIO CODIGO #

print("Este programa calculara la division de un numero por el segundo numero ingresado. ")

def Pedir_Num_1():
    Numero_1=int(input("Ingresa el primer numero: "))
    return Numero_1

def Pedir_Num_2():
    Numero_2=int(input("Ingresa el segundo numero: "))
    return Numero_2

def Dividir_Numero(Numero_1,Numero_2):
    if Numero_2==0:
        print("El numeero no es divisible en 0.")
    elif Numero_1==0:
        print("El numero no se puede dividir. ")
    else:
        Resultado=(Numero_1/Numero_2)
        print(f"El resultado de la division es: {Resultado}")

# ZONA CODIGO FINAL #
Llamar_Numero_1=Pedir_Num_1()
Llamar_Numero_2=Pedir_Num_2()
Llamar_Resultado=Dividir_Numero(Llamar_Numero_1,Llamar_Numero_2)
print(Llamar_Resultado)