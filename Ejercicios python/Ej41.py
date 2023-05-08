edades_manana = []
for i in range(5):
    edad = int(input("Ingrese la edad de un estudiante del turno mañana: "))
    edades_manana.append(edad)

edades_tarde = []
for i in range(6):
    edad = int(input("Ingrese la edad de un estudiante del turno tarde: "))
    edades_tarde.append(edad)

edades_noche = []
for i in range(11):
    edad = int(input("Ingrese la edad de un estudiante del turno noche: "))
    edades_noche.append(edad)


promedio_manana = sum(edades_manana) / len(edades_manana)
promedio_tarde = sum(edades_tarde) / len(edades_tarde)
promedio_noche = sum(edades_noche) / len(edades_noche)


print("Promedio de edad del turno mañana:", promedio_manana)
print("Promedio de edad del turno tarde:", promedio_tarde)
print("Promedio de edad del turno noche:", promedio_noche)


if promedio_manana > promedio_tarde and promedio_manana > promedio_noche:
    print("El turno mañana tiene el promedio de edad mayor.")
elif promedio_tarde > promedio_manana and promedio_tarde > promedio_noche:
    print("El turno tarde tiene el promedio de edad mayor.")
else:
    print("El turno noche tiene el promedio de edad mayor.")
