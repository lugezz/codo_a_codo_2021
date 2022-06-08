
# Dado -------------------

class Cliente:
    def __init__(self,nombre):
        self.nombre=nombre
        self.monto=0

    def depositar(self,monto):
        self.monto=self.monto+monto
    def extraer(self,monto):
        self.monto=self.monto-monto
    def retornar_monto(self):
        return self.monto
    def imprimir(self):
        print("{} tiene depositada la suma de {}".format(self.nombre,self.monto))

# Dado -------------------
class Dado:
    def tirar(self):
        self.valor=random.randint(1,6)
    def imprimir(self):
        print("Valor del dado: {}".format(self.valor))
    def retornar_valor(self):
        return self.valor

class JuegoDeDados:
    def __init__(self):
        self.dado1=Dado()
        self.dado2=Dado()
        self.dado3=Dado()
    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()

        if self.dado1.retornar_valor()==self.dado2.retornar_valor() and self.dado1.retornar_valor()==self.dado3.retornar_valor():
            print("Ganó")
        else:
            print("Perdió")


# Persona - Variable de clase ----------
class Persona:
    variable=20

    def __init__(self, nombre):
        self.nombre=nombre

# Bloque principal
persona1=Persona("Juan")
persona2=Persona("Ana")
persona3=Persona("Luis")
print(persona1.nombre) # Juan
print(persona2.nombre) # Ana
print(persona3.nombre) # Luis
print(persona1.variable) # 20
Persona.variable=5
print(persona2.variable) # 5

# Perro ---
class Perro:
    # Atributo de Clase
    genero= "Canis"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    # Método de instancia
    def imprimir(self):
        return f'{self.nombre} tiene {self.edad} años.'
        # Otro método de instancia
    def ladrar(self, sonido):
        return f'{self.nombre} dice {sonido}.'

# Cliente - Variable de Clase -------------------------------
class Cliente:
    suspendidos=[] #Variable de Clase
    def __init__(self,codigo,nombre):
        self.codigo=codigo #Variable de Instancia
        self.nombre=nombre #Variable de Instancia


    def imprimir(self):
        print("Codigo: {}".format(self.codigo))
        print("Nombre: {}".format(self.nombre))
        self.esta_suspendido()
    
    def suspender(self):
        Cliente.suspendidos.append(self.codigo)

    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta suspendido")
        else:
            print("No esta suspendido")
            print("_____________________________")


cliente1=Cliente(1,"Juan")
cliente2=Cliente(2,"Ana")
cliente3=Cliente(3,"Diego")
cliente4=Cliente(4,"Pedro")
cliente3.suspender()
cliente4.suspender()

