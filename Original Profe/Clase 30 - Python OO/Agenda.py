class Agenda:
    # contactos = []

    def __init__(self):
        self.contactos = []

    def createContact(self, name, tel, email):
        contacto = {"name": name, "tel": tel, "email": email}
        self.contactos.append(contacto)

    def listContacts(self):
        print('Indice\tNombre\tTeléfono\tEmail')
        for index, contacto in enumerate(self.contactos):
            print(f'{index} - {contacto["name"]} - {contacto["tel"]} - {contacto["email"]}')

    def searchContact(self, search):
        for contacto in self.contactos:
            if contacto["name"].find(search) != -1:
                print(f'{contacto["name"]} - {contacto["tel"]} - {contacto["email"]}')

    def updateContact(self, pos):
        self.contactos[pos]["name"] = input("Ingrese nombre: ")
        self.contactos[pos]["tel"] = input("Ingrese nombre: ")
        self.contactos[pos]["email"] = input("Ingrese nombre: ")

def ProgramaAgenda():
    keyboard = 0
    agenda = Agenda()
    while keyboard != '5':
        print('1 - Añadir contacto')
        print('2 - Listar contacto')
        print('3 - Buscar contacto')
        print('4 - Editar contacto')
        print('5 - Cerrar agenda')

        keyboard = input('Ingrese una opción: ')
        if keyboard == '1':
            name = input('Ingrese nombre: ')
            tel = input('Ingrese teléfono: ')
            email = input('Ingrese email: ')
            agenda.createContact(name, tel, email)
        elif keyboard == '2':
            agenda.listContacts()
        elif keyboard == '3':
            search = input('Ingrese nombre a buscar: ')
            agenda.searchContact(search)
        elif keyboard == '4':
            pos = int(input('Ingrese posición del contacto a actualizar: '))
            agenda.updateContact(pos)
        elif keyboard == '5':
            pass
        else:
            print('Opción inválida')



ProgramaAgenda()