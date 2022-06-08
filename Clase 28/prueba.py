'''
count = 0

for i in range(501):
    if i % 4 == 0:
        print(i, end=' ')
        print('(Es múltiplo de 4)')
    elif i % 9 == 0:
        print(i, end=' ')
        print('(Es múltiplo de 9)')
    else: print(i)
    count += 1
    if count == 5:
        print('------------------------------')
        count = 0



def ejercicio15():
  for i in range (1, 501):
'''

numeros = [1,2,3,4,5]

print (numeros [-1])
print (numeros)
numeros.insert(3,10)
print (numeros)
numeros.insert(10,3)
print (numeros)
numeros.pop(4)
print (numeros)
#print (numeros.index(6)) da error
print (numeros.index(3))

numeros.sort()
print (numeros)

texto = "Argentina"
print (texto.lower())
print (texto.upper())
texto = texto.upper().capitalize() #Para boludear
print (texto)

conjunto = {'Palotes, Juan de', (1930, 11, 13), 3000936}
a = set(conjunto)
print(a)
[print (elem) for elem in a]
print(a)
