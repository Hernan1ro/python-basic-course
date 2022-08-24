import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match


if __name__ == '__main__':
    size = int(input("De que tamaño será la lista? "))
    objetivo = int(input("Qué número quieres encontrar"))

    lista = [random.randint(0, 100) for i in range(size)]
    
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no está"} en la lista')