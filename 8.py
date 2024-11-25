#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Solicitar la cantidad de dólares, tasa de interés y número de años
cantidad_dolares = float(input("Ingresa una cantidad de dólares: "))
tasa_interes = float(input("Ingresa la tasa de interés (%): "))
numero_anos = int(input("Ingresa el total de años: "))

# Calcular el capital final usando la fórmula del interés compuesto
capital_final = cantidad_dolares * (1 + tasa_interes / 100) ** numero_anos

# Imprimir el capital final
print(f"El capital final después de {numero_anos} años es: {capital_final:.2f}")
