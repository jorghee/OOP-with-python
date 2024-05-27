from agenda.contacto import Contacto

#Consideraciones sobre la implementacion: 
# __name__ es una variable que se crea en todos los modulos de Python, el valor de esta variable es "__main__" si el modulo se esta ejecutando como un programa principal con "python nombre_modulo.py" o el nombre del modulo si se esta importando

def main():
    contacto = Contacto("jfalskdjfl", "fd", "fd", "j");
    print(contacto)
    return

if __name__ == "__main__":
  main()
