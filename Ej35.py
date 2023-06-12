n= int (input("Ingrese la cantidad de pares de datos: "))
cant=0
for x in range (n):
    x= int (input("Ingrese la base: "))
    y= int (input("Ingrese la altura: "))
    a=x*y
    superficie=a/2
    print ("la medida de la base es: ", x)
    print ("la medida de la altura es: ", y)
    print ("la medida de la superficie es: ", superficie)
    print(" ")
    if  superficie>12:
        cant=cant+1

print("la cantidad de superficies mayores a 12 son: ",cant)
