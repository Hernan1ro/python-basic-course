def run():
    mi_diccionario = {
        "Jaime": 2,
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }

    print(mi_diccionario.get("Juan", "No existe el nombre de juan"))
    mi_diccionario["Hernan"] = 70


    del mi_diccionario["Jaime"]

    print("Jaime" in mi_diccionario)

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