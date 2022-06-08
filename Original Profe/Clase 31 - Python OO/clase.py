class Pet:
    totalPets = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Pet.totalPets += 1


    @classmethod
    def getTotalPets(cls):
        print(f"Hay un total de {cls.totalPets} mascotas")


    def show(self):
        return f'Soy {self.name} y tengo {self.age} años'

    def speak(self):
        print("No puedo hablar.")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        return super().show() + f". Mi color es {self.color}"

    def speak(self):
        print("Miau")


p1 = Pet("Z", 10)
c1 = Cat("A", 1, "Marrón")
c2 = Cat("B", 2, "Rojo")
c3 = Cat("C", 5, "Blanco")

print(c1.show())
p1.speak()
c2.speak()
c2.getTotalPets()
Pet.getTotalPets()











# import paquete.modulo as saludos

# saludos.hola("Juan")
# saludos.adios("Juan")

# hola("Mario")
# adios("Mario")

# class Punto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#        return (self.x + other.x, self.y + other.y)


# punto1 = Punto(1, 2)
# punto2 = Punto(3, 4)

# print(punto1 + punto2)