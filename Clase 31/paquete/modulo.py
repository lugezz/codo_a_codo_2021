def hola(nombre):
    print ('Hola', nombre)

def adios(nombre):
    print ('Adios',nombre)

def programaPrincipal():
    hola("Juan")

if __name__ == '__main__':
    programaPrincipal()
else:
    print (__name__)