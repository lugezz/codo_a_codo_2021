def ejercicio1():
    print("Hello World")
# ejercicio1()

def ejercicio2():
    print(f'El resultado de 3 + 5 es: {3 + 5}')
# ejercicio2()

def ejercicio3():
    nombreUsuario = input('Ingrese nombre: ')
    print(f'Hola {nombreUsuario}')
# ejercicio3()

def ejercicio4():
    num1 = int(input('Ingrese número 1: '))
    num2 = int(input('Ingrese número 2: '))
    print(num1 + num2)
# ejercicio4()

def ejercicio5():
    num1 = int(input('Ingrese número 1: '))
    num2 = int(input('Ingrese número 2: '))
    mayor = max(num1, num2)
    # mayor = num1 if num1 > num2 else num2
    print(mayor)
# ejercicio5()

def ejercicio6():
    num1 = int(input('Ingrese número 1: '))
    num2 = int(input('Ingrese número 2: '))
    num3 = int(input('Ingrese número 3: '))
    mayor = max(num1, num2, num3)
    print(mayor)
# ejercicio6()

def ejercicio7():
    num = int(input('Ingrese número: '))
    # print(not(bool(num % 2)))
    # print('Es impar' if num % 2 else 'Es par')
    print('Es par' if num % 2 == 0 else 'Es impar')
# ejercicio7()

def ejercicio8():
    num = int(input('Ingrese número: '))
    if num % 2 == 0:
        print("El número es divisible por 2.")
    elif num % 3 == 0:
        print("El número es divisible por 3.")
    elif num % 5 == 0:
        print("El número es divisible por 5.")
    elif num % 7 == 0:
        print("El número es divisible por 7.")
    else:
        print("El número no es divisible por 2, 3, 5 ni 7.")

# ejercicio8()

def ejercicio9_conIf():
    num = int(input('Ingrese número: '))
    esDivisible = False
    if num % 2 == 0:
        print("El número es divisible por 2.")
        esDivisible = True
    if num % 3 == 0:
        print("El número es divisible por 3.")
        esDivisible = True
    if num % 5 == 0:
        print("El número es divisible por 5.")
        esDivisible = True
    if num % 7 == 0:
        print("El número es divisible por 7.")
        esDivisible = True
    if not(esDivisible):
        print("El número no es divisible por 2, 3, 5 ni 7.")

# ejercicio9_conIf()

def ejercicio9_conFor():
    num = int(input('Ingrese número: '))
    esDivisible = False
    for i in (2, 3, 5, 7):
        if (num % i == 0):
            print("El número es divisible por ", i)
            esDivisible = True
    if not(esDivisible):
        print("El número no es divisible por 2, 3, 5 ni 7.")

# ejercicio9_conFor()


def ejercicio10():
    num = int(input('Ingrese número: '))
    print("El número es divisible por", num)
    for i in range(num - 1, 1, -1):
        if (num % i == 0):
            print("El número es divisible por", i)
    print("El número es divisible por 1")

# ejercicio10()


def ejercicio11_conFor():
    num = int(input('Ingrese número: '))
    esPrimo = True
    for i in range(num - 1, 1, -1):
        if (num % i == 0):
            esPrimo = False
    if esPrimo:
        print(f'El número {num} es primo')
    else:
        print(f'El número {num} no es primo')

# ejercicio11_conFor()

def ejercicio11_conWhile():
    num = int(input('Ingrese número: '))
    esPrimo = num > 1
    cont = num - 1
    while esPrimo and cont > 1:
        if (num % cont == 0):
            esPrimo = False
        else:
            cont -= 1
    print(f'El número {num} es primo' 
        if esPrimo else f'El número {num} no es primo')

# ejercicio11_conWhile()


def ejercicio13():
    # for i in range(31):
    #     for j in range(i):
    #         print(i, end='')
    #     print('')

    for i in range(31):
        if i < 10:
            print((('0' + str(i)) * i).center(60))
        else:    
            print((str(i) * i).center(60))

ejercicio13()