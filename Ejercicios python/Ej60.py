nombres = ["Juan", "Pedro", "Lucas", "Luna  ", "Alberto"]

contador = 0


for nombre in nombres:
    if len(nombre) > 5:
        contador += 1


print("Cantidad de nombres con más de 5 caracteres:", contador)