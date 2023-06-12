nota=0
notamayor=0
notamenor=0
for x in range (10):
    nota= int (input ("Ingrese nota: "))
    if nota>=7:
        notamayor=notamayor+1
    else:
            notamenor=notamenor+1
print("las notas mayor a 7 son: ",notamayor)
print("las notas menor a 7 son: ",notamenor)

