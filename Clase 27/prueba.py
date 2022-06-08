def ejercicio8():
  num = int(input('Ingrese un numero para dividir: '))
  if num%2 == 0 or num%3 == 0 or num%5 == 0 or num%7 == 0:
    print ('El número es divisible por 2, 3, 5 ó 7')
  else:
    print ('El número NO es divisible por 2, 3, 5 ó 7')

#ejercicio8()

def ejercicio8b():
  num = int(input('Ingrese un numero para dividir: '))
  if num%2 == 0:
    print ('El número es divisible por 2')
  elif num%3 == 0:
    print ('El número es divisible por 3')
  elif num%5 == 0:
    print ('El número es divisible por 5')
  elif num%7 == 0:
    print ('El número es divisible por 7')
  else:
    print ('El número NO es divisible por 2, 3, 5 ó 7')

#ejercicio8b()
def ejercicio9():
  num = int(input('Ingrese un numero para dividir: '))
  res = ""

  if num%2 == 0:
    res += ('El número es divisible por 2')
  
  if num%3 == 0:
    res += ('El número es divisible por 3')
  
  if num%5 == 0:
    res += ('El número es divisible por 5')

  if num%7 == 0:
    res += ('El número es divisible por 7')

  if res == "":
    res= 'El número NO es divisible por 2, 3, 5 ó 7'

  print (res)
ejercicio9()