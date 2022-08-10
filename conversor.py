pesos = input("Ingresa la cantidad de pesos colombianos que tienes: ")
pesos = float(pesos)
valor_dolar = 4200

dolares = pesos/valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)

print("Tienes $" + dolares + " dólares")