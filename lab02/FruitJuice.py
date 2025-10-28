from Beverage import Beverage

class FruitJuice(Beverage):
    def __init__(self, ounces, price, fruits):
        super().__init__(ounces, price)
        self.fruits = fruits
    
    def getInfo(self):
        fruits_str = ''
        for fruit in self.fruits:
            fruits_str += fruit + '/'
        fruits_str = fruits_str[:-1] # get rid of the last /
        fruits_str += ' Juice, ' + super().getInfo()
        return fruits_str