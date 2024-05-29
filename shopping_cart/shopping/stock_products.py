from .product_stock import ProductStock

class StockProducts:
  def __init__(self):
    self._products = {}

  def add_product(self, product):
    self._products[product.name] = product
    print("Producto agregado en stock exitosamente...")

  def get_product(self, name):
    return self._products.get(name)

  def delete_products(self, name, cuantity):
    if self._products[name].cuantity >= cuantity:
      self._products[name].cuantity -= cuantity 
      print("Producto eliminado exitosamente...")
    else:
      print("Producto no encontrado...")
