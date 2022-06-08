# Ejercicio 1


def _1():
    listArg = []
    inputs = 10
    for x in range(inputs):
        listArg.append(int(input(f'Ingrese número {x + 1} a comparar: ')))
    res, msg = getMayorEstricto(*listArg)
    print(msg)

def getMayorEstricto(*argv):
    if len(argv) != 3:
        return (-1, 'Solo se admiten 3 números')
    for arg in argv:
        if arg < 0:
            return (-1, "Solo se admiten números positivos")
    maxNum = max(argv)
    if argv.count(maxNum) > 1:
        return (-1, "No hay mayor estricto")
    # if len(set(argv)) == 3:
    #     return (maxNum, f'El mayor es {maxNum}')
    else:
        return (maxNum, f'El mayor es {maxNum}')


_1()