import datetime

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

# _1()


# Ejercicio 2


def ejercicio2b(dia, mes, anio):
    if dia < 1 or mes < 1 or anio < 1800:
        return False

    if mes == 2:
        # bisiesto te la debo :)
        dia += 3
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dia += 1

    if dia > 31 or mes > 12 or anio > 2100:
        return False

    return True

# print(ejercicio2b(25, 10, 2021))


def ejercicio2(dia, mes, anio):
    res = True
    try:
        x = datetime.date(anio, mes, dia)
    except:
        res = False

    return res


def ejercicio3(total, pagado):
    if pagado < total:
        return {"Error": "No hay dinero suficiente"}

    if pagado == total:
        return {"Sin vuelto": "Pagado justísimo"}

    pdo = pagado
    tot = total
    resultado = {
        "Billete": "Cantidad",
        500: 0,
        100: 0,
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        1: 0
    }
    billetes = [500, 100, 50, 20, 10, 5, 1]

    while pdo > tot:
        for bille in billetes:
            if pdo - bille >= tot:
                resultado[bille] += 1
                pdo -= bille
                break

    return (resultado)


# print(ejercicio3(317, 500))


def getVuelto(total, recibido):
    vuelto = {1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0}
    diferencia = recibido - total

    if diferencia == 0:
        return {}
    if diferencia < 0:
        return -1

    cambioPosible = True
    while diferencia > 0 and cambioPosible:
        cambioPosible = False
        for key in vuelto:
            if (key <= diferencia):
                vuelto[key] += 1
                diferencia -= key
                cambioPosible = True

    return vuelto, diferencia


def _3():
    vuelto, diferencia = getVuelto(317, 500)
    if vuelto == -1:
        print('Dinero insuficiente')
    elif not(vuelto):
        print('El pago fue exacto')
    else:
        for billete, cantidad in vuelto.items():
            print(f'Entregar {cantidad} billetes de {billete}')
        if diferencia:
            print(f'Entregar ${diferencia} en monedas (o caramelos)')


_3()


def eliminadorListas(listaOrig: list, listaBorra):
    listaABorrar = []
    listaFinal = listaOrig.copy()  # Me lo borra también en listaOrig

    for item in listaBorra:
        if listaOrig.count(item) > 0:
            listaABorrar.append(item)
            listaFinal.remove(item)

    print(
        f'La lista era {listaOrig} \nSe borraron los siguientes items {listaABorrar}\n Al final queda {listaFinal} ')


lista1 = ["River", "Boca", "Talleres", "Godoy Cruz",
          "Velez", "San Lorenzo", "Independiente", "Racing"]
lista2 = ["River", "Godoy Cruz", "San Lorenzo",
          "Independiente", "Victoriano Arenas"]

# eliminadorListas(lista1, lista2)


def esPalindromo(frase):
    res = True
    cont = 0
    while res == True and cont < len(frase):
        posicionA = frase[cont]
        posicionB = frase[len(frase) - cont - 1]
        if posicionA != posicionB:
            res = False
        else:
            cont += 1
    return res


def esPalindromoFacil(frase):
    print(frase[::-1])
    return frase == frase[::-1]

# print(esPalindromo("neuquen"))
# print(esPalindromoFacil("neuquen"))
