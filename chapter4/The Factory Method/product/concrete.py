from product.pizza import Pizza


class NYStyleCheesePizza(Pizza):
    NAME = "NY Style Sauce and Cheese Pizza"
    DOUGH = "Thin Crust Dough"
    SAUCE = "Marinara Sauce"
    TOPPINGS = ["Grated Reggiano Cheese", 'Chilli']



class NYStylePepperoniPizza(Pizza):
    NAME = "NY Style Sauce and Pepperoni Pizza"
    DOUGH = "Thin Crust Dough"
    SAUCE = "Marinara Sauce"
    TOPPINGS = ["Pepperoni"]


class NYStyleClamPizza(Pizza):
    NAME = "NY Style Sauce and Clam Pizza"
    DOUGH = "Thin Crust Dough"
    SAUCE = "Marinara Sauce"
    TOPPINGS = ["Clam"]


class NYStyleVeggiePizza(Pizza):
    NAME = "NY Style Sauce and Veggie Pizza"
    DOUGH = "Thin Crust Dough"
    SAUCE = "Marinara Sauce"
    TOPPINGS = ["Veggie"]




class ChicagoStyleCheesePizza(Pizza):
    NAME = "Chicago Style Deep Dish Cheese Pizza"
    DOUGH = "Extra Thick Crust Dough"
    SAUCE = "Plum Tomato Sauce"
    TOPPINGS = ["Shredded Mozzarella Cheese"]


    def cut(self):
        print("Cutting the pizza into square slices")


class ChicagoStylePepperoniPizza(Pizza):
    NAME = "Chicago Style Deep Dish Pepperoni Pizza"
    DOUGH = "Extra Thick Crust Dough"
    SAUCE = "Plum Tomato Sauce"
    TOPPINGS = ["Pepperoni"]


    def cut(self):
        print("Cutting the pizza into square slices")



class ChicagoStyleClamPizza(Pizza):
    NAME = "Chicago Style Deep Dish Clam Pizza"
    DOUGH = "Extra Thick Crust Dough"
    SAUCE = "Plum Tomato Sauce"
    TOPPINGS = ["Clam"]


    def cut(self):
        print("Cutting the pizza into square slices")



class ChicagoStyleVeggiePizza(Pizza):
    NAME = "Chicago Style Deep Dish Veggie Pizza"
    DOUGH = "Extra Thick Crust Dough"
    SAUCE = "Plum Tomato Sauce"
    TOPPINGS = ["Veggie"]


    def cut(self):
        print("Cutting the pizza into square slices")
