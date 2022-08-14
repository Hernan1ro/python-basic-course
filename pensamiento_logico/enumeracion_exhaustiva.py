objetivo = int(input("Escoge un número: "))

contador = 0;

while contador**2 < objetivo:
    contador += 1
if contador**2 == objetivo:
    print(f"La raiz cuadrada de {objetivo} es {contador}")
else:
    print(f"{objetivo} no tiene raiz cuadrada exacta")