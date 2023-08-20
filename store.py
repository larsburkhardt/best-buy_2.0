class Store:

  def __init__(self, store_products):
    self.store_products = store_products

  def add_product(self, product):
    """Add a product to the products list (store_products)"""
    self.store_products.append(product)

  def remove_product(self, product):
    """Removes specific product from list"""
    store_product_index = self.store_products.index(product)
    del self.store_products[store_product_index]

  def get_total_quantity(self) -> int:
    """Returns quantity of ALL PRODUCTS"""
    total_product_quantity = 0
    for product in self.store_products:
      total_product_quantity += product.quantity
    return total_product_quantity

  def get_all_products(self) -> list:
    """Lists all ACTIVE products"""
    active_products = []
    for product in self.store_products:
      if product.is_active():
        active_products.append(product)
    return active_products

  def order(self, shopping_list) -> float:
    order_price = 0

    for item in shopping_list:
      order_product, order_quantity = item

      if order_product.quantity >= order_quantity:
        # Überprüfen, ob eine Promotion für das Produkt vorhanden ist
        if order_product.get_promotion() is not None:
          promotion = order_product.get_promotion()
          order_price += promotion.apply_promotion(order_product, order_quantity)
        else:
          order_price += order_product.price * order_quantity

        order_product.quantity -= order_quantity

        # Deaktiviere das Produkt, wenn der Bestand aufgebraucht ist
        if order_product.quantity == 0:
          order_product.deactivate()
      else:
        raise ValueError(f"Sorry, only {order_product.quantity} items of {order_product.name} in stock.")

      return order_price

    return order_price
