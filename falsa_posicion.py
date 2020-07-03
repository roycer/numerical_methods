from math import *

def f1(x):
    aux=cos(x)-x
    return aux
#=====================#
# a: limite inferior del intervalo
# b: limete superior  del intervalo
# fx: función a obtener la raiz
# nk: número de iteraciones    
# tol: tolerancia
# ERA: error relativo aproximado    

def falsa_posi(a,b,fx,nk,tol):
    print("iter","a"," ","b"," ", "xi"," ","f(ck)"," ", "E_RA")
    x0 = b
    for i in range(0,nk):
        xi = (a*fx(b) - b*fx(a))/(fx(b) - fx(a))
        ERA = 100*abs(xi - x0)/abs(xi) # error relativo aproximado
        print(i+1,round(a,6)," ",round(b,6)," ",round(xi,6)," ", 
              abs(round(fx(xi),7))," ",round(ERA,5))        
        if(fx(a)*fx(xi)<0):
            b=xi
        else: a=xi
        x0=xi
        if(ERA<tol):
            break
    aux = fx(xi)
    return(xi,aux)
#================================#
falsa_posi(0.5, pi/4, f1, 40, 0.0001)         
#================================#    
          
