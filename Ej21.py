cantp= int (input ("Ingrese cantidad piezas: "))
x=0
b=0
while x<cantp:
    long= float (input ("Ingresar longitud de la pieza: "))
    x=x+1
    
    if long<1.30 and long>1.20:
        b=b+1
        
print ("las piezas aptas son: ",b)
