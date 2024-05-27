#Consideraciones de POO en Python: 
# __init__ es el constructor de la clase, es el primer metodo que se ejecuta al crear un objeto de la clase
# self es una referencia al objeto que se esta creando
# __str__ es un metodo que se ejecuta cuando se quiere imprimir el objeto
class Contacto: 

  def __init__(self, nombre, telefono, direccion, relacion):
    self.nombre = nombre
    self.telefono = telefono
    self.direccion = direccion
    self.relacion = relacion

  def __str__(self):
    return f"Nombre: {self.nombre}, Telefono: {self.telefono}, Direccion: {self.direccion}, Relacion: {self.relacion}"

  def get_name(self):
    return self.nombre

  def get_phone(self):
    return self.telefono

  def get_adress(self):
    return self.direccion

  def get_relation(self):
    return self.relacion

  def set_name(self, name):
    self.nombre = name

  def set_phone(self, phone):
    self.telefono = phone

  def set_adress(self, adress):
    self.direccion = adress

  def set_relation(self, relation):
    self.relacion = relation
