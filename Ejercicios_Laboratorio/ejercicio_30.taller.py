# Ejercico 30 #
# INICIO CODIGO #

print ("Este programa hallara la circunferencia del circulo con el radio dado.")

def Pedir_Radio():
    radio = float(input("Ingrese el radio del círculo: "))
    return radio

def crear_circunferencia(radio):
    pi = 3.1416
    circunferencia = 2 * pi * radio
    return circunferencia

def Imprimir_Mensaje(circunferencia):
    print(f"La circunferencia del circulo es de {circunferencia}")
    
# ZONA CODIGO FINAL #
Llamar_Radio=Pedir_Radio()
Llamar_Proceso=crear_circunferencia(Llamar_Radio)
Imprimir=Imprimir_Mensaje(Llamar_Proceso)
print(Imprimir)