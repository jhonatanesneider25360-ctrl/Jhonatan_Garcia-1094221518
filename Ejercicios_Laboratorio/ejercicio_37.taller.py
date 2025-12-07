# Ejercico 37 #
# INICIO CODIGO #

print("Este programaa determinara si el primer numero es múltiplo del segundo usando el operador módulo (%).")

def Pedir_Numero_1():
    Numero_1 = int(input("Ingresar 1er numero: "))
    return Numero_1

def Pedir_Numero_2():
    Numero_2 = int(input("Ingresar 2do numero: "))
    return Numero_2

def Determinar_Multiplo(Numero_1,Numero_2):
    if Numero_1 % Numero_2 == 0:
        print("El primer número ES múltiplo del segundo")
    else:
        print("El primer número NO es múltiplo del segundo")
        
# ZONA CODIGO FINAL #
Llamar_Numero_1=Pedir_Numero_1()
Llamar_Numero_2=Pedir_Numero_2()
Llamar_Proceso=Determinar_Multiplo(Llamar_Numero_1,Llamar_Numero_2)
print(Llamar_Proceso)