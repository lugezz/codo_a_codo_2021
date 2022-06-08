def funcion():
    print('antes')
    div = 10 / 2
    print('despues')
    return div

funcion()

def flaskFunction(algo=None):
    '''
        Se requiere en esta función pasar por parámetro un número
    '''
    if algo is None:
        raise ValueError("Error! Desde el raise")


def ingresarNatural(msg):
    while True:
        try:
            valorReal= float(input(msg))
            print(valorReal)
            valor= int(valorReal)
            print("Resultado:", valor)
            assert (valor == valorReal), "Error: debe ingresar un valor entero."
            assert (valor > 0), "Error: debe ingresar un valor positivo."
            break
        except AssertionError as error:
            print(error)
        except (ValueError):
            print("Error: ha ingresado un valor que no es numérico.")
        except:
            print("Error inesperado.")
        return valor


def ingresarPositivo(msj):
    err= True
    while err:
        try:
            num= float(input(msj))
            if num >= 0:
                err=False
            else:
                print("Error: debe ingresar un valor positivo o igual a 0.")
        except (ValueError):
            print("Error: ha ingresado un valor no numérico.")
        except:
            print("Error inesperado.")
        else:
            if not err:
                break
    return num

# ingresarPositivo("Ingrese un número positivo: ")

def main():
    # x = 5.5
    # y = 0
    # try:
    #     print(funcion(x, y))
    # except Exception as error:
    #     print(type(error).__name__)
    #     print("Algo salió mal")
    # print('listo')

    # print(help(flaskFunction))

    # try:
    #     e = flaskFunction()
    # except Exception as e:
    #     print(e)

    ingresarNatural("Ingrese un número: ")


# main()

# from copy import copy

import this

# a = {"clave": 1}
# b = copy(a)

# print (a is b)
