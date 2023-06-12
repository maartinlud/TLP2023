empleados=int(input("Ingrese la cantidad de empleados: "))
x=0
sueldo_dentro=0
sueldo_mayor=0
while x<empleados:
    sueldo= int (input ("Ingresar sueldo: "))
    x=x+1
    if sueldo>=100 and sueldo<=300:
        sueldo_dentro=sueldo_dentro+1
    if sueldo>300:
        sueldo_mayor=sueldo_mayor+1
    
        
print ("Los sueldos entre 200 y 300 son: ",sueldo_dentro)
print ("Los sueldos mayores a 300 son: ",sueldo_mayor)

