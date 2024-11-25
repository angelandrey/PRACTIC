import random

# Definir los descuentos correspondientes a los colores
descuentos = {
    "blanco": 1.0,  # sin descuento
    "rojo": 0.9,    # 10% de descuento
    "azul": 0.8,    # 20% de descuento
    "verde": 0.75,   # 25% de descuento
    "amarillo": 0.5  # 50% de descuento
}

x = 0
while x == 0:
    # Solicitar el monto de la compra
    cantidad_compra = float(input("Introduzca la cantidad total de la compra: "))
    
    # Verificar si la compra es mayor o igual a 100
    if cantidad_compra >= 100:
        # Generar un número aleatorio para seleccionar un color de bola
        bola_color = random.choice(list(descuentos.keys()))
        
        # Obtener el descuento basado en el color de la bola
        descuento = descuentos[bola_color]
        
        # Si es blanco, no hay descuento
        if bola_color == "blanco":
            print("La bola es blanca, no hay descuento.")
            print(f"Total a pagar: {cantidad_compra}")
        else:
            # Calcular el nuevo precio con el descuento
            nuevo_precio = cantidad_compra * descuento
            print(f"La bola es de color {bola_color}, tienes un descuento del {int((1 - descuento) * 100)}%")
            
