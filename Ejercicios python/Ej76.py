#Hacer el mismo ejercicio pero en vez de sumar tendrán que multiplicar los elementos.#
lista=[]
elementos=int(input("cuantos elementos tendrá la lista"))
sub=int(input("cuantos elementos tendrán las listas internas"))
for k in range(elementos):
    lista.append([])
    for x in range (sub):
        valor=int(input("Ingrese valor:"))
        lista[k].append(valor)
print(lista)
mult=1
for k in range (len(lista)):
    for x in range (len(lista)):
        mult=mult*lista[k][x]
print ("La multiplicación de todos los elementos",mult)