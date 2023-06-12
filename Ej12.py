sueldo=int(input("ingrese el sueldo: "))
antiguedad=int(input("Ingrese la antiguedad: "))
if sueldo<500 and antiguedad>10:
    aumento=sueldo+sueldo*0.05
    print("su sueldo tiene un aumento del 20% y es de ", aumento)
if sueldo<500 and antiguedad<10:
    aumento=sueldo+sueldo*0.20
    print("su sueldo tiene un aumento del 20% y es de ", aumento)
if sueldo>500:
    aumento=sueldo+sueldo*0.20
    print("su sueldo no tiene un aumento y es de ", aumento)
