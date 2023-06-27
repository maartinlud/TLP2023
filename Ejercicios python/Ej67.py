lista = []
for x in range (5):
    valor=int (input("Ingrese valor:"))
    lista.append(valor)
menor=lista[0]
posmenor=lista[0]
for x in range (1,5):
    if lista[x]<menor:
        menor=lista[x]
        posmenor = x
posmenor1=posmenor+1
print ("menor de la lista")
print (menor)
print ("posicion del menor:")
print (posmenor1)