import random

class Persona:

    piernas = 2
    brazos = "2"

    def inicializar(self, nombre):
        self.nombre = nombre

    def imprimirNombre(self):
        print(self.nombre)


class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    
    def imprimir(self):
        print("Nombre: {}".format(self.nombre))
        print("Nota: {}".format(self.nota))

    def mostrar_estado(self):
        if self.nota>=4:
            print("Regular")
        else:
            print("Desaprobado")


class Perro:
    __genero = "Canis"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método de instancia
    def imprimir(self):
        return f'{self.nombre} tiene {self.edad} años.'
    # Otro método de instancia
    def ladrar(self, sonido):
        return f'{self.nombre} dice {sonido}.'

    def __str__(self):
        return f'{self.nombre} tiene {self.edad}'

    def __del__(self):
        pass
        # print(f'{self.nombre} ha dejado de existir.')

class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.imprimir()
    def __del__(self):
        print('Método delete llamado')
    def imprimir(self):
        print("Coordenada del punto: ({}:{})".format(self.x,self.y))
    def imprimir_cuadrante(self):
        if self.x>0 and self.y>0: print("Primer cuadrante")
        elif self.x<0 and self.y>0: print("Segundo cuadrante")
        elif self.x<0 and self.y<0: print("Tercer cuadrante")
        else: print("Cuarto cuadrante")

class ListadoBebidas:
    def __init__(self):
        self.__bebida = 'Naranja'
        self.__bebidas_validas = ['Naranja', 'Manzana']

    @property
    def bebida(self):
        return "La bebida oficial es: {}".format(self.__bebida)

    @bebida.setter
    def bebida(self, bebida):
        self.__bebida = bebida

bebidas= ListadoBebidas()
print(bebidas.bebida)
bebidas.bebida = 'Limonada'
print(bebidas.bebida)

# Bloque principal
# punto1=Punto(10,1)
# punto1.imprimir_cuadrante()


# perro1 = Perro("Firu", 5)
# print(perro1.genero)
# perro1.genero = "Can"
# perro2 = Perro("Tobi", 5)
# perro2.lalala = "lala"
# print(dir(perro2))
# print(perro1.edad)
# print(perro1.nombre)
# print(perro1.ladrar("guau"))

# perro1 = Perro("Tobi", 10)


# alumno1 = Alumno()
# alumno1.inicializar("Diego", 2)
# alumno1.imprimir()
# alumno1.mostrar_estado()

# alumno2=Alumno()
# alumno2.inicializar("Ana",10)
# alumno2.imprimir()
# alumno2.mostrar_estado()


# persona1 = Persona()
# persona1.inicializar("Juan")
# print(persona1.piernas)
# persona1.imprimirNombre()
# print(persona1.brazos)

# persona2 = Persona()
# persona2.inicializar("Fernando")
# print(persona2.piernas)
# persona2.imprimirNombre()
