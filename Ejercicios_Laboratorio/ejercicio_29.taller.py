# Ejercico 29 #
# INICIO CODIGO #

print("El programa determinara si tu numero es par o impar.")

def Pedir_Numero():
    Numero = int(input("Ingresa un número: "))
    return Numero

def Determinar_Valor(Numero):
    if Numero % 2 == 0:
        print("El numero es: PAR")
    else:
        print("El numero es: IMPAR")

# ZONA CODIGO FINAL #
LLamar_Numero=Pedir_Numero()
Llamar_Proceso=Determinar_Valor(LLamar_Numero)
print(Llamar_Proceso)