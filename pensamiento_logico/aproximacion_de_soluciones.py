objetivo = int(input("Escoge un numero: "))
epsilon = 0.001
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso
    print(respuesta, paso)
if abs(respuesta**2 - objetivo) >= epsilon:
    print(f"No se encontró la raíz cuadrada de {objetivo}")
else: 
    print(f"La raíz cuadrada de {objetivo} es {respuesta}")

