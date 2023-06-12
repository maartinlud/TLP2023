sueldos = []

for i in range(5):
    sueldo = float(input("Ingrese el sueldo del operario: "))
    sueldos.append(sueldo)

print("Lista :", sueldos)

promedio = sum(sueldos) / len(sueldos)

print("Promedio : ", promedio)

