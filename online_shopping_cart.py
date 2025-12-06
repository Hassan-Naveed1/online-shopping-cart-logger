import logging
import sys

#Creating my logger
shopping_cart = logging.getLogger(__name__)
shopping_cart.setLevel(logging.INFO)

#Creating a handler
shopping_handler = logging.FileHandler("cart.log")

#Creating a formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

#Assigning the formatter to the handler
shopping_handler.setFormatter(formatter)

#Assigning the handler to the logger
shopping_cart.addHandler(shopping_handler)

print("Items in Cart: ")
products = {
    "A":{"name":"Apple","price":2},
    "B":{"name":"Banana","price":3},
    "C":{"name":"Mango","price":4}
}
try:
    choice = input("Please choose one of the above to add in cart: ")
    if choice in products.keys():
        shopping_cart.info(f"The entered {choice} exists in the cart")
        quantity = int(input(f"Please enter the quantity of {choice} you would like to have: "))
        final_quantity = quantity * products[choice]["price"]
        shopping_cart.info(f"{quantity} {choice} has been added to the cart and the price of the product is: {final_quantity}")
    if choice not in products:
        raise ValueError("Invalid Product: The entered product doesnt exist.")
except ValueError as e:
    shopping_cart.info(f"Exception occured: {e}")