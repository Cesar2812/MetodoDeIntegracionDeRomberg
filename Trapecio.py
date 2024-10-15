from math import *

def evaluarFuncion(expr, val):
    x = val
    y = eval(expr)
    return y


def mTrapecio(ecuacion, lim_inf, lim_sup, n):
    h = (lim_sup-lim_inf)/n
    fxa=evaluarFuncion(ecuacion,lim_inf)
    fxb=evaluarFuncion(ecuacion,lim_sup)
    sfx = 0
    nvh = 0
    if(lim_inf+h == lim_sup):

        integral = (h/2)*(fxa+fxb)
        print(f'\n      METODO DE TRAPECIO\n')
        print(f'  Nro. de fracciones = {n}\n')
        print(f'        I = {"{0:.7f}".format(integral)}')
    else:

     for k in range(1, n-1):
        nvh = nvh +1
        eval_x=lim_inf+nvh*h
        fxeval=evaluarFuncion(ecuacion,eval_x)
        sfx = sfx+fxeval
     integral = (h/2)*(fxa+2*sfx+fxb)
     print(f'\n      METODO DE TRAPECIO\n')
     print(f'  Nro. de fracciones = {n}\n')
     print(f'        I = {"{0:.7f}".format(integral)}')