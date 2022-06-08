#Ejercicio 1

def _1():
  listArg = []
  for x in range(3):
    listArg.append(int(input (f'Ingrese número {x+1} a comparar: ')))
  res, msg = getMayorEstricto(*listArg)
  print(msg)

def getMayorEstricto(*argv):
  if len (argv)!= 3:
    return (-2, 'Solo se admiten 3 números')  
  maxNum = max(argv)
  if argv.count(maxNum) > 1:
    return (-1, 'No hay un mayor estricto')
  else:
    return (maxNum, f'El mayor es {maxNum} ')

_1()
#print(getMayorEstricto(1, 3, 3)[1])
#print(getMayorEstricto(1, 1, 3)[1])

x = lambda a,b: a * b

print(x(5, 6))