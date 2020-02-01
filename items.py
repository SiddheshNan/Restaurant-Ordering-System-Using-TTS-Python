class Item:
    def __init__(self, thing, rs):
        self.thing = thing
        self.rs = rs

class Burgers:
    def __init__(self):
        self.burgers = []
        self.burgers.append(Item('Veg','40'))
        self.burgers.append(Item('Paneer','55'))
        self.burgers.append(Item('Cheese','55'))
        self.burgers.append(Item('Egg','45'))
        self.burgers.append(Item('Chicken','60'))
        self.burgers.append(Item('Grill Chicken','65'))

class Shakes:
    def __init__(self):
        self.shakes = []
        self.shakes.append(Item('Chocolate Shake','40'))
        self.shakes.append(Item('Black Currant Shake','55'))
        self.shakes.append(Item('Mango Shake','40'))
        self.shakes.append(Item('Strawberry Shake','40'))
        self.shakes.append(Item('Coke','45'))


class Combos:
    def __init__(self):
        self.combos = []
        self.combos.append(Item('Cheese Fries and Medium Coke','146'))
        self.combos.append(Item('Veg Burger and Fries and Coke','196'))
        self.combos.append(Item('Egg Burger and Fries and Coke','186'))

def food():
    return ['burgers','shakes','combos']