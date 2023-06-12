suma = 0

while True:
    num = int(input("Ingrese un número entero: "))
    suma += num
    continuar = input("¿Desea ingresar otro número? (Ingrese 'sí' para continuar): ")
    if continuar.lower() != "sí":
        break

print("La suma de los números ingresados es:", suma)