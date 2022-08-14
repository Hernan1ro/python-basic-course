objetivo = int(input("Escoge un número para sacar su raíz cuadrada: "))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo )
respuesta = (alto + bajo)/2

while abs(respuesta**2 - objetivo) >= epsilon:
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (alto + bajo)/2
print(f"La raíz cuadrada de {objetivo} es {respuesta}")
