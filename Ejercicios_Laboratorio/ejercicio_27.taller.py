# Ejercico 27 #
# INICIO CODIGO #

print("Este programa hallara la rai cuadrada de un numero.")

def Pedir_Numero(): 
    Numero = float(input("Ingresa un número: "))
    return Numero
def Calcular_Raiz(Numero):
    raiz = Numero ** 0.5   # operador aritmético de potencia
    return raiz
def Imrimir(Raiz):
    print("La raíz cuadrada es:", Raiz)
    
# ZONA CODIGO FINAL #
Llamar_Numero=Pedir_Numero()
Llamar_Resultado=Calcular_Raiz(Llamar_Numero)
print(Llamar_Resultado)