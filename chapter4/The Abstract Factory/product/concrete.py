from product.pizza import Pizza

class CheesePizza(Pizza):
    def __init__(self,ingredientFactory):
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print('Preparing Cheese Pizza..')

        dough = self.ingredientFactory.createDough()
        sauce = self.ingredientFactory.createSauce()
        cheese = self.ingredientFactory.createCheese()