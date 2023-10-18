#Definir una lista y almacenar los nombres de 3 empleados, por otro lado definir otra lista y almacenar#
#en cada elemento una sublista con los números del día del mes que el empleado faltó.#
#Imprimir los nombres de empleador y los días que faltó. Mostrar los empleados con la cantidad de dias faltados#
#Mostrar los empleados con la cantidad de dias faltados mayores a 10, finalmente mostrar el nombre o #
#los nombres de los empleados con menos de 3 faltas.#

empleados=[]
faltas=[]
for k in range (3):
    empleado=input("Ingrese el nombre del empleado:")
    empleados.append([empleado])
    falta=int(input("Ingrese cantidad de faltas por empleado"))
    faltas.append([])
    for x in range(falta):
        dia=int(input("Ingrese el numero de dia que faltó"))
        faltas[k].append(dia)
print("nombres de empleado y días que faltó")
for k in range (3):
    print("Empleado:", empleados[k])
    for x in range(len(faltas[k])):
       print("dia:", faltas[k][x])
print("Nombres de empleados y cantidad de inasistencias mayores a 10")
for x in range(3):
    print(empleados[x],len(faltas[x]))
for x in range(1,3):
    if len(faltas[x])>10:
        cantfaltantes=0
        cantfaltantes=cantfaltantes+1
print ("Empleado o empleados que faltaron menor a 3")
for x in range(3):
    if len(faltas[x])<3:
        print (empleados[x])


    
