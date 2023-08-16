paises=[]
habitantes=[]
for x in range (5):
    nom=input("Ingrese el nombre del pais: ")
    paises.append(nom)
    no=int(input("Ingrese la cantidad de habitantes:"))
    habitantes.append(no)
for k in range (4):
        for x in range (4-k):
            if (paises[x]>paises[x+1]):
                aux1 = paises[x]
                paises[x]=paises[x+1]
                paises[x+1]=aux1
                aux2=paises[x]
                paises[x]=paises[x+1]
                paises[x]=aux2
print("lista de paises y sus habitantes respectivas alfabeticamente")
for x in range (5):
        print(paises[x],habitantes[x])  

for k in range (4):
        for x in range (4-k):
            if (habitantes[x]<habitantes[x+1]):
                aux1 = habitantes[x]
                habitantes[x]=habitantes[x+1]
                habitantes[x+1]=aux1
                aux2=habitantes[x]
                habitantes[x]=habitantes[x+1]
                habitantes[x]=aux2
print("lista de paises y sus habitantes respectivas por cantidades habitantes")
for x in range (5):
        print(habitantes[x],paises[x]) 