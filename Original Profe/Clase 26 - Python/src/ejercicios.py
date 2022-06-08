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