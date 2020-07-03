from math import *

# funcion del ejemplo
def f1(x):
    aux=cos(x)-x
    return aux

# metodo de la secante
# x0=x_(0)
# x1=x_(1)
# tol: tolerancia en porcentaje
# Nmax: número de iteraciones
def secante(x0,x1,Nmax,tol,fx):
    ERA = 100
    iter = 1
    print("iter", " ", "xk", " ", "fx(xk)", " ", "EA", " ", "ERA" )
    while(ERA>tol):
        # xk: genera la raiz
        xk = x1 - (fx(x1)*(x1 - x0))/(fx(x1)-fx(x0))
        iter = iter + 1
        EA = abs(xk-x1)
        ERA = abs((xk-x1)/xk)*100
        x0 = x1
        x1 = xk
        if(iter > Nmax):
            return
        print(iter," ",round(xk,7)," ",round(fx(xk),9)," ",
              round(EA,8), " ", round(ERA,8) )
    aux = abs(fx(xk))
    return(xk,aux)   
#------------------------------#
#%%        
secante(0.5,pi/4,80,0.0001,f1)

