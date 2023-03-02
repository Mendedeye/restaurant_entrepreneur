class Logger:
    def __init__(self) -> None:
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, order, store_id):
        self.transaction_count += 1
        self.daily_sales += order.price
        file = open("log.txt", "a")
        file.write(f"""
        Transaction:  {self.transaction_count}
        Meal Ordered: {order.dish_name}
        Store ID:     {store_id}
        Item Price:   {order.price}
        Daily Income  {self.daily_sales}
        ________________________________________""")
        file.close()

loger = Logger()