sueldos_manana = []
sueldos_tarde = []

print("Ingrese los sueldos para el turno de la mañana:")
for i in range(4):
    sueldo = float(input("Empleado {}: ".format(i+1)))
    sueldos_manana.append(sueldo)

print("Ingrese los sueldos para el turno de la tarde:")
for i in range(4):
    sueldo = float(input("Empleado {}: ".format(i+1)))
    sueldos_tarde.append(sueldo)

print("Sueldos del turno de la mañana:", sueldos_manana)
print("Sueldos del turno de la tarde:", sueldos_tarde)
