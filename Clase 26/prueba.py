""" print ('hola!')
nombre = input ('Ingrese su nombre\n')

print (f'Tu nombre es {nombre}') 

nombre = 'Juan'
print (len(nombre))
print (nombre.capitalize())

"""
def ejercicio1():
  print ('Hello World!')

ejercicio1()

def ejercicio2():
  print (f'El resultado de 3+5 es {3+5}')

ejercicio2()

def ejercicio3():
  nombre = input ('Ingresa tu nombre: ')
  print (f'Hola {nombre}')

#ejercicio3()

def ejercicio4():
  num1 = int(input ('Ingresa numero 1: '))
  num2 = int(input ('Ingresa numero 2: '))
  print (f'El resultado de la suma es {num1 + num2} ')


#ejercicio4()

def ejercicio5():
  num1 = int(input ('Ingresa numero 1: '))
  num2 = int(input ('Ingresa numero 2: '))
  res = max(num1, num2)

  print (f'El mayor numero es { res } ')

#ejercicio5()

def ejercicio6():
  num1 = int(input ('Ingresa numero 1: '))
  num2 = int(input ('Ingresa numero 2: '))
  num3 = int(input ('Ingresa numero 3: '))
  res = max(num1, num2, num3)


  print (f'El mayor numero es { res } ')

#ejercicio6()

def ejercicio7():
  num1 = int(input ('Ingresa numero a dividir por 2: '))
  res = "no es divisible"
  if num1 % 2 == 0:
    res = "es divisible"

  print (f'El número { num1 } { res } por 2')
  print (not bool(num1%2))
  print ('Es impar' if num1%2 else 'Es par')
  
ejercicio7()
