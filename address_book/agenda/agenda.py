import os;
import json;
from .contacto import Contacto

class Agenda:
  def __init__(self, path_data):
    self._contacts = self.recuperar_agenda(path_data)
    print(self._contacts)

  def recuperar_agenda(self, path_data):
    if not (os.path.exists(path_data)):
      return []

    with open(path_data, "r") as data: 
      datos = json.load(data)
    return [Contacto.parsear(dic) for dic in datos]


  def __repr__(self) -> str: 
    return self.__str__()

  def __str__(self) -> str:
    return '\n'.join([str(contact) for contact in self._contacts])
  
  def getContact(self, search):
    for contact in self._contacts:
        name = contact.nombre
        isName = self._match(name.lower(), search.lower())
        if isName:
          return "No encontrado\n"
        else:
          return contact

  def _match(self, name, search):
    lenS = len(search)
    lenN = len(name)
    j = 0

    for i in range(lenN - lenS):
      if j < lenS and name[i] == search[j]: 
        j += 1
      elif j == lenS - 1:
        return True
    return False

