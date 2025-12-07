# Ejercico 23 #
# INICIO CODIGO #

print("Este programa hallara el procuto de dos numeros ingresados.")

def Pedir_Num_1():
    Numero_1=int(input("Ingresa el primer numero: "))
    return Numero_1

def Pedir_Num_2():
    Numero_2=int(input("Ingresa el segundo numero: "))
    return Numero_2

def Sacar_Producto(Numero_1,Numero_2):
    print(f"El producto de los numeros es: {Numero_1*Numero_2}",)
    
# ZONA CODIGO FINAL #
Llamar_Numero_1=Pedir_Num_1()
Llamar_Numero_2=Pedir_Num_2()
Llamar_Resultado=Sacar_Producto(Llamar_Numero_1,Llamar_Numero_2)
print(Llamar_Resultado)