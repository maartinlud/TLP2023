lista1=0
lista2=0
x=0
b=0
while x<15:
    num1= int (input ("Ingresar numero de la lista 1: "))
    x=x+1
    lista1=lista1+num1
print ("                  ")
while b<15:
    num2= int (input ("Ingresar numero de la lista 2: "))
    b=b+1
    lista2=lista2+num2

if lista1 > lista2:
    print("la lista 1 es mayor")
else:
        print("la lista 2 es mayor")
