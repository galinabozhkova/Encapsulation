from Restaurant.food.dessert import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name):
        super().__init__(name, price=Cake.PRICE, grams=Cake.GRAMS, calories=Cake.CALORIES)
