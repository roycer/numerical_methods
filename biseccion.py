from math import *

# funcion del ejemplo
def f1(x):
    if(x==1):
        return -5
    if(x==2):
        return 14
    aux=pow(x,3)+4*pow(x,2)-10

    return aux

   
def biseccion(a,b,tol,Nro,fx):
    FA = fx(a)

    i = 1

    while(i <= Nro):
        
        p = a + (b - a)/2
        FP = fx(p)
        print("a",i,": ",a," b",i,": ", b," p",i,": "," fP: ",FP)
        if(FP == 0 or ((b-a)/2 < tol) ):
            return print("Procedimiento terminado satisfactoriamente-> ", p)
        
        if(FP*FA > 0):
            a = p
            FA = FP
        else:
            b = p
         
    return print("(El metodo fracaso despues de Nr, iteraciones, N0 ", Nro , "Procedimiento terminado sin exito")       
      

biseccion(1,2,0.0000001,13,f1)