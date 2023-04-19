numeros=int(input("Ingrese la cantidad de numeros: "))
x=0
numero_par=0
numero_impar=0
while x<numeros:
    numero= int (input ("Ingresar numero: "))
    x=x+1
    if numero % 2 == 0:
        numero_par=numero_par+1
    else:
        numero_impar=numero_impar+1
    
        
print ("Los numeros par son: ",numero_par)
print ("Los numeros impar son: ",numero_impar)
