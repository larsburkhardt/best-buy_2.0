class Product:

  def __init__(self, name: str, price: float, quantity: int):

    if not name:
      raise ValueError("Product name mustn't be empty")

    if price < 0 or quantity < 0:
      raise ValueError("Price and amount can't be negative")



    self.name = name
    self.price = price
    self.quantity = quantity
    self.active = True

  def get_quantity(self) -> float:
    """Get quantity of a product"""
    return self.quantity

  def set_quantity(self, quantity):
    """Set quantity of a product"""
    self.quantity = quantity
    if self.quantity <= 0:
      self.deactivate()

  def is_active(self) -> bool:
    """Helper for checking if product is active"""
    return self.active

  def activate(self):
    """Set product to active state"""
    self.active = True

  def deactivate(self):
    """Helper for deactivating a product"""
    self.active = False

  def show(self):
    """Show name, price and quantity of product"""
    return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

  def buy(self, quantity) -> float:
    """
    For buying a product with given amount
    Returns the total price -> float
    Raises Error when more ordered than in stock
    """

    if quantity > self.quantity:
      raise ValueError("More than we have")
    else:
      self.quantity -= quantity
      total_price = quantity * self.price
      return total_price
