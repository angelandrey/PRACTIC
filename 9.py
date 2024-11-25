# Definir una tupla con 10 edades de personas
# tupla = (20, 23, 46, 3, 2, 54, 23, 34, 24, 64)

# Opción para que el usuario ingrese las edades
edades = []
for i in range(10):
    edad = int(input("Escribe una edad: "))
    edades.append(edad)

# Contar cuántas personas tienen edades superiores a 20
cantidad = 0
for edad in edades:
    if edad > 20:
        cantidad += 1

print(f"Cantidad de personas con edades superiores a 20: {cantidad}")
