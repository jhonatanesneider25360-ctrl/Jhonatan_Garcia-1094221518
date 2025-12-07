# Ejercico 26 #
# INICIO CODIGO #

print("Este programa sacara el residuo dee una division de dos numeros ingresados.")

def Pedir_Num_1():
    Numero_1=int(input("Ingresa el primer numero: "))
    return Numero_1

def Pedir_Num_2():
    Numero_2=int(input("Ingresa el segundo numero: "))
    return Numero_2

def Calcular_Residuo(Numero_1,Numero_2):
    if Numero_2 == 0:
        print ("Error: no se puede dividir entre cero.")
    else:
        residuo = Numero_1 % Numero_2
        print( "El residuo de la división es: ", residuo)

# ZONA CODIGO FINAL #
Llamar_Numero_1=Pedir_Num_1()
Llamar_Numero_2=Pedir_Num_2()
Llamar_Resultado=Calcular_Residuo(Llamar_Numero_1,Llamar_Numero_2)
print(Llamar_Resultado)