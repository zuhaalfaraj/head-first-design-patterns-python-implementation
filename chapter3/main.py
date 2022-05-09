from menu import *

beverage1 = Espresso()
beverage2 = HouseBlend()

beverage1 = Mocha(beverage1)
beverage2 = Mocha(beverage2)

print(beverage1.get_description() ,beverage1.cost())

print(beverage2.get_description() ,beverage2.cost())