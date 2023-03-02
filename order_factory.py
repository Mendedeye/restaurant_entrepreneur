from food_classes import Pizza
from food_classes import Pasta
from food_classes import Salad

entry_error = -1

class Order_Factory:
    @staticmethod
    def create_order(dish_name):
        if  dish_name is "pizza":
            return Pizza()
        elif dish_name is "pasta":
            return Pasta()
        elif dish_name is "salad":
            return Salad()