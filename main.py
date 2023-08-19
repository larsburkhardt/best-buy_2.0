import products
import store


def start(store_obj):
  """
  Showing the menu and providing the options to select as user input
  :param store_obj: Referencing Store object in store.py
  """

  while True:
    print("\n"
          "1. List all products in store\n"
          "2. Show total amount in store\n"
          "3. Make an order\n"
          "4. Quit\n")

    try:
      user_input = int(input("Please chose an option between 1 and 4"))
      if not isinstance(user_input, int) or user_input <= 0 or user_input > 4:
        raise ValueError("invalid choice")
    except ValueError:
      print("Please enter a valid choice between 1 and 4")

    if user_input == 1:
      list_item = 1
      print("--------------------------------------------")
      for product in store_obj.get_all_products():
        print(f"{list_item}. {product.show()}")
        list_item += 1
      print("--------------------------------------------")

    elif user_input == 2:
      print(f"There are {store_obj.get_total_quantity()} products in store")

    elif user_input == 3:

      while True:
        list_item = 1
        order_basket = []

        # list items and append every item to order_basket
        print("------------------------")
        for product in store_obj.get_all_products():
          print(f"{list_item}. {product.show()}")
          list_item += 1
        print("------------------------")
        print("Please enter empty text to finish your purchase")

        try:
          product_choice = int(input("Please enter the product number you want to purchase: "))
          product_quantity = int(input("Please enter the quantity of the selected product: "))
          selected_product = store_obj.store_products[product_choice - 1]

          # Check if entered values are empty - if so, raise error
          if product_choice == "" or product_quantity == "":
            raise ValueError("Please provide valid numbers")

          order_basket.append((selected_product, product_quantity))

          total_price = store_obj.order(order_basket)

          print(f"You have ordered {product_quantity} of {selected_product.name}")
          print(f"The total price of your order is {total_price}")

        except IndexError as e:
          print("Something went wrong", e)
        except ValueError as e:
          print(f"An error occured: {e} \nBack to menu")
          break

    # store_obj.order()
    elif user_input == 4:
      print("Thank you for purchasing in our shop!")
      break
    else:
      print("Please enter a valid choice between 1 and 4")


def main():
  """Main function, loads product list and executes start function"""

  product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                  products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                  products.Product("Google Pixel 7", price=500, quantity=250),
                  ]

  _store = store.Store(product_list)
  _products = _store.get_all_products()

  # print(_store.get_total_quantity())
  # print(_store.order([(_products[0], 1), (_products[1], 2)]))

  start(_store)


if __name__ == "__main__":
  main()
