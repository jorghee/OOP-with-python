from agenda.contacto import Contacto
from agenda.agenda import Agenda

#Consideraciones sobre la implementacion: 
# __name__ es una variable que se crea en todos los modulos de Python, el valor de esta variable es "__main__" si el modulo se esta ejecutando como un programa principal con "python nombre_modulo.py" o el nombre del modulo si se esta importando

class Principal:

  def __init__(self):
    self._agenda = Agenda("./data/data.json")

  def menu(self):

    print("Welcome to address book!")
    print("""
    ---------------------------------------------------------------------
    |   1. search -> search by name                                     |
    |   6. save -> save the contacts                                    |
    |   7. exit -> exit the program                                     |
    ---------------------------------------------------------------------
    """)

    while True:
      option = input("agenda> ")
      option = option.split()

      if option[0] == "search":
        if len(option) == 2:
          contact = self._agenda.getContact(option[1])
          print(contact)
        else:
          print("Ingrese: search <nombre>\n")
      elif option[0] == "save":
        if len(option) == 1:
          self._agenda.guardar_agenda()
        else:
          print("Ingrese: save\n")
      elif option[0] == "exit":
        break
      else:
        print("Comando no encontrado\n")

if __name__ == "__main__":
    principal = Principal()
    principal.menu()
