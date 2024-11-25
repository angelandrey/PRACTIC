#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
'''

# Solicitar el año en curso y convertirlo a entero
ano_curso = int(input("Escribe el año en curso: "))

# Ingresar los datos de las tres personas
nombre_uno = input("Primer nombre: ")
ano_uno = int(input(f"Año de nacimiento de {nombre_uno}: "))

nombre_dos = input("Segundo nombre: ")
ano_dos = int(input(f"Año de nacimiento de {nombre_dos}: "))

nombre_tres = input("Tercer nombre: ")
ano_tres = int(input(f"Año de nacimiento de {nombre_tres}: "))

# Calcular la edad que cumplirá cada persona
cumple_uno = ano_curso - ano_uno
cumple_dos = ano_curso - ano_dos
cumple_tres = ano_curso - ano_tres

# Imprimir los resultados
print(f"{nombre_uno} cumplirá {cumple_uno} años en el año {ano_curso}.")
print(f"{nombre_dos} cumplirá {cumple_dos} años en el año {ano_curso}.")
print(f"{nombre_tres} cumplirá {cumple_tres} años en el año {ano_curso}.")
