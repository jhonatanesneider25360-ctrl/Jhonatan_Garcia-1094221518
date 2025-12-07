# Ejercico 22 #
# INICIO CODIGO #

print("Este programa hara la resta del 1er numero que ingreses menos el 2do.")

def Pedir_Num_1():
    Numero_1=int(input("Ingresa el primer numero: "))
    return Numero_1

def Pedir_Num_2():
    Numero_2=int(input("Ingresa el segundo numero: "))
    return Numero_2

def Restar(Numero_1,Numero_2):
    print(f"La Resta de los numeros es: {Numero_1-Numero_2}",)
    
# ZONA CODIGO FINAL #
Llamar_Numero_1=Pedir_Num_1()
Llamar_Numero_2=Pedir_Num_2()
Llamar_Resultado=Restar(Llamar_Numero_1,Llamar_Numero_2)
print(Llamar_Resultado)