#Solicitar por teclado dos enteros. El primer valor indica la cantidad de elementos que crearemos en la lista.#
#El segundo vlaor indica la cantidad de elementos que tendrá cada una de las listas internas a la principal.#
#Mostrar la lista y la suma de todos los elementos.#
#Por ej: si cargan un 2 y un 4 significa que debemos crear una lista similar a: lista=[[1,1,1,1],[1,1,1,1]]#

lista=[]
elementos=int(input("cuantos elementos tendrá la lista"))
sub=int(input("cuantos elementos tendrán las listas internas"))
for k in range(elementos):
    lista.append([])
    for x in range (sub):
        valor=int(input("Ingrese valor:"))
        lista[k].append(valor)
print(lista)
suma=0
for k in range (len(lista)):
    for x in range (len(lista)):
        suma=suma+lista[k][x]
print ("La suma de todos los elementos",suma)
