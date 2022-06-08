'''
1) Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe.
2) Desarrollar una función que reciba tres números enteros positivos y verifique si corresponden a una fecha válida (día, mes, año). Devolver True o False según la fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de la función.
3) Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos números enteros, correspondientes al total de la compra y al dinero recibido. Informar cuántos billetes de cada denominación deben ser entregados al cliente como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: si la compra es de $317 y se abona con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1.
4) Escribir dos funciones separadas para imprimir por pantalla los siguientes patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:
5) Crear una función lambda que devuelva el cuadrado de un valor recibido cómo parámetro. Desarrollar además un programa para verificar el comportamiento de la función.
6) Crear una función lambda para comprobar si un número es par o impar. Desarrollar además un programa para verificar el comportamiento de la función.
7) Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista.
8) Eliminar de una lista de palabras que se encuentren en una segunda lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.
9) Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada en forma ascendente o False en caso contrario. Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar además un programa para verificar el comportamiento de la función.
10) Desarrollar una función que determine si una cadena de caracteres es capicúa, sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita verificar su funcionamiento.
11) Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la misma tiene 80 columnas.
12) Escribir una función que reciba como parámetro una tupla conteniendo una fecha (día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada en formato extendido. Por ejemplo, para (12, 10,17) devuelve “12 de Octubre de 2017”. Escribir también un programa para verificar su comportamiento.
13) Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras ordenadas según su longitud.
14) Desarrollar una función eliminar_claves() que reciba como parámetros un diccionario y una lista de claves. La función debe eliminar del diccionario todas las claves contenidas en la lista, devolviendo el diccionario modificado y un valor de verdad que indique si la operación fue exitosa. Desarrollar también un programa para verificar su comportamiento.
15) Escribir una función para eliminar una subcadena de una cadena de caracteres, a partir de una posición y cantidad de caracteres dados, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma. Escribir una función utilizando rebanadas.
'''

#Ejercicio 1 --------------------------------------------------------
def ejercicio1 ():
  res = [-1, "Máximo no encontrado"]
  nume = []

  for i in range (3):
    valor = int(input(f'Ingrese el valor {i+1}: '))
    nume.append(valor)
  
  if nume.count(max(nume))== 1:
    res = [max(nume), f'El valor máximo es {max(nume)}' ]

  return res

#print(ejercicio1())
  
#Ejercicio 2 --------------------------------------------------------
import datetime

def ejercicio2(dia, mes, anio):
  res = True
  try:
    x = datetime.date(anio, mes, dia)
  except:
    res = False
  
  return res

#print (ejercicio2(9,11,2021))
#print (ejercicio2(9,13,2021))

#Ejercicio 2b --------------------------------------------------------
def ejercicio2b(dia, mes, anio):
  if dia < 1 or mes < 1 or anio < 1800:
    return False

  if mes == 2:
    #bisiesto te la debo :)
    dia += 3
  elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dia +=1
  
  if dia > 31 or mes > 12 or anio > 2100:
    return False
  
  return True

#print (ejercicio2b(9,11,2021))
#print (ejercicio2b(9,13,2021))
#print (ejercicio2b(-1,11,2021))
#print (ejercicio2b(31,6,2021))

#Ejercicio 3 --------------------------------------------------------
def ejercicio3 (total, pagado):
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
        pdo -=bille
        break

  return (resultado)

#print (ejercicio3(150, 1500))
#print (ejercicio3(1810, 2000))
#print (ejercicio3(1810, 3000))

#Ejercicio 4 --------------------------------------------------------
def printAst (caracteres):
  for i in range (5):
    print ("*"*caracteres)

def printAstIncr (caracteres):
  for i in range (5):
    print ("*"*(caracteres + i))

#printAst(3)
#printAstIncr(2)

#Ejercicio 5 --------------------------------------------------------
funcioncilla = lambda x : x ** 2

#print(funcioncilla (5))
#print(funcioncilla (25))

#Ejercicio 6 --------------------------------------------------------
esPar = lambda x : x%2 == 0

#print (esPar(3))
#print (esPar(4))

#Ejercicio 7 --------------------------------------------------------
def ejercicio7 ():
  cuad = []
  num1 = int(input ('Ingrese el valor para buscar los cuadrados hasta este: '))

  for i in range (1, num1+1):
    cuad.append (i ** 2)

  return cuad [-10:]

#print(ejercicio7 ())

#Ejercicio 8 --------------------------------------------------------
def eliminadorListas (listaOrig, listaBorra):
  listaABorrar = []
  listaFinal = listaOrig # Me lo borra también en listaOrig

  for item in listaBorra:
    if listaOrig.count(item)>0:
      listaABorrar.append(item)
      listaFinal.remove(item)
  
  print (f'La lista era {listaOrig+listaABorrar} \nSe borraron los siguientes items {listaABorrar}\n Al final queda {listaFinal} ')

lista1 = ["River", "Boca", "Talleres", "Godoy Cruz", "Velez", "San Lorenzo", "Independiente", "Racing"]
lista2 = ["River", "Godoy Cruz", "San Lorenzo", "Independiente", "Victoriano Arenas"]

#eliminadorListas(lista1, lista2)

#Ejercicio 9 --------------------------------------------------------
def ejercicio9(lista):
  if lista == sorted(lista):
    res = True
  elif lista == sorted(lista, reverse=True):
    res = False
  else:
    print ("No tiene ningún orden")
    res = "Nini"

  return res

#print (ejercicio9([1, 2, 3]))
#print (ejercicio9([10, 5, 3]))
#print (ejercicio9([10, 2, 3]))

#Ejercicio 10 --------------------------------------------------------
def esCapicuaz(nombre):
  resp = False

  for letra in range (len(nombre)):
    if nombre[letra] == nombre [-(letra+1)]:
      resp = True
      print (nombre[letra],"--", nombre[-(letra+1)], resp)
    else:
      resp = False
      print (nombre[letra],"--", nombre[-(letra+1)], resp)

  return resp
  

print(esCapicuaz ("anana"))
print ("-"*40)
print (esCapicuaz("codon"))

#Ejercicio 11 --------------------------------------------------------
def imprimir_centrado(cadena):
  if len (cadena)>= 80:
    return cadena
  else:
    margen = " " * int((80 - len (cadena))/2)
    return margen + cadena + margen


print (len(imprimir_centrado("Cara e cui")))
print (imprimir_centrado("Cara e cui"))

print (len(imprimir_centrado("kasdjkasjkasdj ñañaññañañ kdkl klfklasfdlkasdfkls asadklfklfsadklfdasklasfd fdfasjkfasklfasd")))
print (imprimir_centrado("kasdjkasjkasdj ñañasññañasña kdkl klfklasfdlkasdfkls asadklfklfsadklfdasklasfd fdfasjkfasklfasd"))

#Ejercicio 12 --------------------------------------------------------
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

def fecha_larga (fecha):
  return str(fecha[0])+" de " + meses [fecha[1]-1]+" de 20"+ str(fecha[2])

print (fecha_larga((12, 10, 17)))
print (fecha_larga((15, 11, 21)))

#Ejercicio 13 --------------------------------------------------------
def orden_x_longi(frase):
  palabras = frase.split(" ")
  palabras = list(dict.fromkeys(palabras))
  palabras = sorted(palabras, key=len)

  return palabras

frase = "estoy estudiando en codo a codo con clases geniales y estoy renegando con este ejercicio"

print(orden_x_longi(frase))

#Ejercicio 14 --------------------------------------------------------
def eliminar_claves(diccionario, lista_claves):
  diccio = diccionario

  for k, v in list(diccio.items()): # Le pongo list para que no de error de que ha cambiado el dict en la iteración
    if k in lista_claves:
      del diccio[k]
  
  return diccio

dic = {"Club": 'Talleres', 'Años': 100, 'Campeonatos': 2, 'Hinchas': 100000000 }
lista1 = ["Años", "Hinchas", "Cachula"]

print (eliminar_claves(dic, lista1))

#Ejercicio 15 --------------------------------------------------------
def achicar_list (lista, borra_desde, borra_largo):

  for i in range (borra_desde + borra_largo, borra_desde, -1): #Inverso porque sino van cambiando los índices a borrar
    lista.pop(i-1) 

  return lista

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
print (achicar_list(meses, 2, 5))