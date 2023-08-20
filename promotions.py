from abc import ABC, abstractmethod


class Promotions(ABC):
  def __init__(self, promotion) -> None:
    self.promotion = promotion

  @abstractmethod
  def apply_promotion(self, product, quantity) -> float:
    pass


class SecondHalfPrice(Promotions):
  """Reduces price for every 2nd item to 50%"""

  def apply_promotion(self, product, quantity) -> float:
    total_price = 0
    half_price = product.price * 0.5

    for item in range(1, quantity + 1):
      if item % 2 == 0:
        total_price += half_price
      else:
        total_price += product.price

    num_promoted_products = (quantity + 1) // 2
    total_price = total_price * num_promoted_products
    return total_price



class ThirdOneFree(Promotions):
  """every 3rd product at no cost"""

  def apply_promotion(self, product, quantity) -> float:
    total_price = 0

    for item in range(1, quantity + 1):
      if item % 3 == 0:
        continue
      else:
        total_price += product.price
    return total_price


class PercentDiscount(Promotions):
  def __init__(self, promotion, percent) -> None:
    super().__init__(promotion)

    if percent <= 0:
      raise ValueError("Discount must be more than 0")
    elif percent > 100:
      raise ValueError("Discount mustn't be more than 100")
    else:
      self.percent = percent

  def apply_promotion(self, product, quantity) -> float:
    price_with_promo = product.price - (product.price * (self.percent / 100))
    return quantity * price_with_promo
