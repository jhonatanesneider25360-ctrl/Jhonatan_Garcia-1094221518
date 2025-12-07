# Ejercico 35 #
# INICIO CODIGO #

print("Este programa calculara el 5% de interes del Dinero que ingreses en la cuenta.")

def Pedir_Cantidad_Dinero():
    Dinero = float(input("Ingrese la cantidad de dinero en la cuenta: "))
    return Dinero

def Calcular_Interes(Dinero):
    Interes= 0.05
    Total_Interes = Dinero * Interes 
    return Total_Interes

def Imprimir(Total_Interes):
    print(f"El Interes del dinero ingresado es de: {Total_Interes}$")

# ZONA CODIGO FINAL #
Llamar_Dinero=Pedir_Cantidad_Dinero()
Llamar_Interes=Calcular_Interes(Llamar_Dinero)
Llamar_Impresion=Imprimir(Llamar_Interes)
print(Llamar_Impresion)