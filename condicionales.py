# Condicionales sencillas

menu = """
Bienvenido al verificador de edad

En este lugar hay restricción de edad

Por favor introduce tu edad: """

edad = int(input(menu))
if edad > 17:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


numero = int(input("Escribe un número: "))

if numero > 5:
    print("Es mayor a 5")
elif numero == 5:
    print("Es igual a 5")
else: 
    print("Es menor a 5")