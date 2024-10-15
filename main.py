import IntegracionRomberg
import Trapecio


def datos():
    print("La ecuacion debe estar en funcion de (x)")
    ecuacion = input("  Ecuacion a evaluar: ")
    x0 = float(input("  Limite inferior: "))
    x1 = float(input("  Limite superior: "))
    return ecuacion, x0, x1


def metodo(opcion):
    if opcion == 1:

        ecuacion, x0, x1 = datos()
        n = int(input("Numero de J o K: "))
        IntegracionRomberg.mromberg(ecuacion, x0, x1, n)

    elif opcion ==2:
        ecuacion, x0, x1 = datos()
        n = int(input("Numero de n "))
        Trapecio.mTrapecio(ecuacion, x0, x1, n)

    else:
        print("Opcion incorrecta, vuelva a seleccionar otra opcion")


if __name__ == '__main__':
    ejecutar = True

    while(ejecutar):
        # print(" \n- - - Ecuaciones no lineales - - -")
        opcion = int(input('''
        - - - integracion Numerica - - -\n
        Elegir metodo:\n         
            [1] Integracion de Romberg
            [2] Trapecio
            [5] Salir\n
        Opcion: '''))
        if opcion == 5:
            ejecutar = False
        else:
            metodo(opcion)
            ejecutar = False
