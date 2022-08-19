def palindromo(string):
    assert len(string) > 0, "no se puede ingresas una cadena vacía nigga"
    return string == string[::-1]

try: 
    print(palindromo(""))
except TypeError:
    print("No se aceptan numeros nigag")
