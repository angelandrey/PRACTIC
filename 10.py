#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Escribir una función filtrar_palabras()
que tome una lista de palabras y un entero n, y devuelva las palabras que tengan más de n caracteres.
'''

def filtrar_palabras(lista, numero):
    # Filtrar las palabras que tienen más de 'numero' caracteres
    resultado = [palabra for palabra in lista if len(palabra) > numero]
    
    # Verificar si el resultado está vacío
    if len(resultado) == 0:
        print("Ninguna palabra :(")
    else:
        print(resultado)


# Lista de palabras y obtención del número desde el usuario
lista = ["sa", "sfsaf", "dsfds", "idsids"]
numero = int(input("Escribe un numero: "))  # Convertimos la entrada a entero

# Llamamos a la función con la lista y el número introducido por el usuario
filtrar_palabras(lista, numero)
