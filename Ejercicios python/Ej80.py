#En el ejercicio anteriro de la madres y padres (ej78) contar cuantos padres tienen más de 2 hijos 
# y mostrar el nombre de los padres cuando no tengan hijos

padres=[]
hijos=[]
for K in range (3):
    pa=input("Ingrese el nombre del padre:")
    ma=input("Ingrese el nombre de la madre:")
    padres.append([pa,ma])
    cant=int(input("Ingrese cantidad de hijos por familia"))
    hijos.append([])
    for x in range(cant):
     nom=input("Ingrese el nombre del hijo:")
     hijos[K].append(nom)
print("Listado del padre, madre y sus hijos")

for k in range (3):
    print("Padre:", padres[K][0])
    print("Madre:", padres[K][1])
    for x in range(len(hijos[K])):
       print("Hijos:", hijos[K][x])
print("Listado de padres y cantidad de hijos que tiene")
for x in range(3):
   print("Padre:", padres[x][0])
   print("Cantidad de hijos;", len(hijos[x]))

cantfaltantes=0
for x in range(3):
    if len(hijos[x])>2:
        cantfaltantes=cantfaltantes+1
print ("cantidad de hijos mayor a dos: ", cantfaltantes)

print ("Padres sin hijos: ")
for x in range(3):
    if len(hijos[x])==0:
        print (padres[x])
