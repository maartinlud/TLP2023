nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")

nombres = [nombre1, nombre2]

if nombre1 < nombre2:
    nombre_mayor = nombre2
    nombre_menor = nombre1
    print(nombre_mayor)
    print(nombre_menor)
else:
   nombre_mayor = nombre1
   nombre_menor = nombre2
   print(nombre_mayor)
   print(nombre_menor)
