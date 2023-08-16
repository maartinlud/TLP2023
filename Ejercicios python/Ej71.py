#crear una lista por asignación. la lista tiene que tener 4 elementos. Cada elemento debe ser una lista de 3 enteros. Imprimir sus elementos accediendo de diferentes modos#
lista=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(lista)
print(lista[0])
print(lista[0][0])
for k in range(len(lista)):
    for x in range (len(lista[k])):
        print(lista[k][x])