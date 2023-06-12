num=0
nummayor=0
n=int (input("Ingrese la cantidad de numeros que quiere que sean leidos: "))
for x in range (n):
    num= int (input ("Ingrese valor: "))
    if num>=1000:
        nummayor=nummayor+1
print("las entradas mayores a 1000 son: ",nummayor)
