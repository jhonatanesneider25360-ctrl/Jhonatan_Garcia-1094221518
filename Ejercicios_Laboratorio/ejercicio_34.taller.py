# Ejercico 34 #
# INICIO CODIGO #

print("Este programa calculara el 10% del precio que ingreses.")

def Pedir_Precio():
    Precio = float(input("Ingresa el precio del artículo: "))
    return Precio

def Calcular_Descuento(Precio):
    Descuento = Precio * 0.10      
    return Descuento

def Calcular_Precio_Total(Precio, Descuento):
    Total= Precio - Descuento
    return Total
    
def Imprimir(Total,Descuento):
    print(f"El descuento del articulo es de: {Descuento}\nEl precio a pagar es de: {Total}")

# ZONA CODIGO FINAL #
Llamar_Precio=Pedir_Precio()
Llamar_Descuento=Calcular_Descuento(Llamar_Precio)
Llamar_Total=Calcular_Precio_Total(Llamar_Precio,Llamar_Descuento)
Llamar_Impresion=Imprimir(Llamar_Total,Llamar_Descuento)
print(Llamar_Impresion)