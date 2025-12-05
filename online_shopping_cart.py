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




