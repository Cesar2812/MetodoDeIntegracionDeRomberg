#Calculo de la integral log(x)/x^3 entre los limites a=1 y b=3

#importacion de numpy y scipy

import numpy as np
import math as m

from scipy import integrate

#definicion de la funcion a integrar

f= lambda x: np.tan(2*x-1)/np.log(x+2)

a=0.5
b=1

#calculo de la integral

integral = integrate.romberg(f,a,b,show=True)
print(f'        I = {"{0:.7f}".format(integral)}')

lm = m.log10(2)
ln = np.log(2)

print(lm)
print(ln)


