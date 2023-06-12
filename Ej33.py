suma=0
multtres=0
multcinco=0
b=0
for x in range (10):
    nota= int (input ("Ingrese numero: "))
    if nota % 3 == 0:
        multtres=multtres+1
    else:
         if nota % 5 == 0:
            multcinco=multcinco+1
         else:
            b=0
print("los multiplos de 3 son: ",multtres)
print("los multiplos de 5 son: ",multcinco)

