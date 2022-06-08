class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def catalogar(listaVeh):
        mostrar = 'Listado de objetos:\n'

        for veh in listaVeh:
            mostrar +=  f'* {type(veh).__name__.upper()}: '
            mostrar += f'Color: {veh.color}, Ruedas: {veh.ruedas}, '

            if type(veh).__name__ == "Coche" or type(veh).__name__ == "Motocicleta":
                mostrar += f'Velocidad: {veh.velocidad}, Cilindrada: {veh.cilindrada}'

            if type(veh).__name__ == "Camioneta":
                mostrar += f'Carga: {veh.carga}'

            if type(veh).__name__ == "Bicicleta":
                mostrar += f'Tipo: {veh.tipo}'

            mostrar += '\n'

        return mostrar

    def catalogar2(listaVeh, cantRu=0):
        mostrar = 'No has elegido cantidad de ruedas'
        ct = 0
        
        if cantRu>0:
            for veh in listaVeh:
                if veh.ruedas == cantRu:
                    ct += 1
            
            mostrar = 'Se han encontrado {} vehículos con {} ruedas'.format(ct, cantRu)

        return mostrar

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f'El coche es de color {self.color}, tiene {self.ruedas} ruedas y anda a {self.velocidad} kmxh.'

class Camioneta(Vehiculo):
    def __init__(self, color, ruedas, carga):
        super().__init__(color, ruedas)
        self.carga = carga


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

class Motocicleta(Coche):
    pass


c = Coche("Rojo", 4, 180, 1500)
cm = Camioneta("Azul", 4, 10000)
b = Bicicleta("Amarilla", 2, "Ciudad")
m = Motocicleta("Violeta", 2, 210, 4000)

vehiculos = [c, cm, b, m]

print(Vehiculo.catalogar(vehiculos))
print(Vehiculo.catalogar2(vehiculos))
print(Vehiculo.catalogar2(vehiculos,2))
print(Vehiculo.catalogar2(vehiculos,4))
