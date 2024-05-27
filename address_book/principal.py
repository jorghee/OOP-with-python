from agenda.contacto import Contacto
from agenda.agenda import Agenda

#Consideraciones sobre la implementacion: 
# __name__ es una variable que se crea en todos los modulos de Python, el valor de esta variable es "__main__" si el modulo se esta ejecutando como un programa principal con "python nombre_modulo.py" o el nombre del modulo si se esta importando

class Principal:

  def __init__(self):
    self._agenda = Agenda("./data/data.json")

  def menu(self):

    print("Welcome to address book! Enter 'finish' to finish the list\n")

    print("""
    ---------------------------------------------------------------------
    |   1. search -> search by name                                     |
    ---------------------------------------------------------------------
    """)

    while True:
      option = input("\n$ ")

      if option == "search":
        search = input("Enter the name: ")
        contact = self._agenda.getContact(search)
        print(contact)

if __name__ == "__main__":
    principal = Principal()
    principal.menu()
