from math import *
#import math as m
#import numpy as np
from prettytable import PrettyTable
from decimal import *

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
        return integral
    else:

     for k in range(0, n-1):
        nvh = nvh +1
        eval_x=lim_inf+nvh*h
        fxeval=evaluarFuncion(ecuacion,eval_x)
        sfx = sfx+fxeval
     integral = (h/2)*(fxa+2*sfx+fxb)

     return integral



def mromberg(ecuacion, lim_inf, lim_sup, puntos ):
    
    Ii = []
    Ijk =[]

   # tabla = PrettyTable(["J", "N", "I: Trapecio"])
   # tabla.title = "METODO DE INTEGRACION DE ROMBERG "
    n = 1
    for i in range (1, puntos+1):
        
        I1 = round(mTrapecio(ecuacion, lim_inf, lim_sup, n ), 8)
        Ii.append(I1)
        #tabla.add_row([i, n, "{0:.8f}".format(I1)])
        n = n*2
   # print(tabla)

    Ii1 = Ii
    dec = 0
    ji=0
    Error = []
    p = puntos
    conte = 0
    cont = puntos
    contac = puntos-1
    for k in range (2, puntos+1):

        for j in range (1,puntos-dec):
            ji = ji+1
            
            IJK = round(((4**(k - 1))*Ii1[ji]-Ii1[ji-1])/((4**(k - 1))-1), 8)
            
            
            Ii1.append(IJK)
            #print(ji)
        #print()
        dec = dec+1
        Err = abs(((Ii1[p]-Ii1[conte])/Ii1[conte]))*100
        Error.append(Err)
        p = p + contac
        conte = conte + cont
        cont = cont-1
        contac = contac-1
        ji = ji + 1

    error = Error
    Ijk = Ii1

   # Error = abs(((Ijk[-3]-Ijk[-6])/Ijk[-6]))*100

    # Arreglo de datos
    datos = Ijk

    # Crear una instancia de PrettyTable
   
    tabla = PrettyTable()
    tabla.title = "METODO DE INTEGRACION DE ROMBERG"
    # Número inicial de elementos a tomar para la primera columna
    n = puntos

    # Crear las columnas y agregar filas
    while datos:
        columna = datos[:n]  # Tomar los primeros n elementos del arreglo
        datos = datos[n:]  # Quitar los elementos ya tomados del arreglo principal

        # Asegurar que todas las filas tengan la misma longitud
        if len(columna) < len(tabla._rows):  # Comparar con la cantidad actual de filas en la tabla
            columna += [''] * (len(tabla._rows) - len(columna))

        tabla.add_column(f"K {len(tabla.field_names) + 1} ({n} elementos)", columna)

        # Disminuir el número de elementos para la siguiente columna
        n -= 1

    # Imprimir la tabla
    print(tabla)

    # Imprimir los errores
    for k in range(2, puntos+1):
         
            print(f'  Error de K{k} = ',round(error[k-2],4),"%")


        
        
        







    
        
            
      
         
        


    

""" x0 = 0
x1 = 1
ecuacion = 'sin(pi*x)'
puntos = 4

mRomberg(ecuacion, x0, x1, puntos) """


""" x0 = -1
x1 = 1
ecuacion = '(1/(2*pi)**0.5)*(exp((-x**2)/2))'
puntos = 5
mRomberg(ecuacion, x0, x1, puntos) """

""" x0 = 0
x1 = 1
ecuacion = '(x**0.1)*(1.2-x)*(1-exp(20*(x-1)))'
puntos = 12
mRomberg(ecuacion, x0, x1, puntos) """
