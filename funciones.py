#Funcion tradicional

# def imprimir_mensaje():
#     print("Mensaje especial: ")
#     print("!Estoy aprendiendo a utilizar funciones")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def conversacion(mensaje):
    print("Hola")
    print("Como estás")
    print(mensaje)
    print("adios")

opcion = int(input("Elige una opción (1, 2, 3): "))
if opcion == 1:
    conversacion("Elegiste la opción 1")
elif opcion == 2:
    conversacion("Elegiste la opción 2")
elif opcion == 3:
    conversacion("Elegiste la opción 3")
else:
    print("Escribe la opción correcta")
