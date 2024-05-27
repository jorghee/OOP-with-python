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
