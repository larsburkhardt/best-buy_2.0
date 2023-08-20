import pytest

from products import Product


def test_create_product():
  """Tests if creating product works correctly"""

  product = Product("Test Product", 10, 50)
  assert product.name == "Test Product"
  assert product.price == 10
  assert product.quantity == 50
  assert product.active == True


def test_wrong_product_details():
  """Test if correct product values are provided"""

  with pytest.raises(ValueError):
    Product("", price=100, quantity=100)
  with pytest.raises(ValueError):
    Product("Test Product", price=-100, quantity=100)
  with pytest.raises(ValueError):
    Product("Test Product", price=100, quantity=-100)


def test_product_inactive():
  """Test if product gets inactive when out of stock"""

  product = Product("Test Product", 10, 50)
  product.set_quantity(0)
  product.is_active() == False


def test_buy_product():
  """test if total price gets calculated correctly"""

  product = Product("Test Product", 10, 50)
  price_total = product.buy(5)
  assert product.quantity == 45
  assert price_total == 10 * 5


def test_buy_more_than_available():
  """ test if error raises when more products bought than available"""

  product = Product("Test Product", 10, 50)
  with pytest.raises(ValueError):
    product.buy(51)


pytest.main()
