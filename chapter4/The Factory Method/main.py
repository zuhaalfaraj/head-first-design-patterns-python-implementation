from factory.concrete import *


if __name__ == '__main__':
    ny_store = NYStylePizzaStore()
    ny_store.order_pizza("cheese")

    chicago_store = ChicagoStylePizzaStore()
    chicago_store.order_pizza("cheese")