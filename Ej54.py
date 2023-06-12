clave = input("Ingrese una clave: ")

caracteres = len(clave)
if 10 <= caracteres <= 20:
    print("La clave es válida.")
else:
    print("La clave no es válida porque tiene menos de 10 caracteres o mas de 20.")