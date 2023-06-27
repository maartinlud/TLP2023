alturas = []
for i in range(5):
    altura = float(input("Ingresa la altura de la persona {}: ".format(i+1)))
    alturas.append(altura)

promedio = sum(alturas) / len(alturas)


contador_altas = 0
for altura in alturas:
    if altura > promedio:
        contador_altas += 1

persona_mas_baja = min(alturas)
persona_mas_alta = max(alturas)


print("Promedio de alturas: {:.2f}".format(promedio))
print("Personas más bajas: {:.2f}".format(persona_mas_baja))
print("Personas más altas: {:.2f}".format(persona_mas_alta))
print("Cantidad de personas más altas que el promedio: {}".format(contador_altas))
