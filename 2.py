#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Escribir una función es_bisiesto() 
que determine si un año determinado 
es un año bisiesto. Un año bisiesto 
es divisible por 4, pero no por 100, 
a menos que también sea divisible por 400.
'''

def es_bisiesto(ano):
    # Verificar si el año es bisiesto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"El año {ano} es bisiesto.")
    else:
        print(f"El año {ano} no es bisiesto.")

# Solicitar al usuario un año
ano = int(input("Escriba un año para saber si es bisiesto: "))  # Convertimos la entrada a entero
es_bisiesto(ano)
