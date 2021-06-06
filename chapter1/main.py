from chapter1.duck import ModelDuck, MallardDuck

if __name__ == '__main__':
    model_duck = ModelDuck()

    model_duck.display()
    model_duck.perform_quack()
    model_duck.perform_fly()


    print('--------------------------')


    mallar_duck = MallardDuck()
    mallar_duck.display()
    mallar_duck.perform_quack()
    mallar_duck.perform_fly()
