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

  def get_promotion(self):
    """get promotions """
    return self.promotion

  def set_promotion(self, promotion):
    """set promotion to a product"""
    self.promotion = promotion

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


class NonStockedProduct(Product):
  """Subclass for products without tracking (digital product)"""

  def __init__(self, name: str, price: int):
    super().__init__(name, price, quantity=float('inf'))

  def show(self):
    return f"{self.name}: {self.price} (unlimited products in stock)"


class LimitedProduct(Product):
  """Subclass for products with a maximum quantity limit."""

  def __init__(self, name: str, price: int, quantity: int, maximum: int):
    super().__init__(name, price, quantity)
    self.maximum = maximum

  def show(self):
    return f"{self.name}: {self.price} (only {self.quantity} available)"

  def buy(self, quantity):
    if quantity > self.quantity:
      raise Exception(f'Cannot buy more than allowed, max: {self.quantity}')
    self.quantity -= quantity
    return self.price * quantity
