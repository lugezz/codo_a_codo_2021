# Herencia ------------------------------------------------------------

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas


class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'El auto es de color {self.color}, tiene {self.ruedas} ruedas y anda a {self.velocidad} kmxh.'

auto1 = Auto("rojo", 4, 188)

print (auto1)

# Main ------------------------------------------------------------
import paquete.modulo as saludos #Cuando yo lo importo se ejecuta, por eso hago lo de __main__

saludos.hola("Rocoo")
saludos.adios('Facebook')

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add (self, other):
        return self.x + self.y + other.x + other.y
    

punto1 = Punto(1,2)
punto2 = Punto(3,4)

#print (punto1.add(punto2))

# Caso Ejemplo --------------
class Pet:
    totalPets = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        #self.totalPets += 1 Si dejo así cada uno tiene un valor distinto y la variable de pet es siempre 0
        Pet.totalPets += 1

    def show(self):
        return f'Soy {self.name} y tengo {self.age} años'

    def speak(self):
        print ('No puedo hablar')

    @classmethod #Hace para identificarlo como método de clase
    def getTotalPets(cls): #cls es de clase, no sería obligatorio
        print (f'Hay un total de {cls.totalPets} mascotas ')

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def show(self):
        return super().show () + f". Mi color es {self.color} "

    def speak(self):
        print ("Miau!!")

c1 = Cat("Florcito", 2, "Blanco y gris")
c2 = Cat("Otro Gato", 12, "Gris")
c3 = Cat("Callejero", 1, "Negro")

print(c1.show())
print(c3.show())
c2.speak()

p1 = Pet ("ZZ", 14)
p1.speak()

print (c2.totalPets) # Da 1 siempre
print (p1.totalPets) # Da 1 siempre
print (Pet.totalPets) # Da 0 siempre, porque son variables diferentes. Nunca se modificó
# Al cambiar self.totalPets - a -> Pet.totalPets ya si cuenta las instancias.

p1.getTotalPets()
Pet.getTotalPets()