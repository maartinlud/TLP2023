#Definir 2 listas de 3 elementos#
#La primera lista cada elemento es una sublista con el nombre del padre y la madre de una familia#
#La segunda lista está constituida por listas con los nombres de los hijos de c/familia#
#Puede haber familia sin hijos. Imprimir los nombres del padre, madre y sus hijos. Imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre#

padres=[]
hijos=[]
for K in range (3):
    pa=input("Ingrese el nombre del padre:")
    ma=input("Ingrrese el nombre de la madre:")
    padres.append([pa,ma])
    cant=input("Ingrese cantidad de hijos por familia")
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
    for K in range(3):
        pa=input("Ingese el nombre del padre:")
        ma=input("Ingrese el nombre de la madre:")
        padres.append([pa,ma])
        cant=input("Ingrese cantidad de hijos por familia")


