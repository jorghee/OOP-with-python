from .product_stock import ProductStock

class StockProducts:
  def __init__(self):
    self._products = {}

  def add_product(self, product):
    self._products[product.name] = product
    print("Producto agregado en stock exitosamente...")

  def get_product(self, name):
    return self._products.get(name)
