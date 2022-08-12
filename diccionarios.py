def run():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }

    print(mi_diccionario["llave1"])
    print(mi_diccionario["llave2"])
    print(mi_diccionario["llave3"])

    for elemento in mi_diccionario.keys():
        print(elemento)
    for elemento in mi_diccionario.values():
        print(elemento)

    for llave, numero in mi_diccionario.items():
        print(llave, numero)

if __name__ == "__main__":
    run()