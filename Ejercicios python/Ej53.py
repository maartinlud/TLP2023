oracion = input("Ingrese una oración: ")

vocales = 0
for carac in oracion:
    if carac.lower() in "aeiou":
        vocales += 1

print("vocales:", vocales)

oracionmayus = oracion.upper()
print("Oración en mayuscula:", oracionmayus)

cantidadcarac = len(oracion)
print("caracteres:", cantidadcarac)
