print ("Datos de la primera persona:")
nombre1= input("Ingrese nombre.")
edad1= int(input("Ingrese la edad."))
altura1= float(input("Ingrese la altura."))
nombre2 = input("Ingrese nombre de la segunda persona: ")
edad2 = int(input("Ingrese la edad de la segunda persona: "))
altura2 = float(input("Ingrese la altura de la segunda persona: "))
if altura1 > altura2:
    print(nombre1)
else:
    print(nombre2)