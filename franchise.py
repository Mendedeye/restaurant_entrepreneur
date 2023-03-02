from order_factory import Order_Factory
from logger import logger

class Franchise:
    def __init__(self, store_id) -> None:
        self.store_id = store_id

    def place_order(self):
        user_choice = input("Please choose one of these dishes: pizza, pasta, or salad: ")

        order = Order_Factory.create_order(user_choice)

        logger.log_transaction(order, self.store_id)

        

