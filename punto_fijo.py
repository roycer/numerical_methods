from math import *

#función original
def fx(x):
    aux= x**2+x-2
    return aux
#función despejada
def gx(x):
    aux= sqrt(2-x)
    return aux
#=====================#
# Programa Punto Fijo    
# x0: punto inicial
# xk: punto medio
# gx: función a obtener la raiz
# tol: tolerancia
# ERA: error aproximado 
# nk: número máximo de iteraciones
#     
def puntofijo(fx,gx,x0,tol,nk):
    print("iter","x0"," ","xk"," ","ERA", " ", "f(xk)" )
    for i in range(1,nk):
        xk  = gx(x0)
        ERA = 100*abs(xk-x0)/abs(xk) # xk diferente de cero
        print(i, round(x0,6), " ",round(xk,6), " ", round(ERA,3)," ", round(abs(fx(xk)),5) )
        x0=xk # actualizando 
        if(ERA<tol):
            break
    aux = fx(xk) # función evaluada en la raíz aproximada
    return(xk,aux)
#================================#
puntofijo(fx,gx,-1,0.0001,30)
