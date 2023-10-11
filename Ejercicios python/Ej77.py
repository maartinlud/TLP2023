#Hacer el mismo ejercicio pero en vez de multiplicar y de sumar finalmente dividir la multiplicación de todos#
#los elementos con la suma de elementos#

lista1=[]
elementos=int(input("cuantos elementos tendrá la lista de suma"))
sub=int(input("cuantos elementos tendrán las listas internas"))
for k in range(elementos):
    lista1.append([])
    for x in range (sub):
        valor=int(input("Ingrese valor:"))
        lista1[k].append(valor)
print(lista1)
suma=0
for k in range (len(lista1)):
    for x in range (len(lista1)):
        suma=suma+lista1[k][x]
print ("La suma de todos los elementos",suma)

lista=[]
elementos=int(input("cuantos elementos tendrá la lista de multiplicación"))
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

div=mult/suma
print ("la división entre la multiplicación",mult," y la suma ",suma,"es ",div)
