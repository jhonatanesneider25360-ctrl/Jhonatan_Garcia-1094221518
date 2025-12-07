# Ejercico 36 #
# INICIO CODIGO #

print("Este programa mostrara el cociente de una division entera.")

def Pedir_Numero_Dividendo():
    Numero_1 = int(input("Ingrese el numero que sera dividido (Dividendo) : "))
    return Numero_1

def Pedir_Numero_Divisor():
    Numero_2 = int(input("Ingrese el numero que dividira al Dividendo (Divisor) : "))
    return Numero_2

def Calcular_Division(Numero_1,Numero_2):
    Cociente=Numero_1//Numero_2
    return Cociente

def Imprimir(Cociente):
    print(f"El cociente de la division es: {Cociente}")

# ZONA CODIGO FINAL #
Llamar_Dividendo=Pedir_Numero_Dividendo()
Llamar_Divisor=Pedir_Numero_Divisor()
Llamar_Division=Calcular_Division(Llamar_Dividendo, Llamar_Divisor)
Llamar_Impresion=Imprimir(Llamar_Division)
print(Llamar_Impresion)