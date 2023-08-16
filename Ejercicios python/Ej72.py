#crear una lista por asignación. la lista tiene que tener 2 elementos. Cada elemento debe ser 5 enteros. Calcular y mostrar la suma de cada lista contenida en la lista ppal #
lista=[[1,2,3,4,5],[7,8,9,10,11]]
suma1=0
suma2=0
print(lista)
print(lista[0])
print(lista[0][0])
for x in range (len(lista[0])):
       suma1=suma1+lista[0][x]
for x in range (len(lista[1])):
       suma2=suma2+lista[1][x]
print (suma1)
print (suma2)
       