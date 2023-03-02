from order import Order

class Pizza(Order):
    def __init__(self) -> None:
        super().__init__("Pizza", 15)
    

class Pasta(Order):
    def __init__(self) -> None:
        super().__init__("Pasta", 13)


class Salad(Order):
    def __init__(self) -> None:
        super().__init__("Salad", 12)

