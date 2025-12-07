# Ejercico 31 #
# INICIO CODIGO #

print ("Este programa pasara las horas a minutos.")

def Pedir_Hora():
    horas = float(input("Ingresa el número de horas: "))
    return horas

def Convertir_Horas(horas):
    minutos = horas * 60     # conversión usando multiplicación (operador aritmético)
    return minutos

def Imprimir_Mensaje(minutos):
    print(f"La hora ingresada en minutos es de: {minutos}")
    
# ZONA CODIGO FINAL #
Llamar_Horas=Pedir_Hora()
Llamar_Proceso=Convertir_Horas(Llamar_Horas)
Imprimir=Imprimir_Mensaje(Llamar_Proceso)
print(Imprimir)