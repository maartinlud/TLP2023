#Se desea saber la temperatura media trimestral de cuatro paises. Para ellos se tiene como dato las temperaturas medias
#mensuales de dichos paises.
#Se debe ingresar el nombre del pais y seguidamente las tres temperaturas medias mensuales.
#Seleccional las estructuras de datos adecuados para el alacentamiento de los datos en memoria.
#a) Cargar por teclado los nombres de los paises y las temperaturas medias mensuales. 
#b) Imprimir los nombres de los apiese y las temperaturas medias mensules de las mismas.
#c) Calcular la temperatura media trismestral de cada pais. 
#d) Imprimir los nombres de los paises y las temperaturas medias trimestarales
#e) Imprimir el nombre del pais con la temperatura media trismestral mayor

paises=[]
temperaturas=[]
promediotemp=[]
for x in range (4):
    nom=input("ingrese el nombre del país: ")
    paises.append(nom)
    temp1=int(input("ingrese primer temperatura"))
    temp2=int(input("ingrese SEGUNDA temperatura"))
    temp3=int(input("ingrese tercera temperatura"))
    temperaturas.append([temp1,temp2,temp3])
print("Paises y temperaturas medias de los últimos tres meses mensuales")
for x in range(4):
    print(paises[x],temperaturas[x][0],temperaturas[x][1],temperaturas[x][2])
for x in range(4):
    pro=(temperaturas[x][0],temperaturas[x][1],temperaturas[x][2])//3
    promediotemp.append(pro)
print("paises y temperaturas medias")
for x in range (4):
    print(paises[x],promediotemp[x])
posmayor=0
for x in range (4):
    if (promediotemp[x]>promediotemp[mayor]):
        posmayor=x
print("Pais con temperatura media trimestral mayor"),paises[posmayor]
