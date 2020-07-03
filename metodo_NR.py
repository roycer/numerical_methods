
from math import *

# funcion del ejemplo
def f1(x):
    aux=exp(-x)-x
    return aux
# derivada de la función fx(x)
def df1x(x):
    aux=-exp(-x)-1
    return aux
   
#------------------------------#
# metodo de N-R
# x0: raiz inicial
# Nmax: número de iteraciones máxima    
# tol: tolerancia
# fx: función a encontrar la raíz     
# dfx: derivada de la función fx    
# NOTA: la función evaluada en la raíz aproximada, fx(xk),
#       es mostrada en  valor absoluto
def newtonr(x0,imax,tol,fx,dfx):
    ERA = 100
    iter = 0
    print("iter", " ", "xk", " ", "fx(xk)", " ", "EA", " ", "ERA" )
    while(ERA>tol):
        xk = x0 - ( fx(x0)/dfx(x0) )
        iter= iter + 1
        EA = abs(xk-x0)
        ERA= 100*(EA/abs(xk))
        x0 = xk
        if(iter > imax):
            return
        print( iter," ",round(xk,7)," ",round(abs(fx(xk)),8)," ", round(EA,8), 
              " ", round(ERA,8) ) 
    aux = abs(fx(xk))
    return(xk,aux)        
      
#%%
# EJECUTAR EL PROGRAMA         
newtonr(0,80,0.0000001,f1,df1x)   
#%%
   
