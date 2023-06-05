lista_enteros = []

while True:
    entero = int(input("Ingrese un entero (0 finaliza): "))
    if entero == 0:
        break
    lista_enteros.append(entero)

print("lista:", len(lista_enteros))