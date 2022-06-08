def flaskFunction(algo=None):
    '''
        Se requiere en esta función pasar por parámetro un número
    '''
    if algo is None:
        raise ValueError("Error! Desde el raise")


def ingresarNatural(msg):
    while True:
        valor = 0
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

#ingresarNatural("Ingrese un número: ")

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

#ingresarPositivo("Ingrese un número positivo: ")

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

a = {"clave": 1}
b = a.copy()
c = a

print (f'B: {a is b}, C: {a is c}')

from collections import Counter

numeros = [1,2,3,4,1,2,3,1,2,1]
print(Counter(numeros)) #Counter({1: 4, 2: 3, 3: 2, 4: 1})

print(Counter("palabra")) #Counter({'a': 3, 'p': 1, 'l': 1, 'b': 1, 'r': 1})

coches= "mercedes ferrari bmw bmw ferrari bmw"
print(Counter(coches.split())) #Counter({'bmw': 3, 'ferrari': 2, 'mercedes': 1})

animales= "perro gato jirafa jirafa gato jirafa"
a= Counter(animales.split())
print(a.most_common(1)) #Elemento más repetido
print(a.most_common(2)) #Las dos palabras más repetidas
print(a.most_common()) #Ordenado por número de repeticiones
