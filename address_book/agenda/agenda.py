import os;
import json;
from .contacto import Contacto

class Agenda:
  def __init__(self, path_data):
    self._contacts = self.recuperar_agenda(path_data)

  def recuperar_agenda(self, path_data):
    if not (os.path.exists(path_data)):
      return []

    with open(path_data, "r") as data: 
      datos = json.load(data)
      print("Recuperación exitosa...\n")
    return [Contacto.parsear_de_json(dic) for dic in datos]

  def guardar_agenda(self):
    contacts_pars = [contact.parsear_a_json() for contact in self._contacts]
    with open("./data/data.json", "w", encoding = "utf-8") as save:
      json.dump(contacts_pars, save, ensure_ascii=False, indent=2)
      print("Guardacion exitosa...\n")

  def getContact(self, pattern):
    for contact in self._contacts:
        name = contact.nombre
        isName = self._match(name.lower(), pattern.lower())
        if isName:
          return contact
    return "No encontrado\n"

  def insertContact(self, newContact):
    for saved in self._contacts:
      if saved.nombre == newContact.nombre:
        saved = newContact
        print("El contacto se sobreescribió exitosamente...\n")
        return

    self._contacts.append(newContact)
    print("El contacto se guardó exitosamente...\n")

  def  updateContact(self, pattern, newContact):
    for contact in self._contacts:
      name = contact.nombre
      isName = self._match(name.lower(), pattern.lower())
      if isName:
        contact = newContact
        print("El contacto se modificó exitosamente...\n")
        return
    print("No se encontró el contacto a modificar...\n")
    
  def deleteContact(self, pattern):
    for contact in self._contacts:
      name = contact.nombre
      isName = self._match(name.lower(), pattern.lower())
      if isName:
        self._contacts.remove(contact)
        print("El contacto se eliminó exitosamente...\n")
        return
    print("No se encontró el contacto a eliminar...\n")

  def listAgenda(self):
    for contact in self._contacts:
      print(contact)

  def __repr__(self) -> str:
    return self.__str__()

  def __str__(self) -> str:
    return '\n'.join([str(contact) for contact in self._contacts])

  # Algoritmo Knuth-Morris-Pratt (KMP)
  def _match(self, name, pattern):
    lps = self._compute_lps(pattern)
    i = 0
    j = 0

    while i < len(name):
      if pattern[j] == name[i]:
        i += 1
        j += 1

      if j == len(pattern):
        j = lps[j - 1]
        return True
      elif i < len(name) and pattern[j] != name[i]:
        if j != 0:
          j = lps[j - 1]
        else:
          i += 1
    return False

  # Generación de la funcion π
  def _compute_lps(self, pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
      if pattern[i] == pattern[length]:
        length += 1
        lps[i] = length
        i += 1
      else:
        if length != 0:
          length = lps[length - 1]
        else:
          lps[i] = 0
          i += 1
    return lps
