from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice

class DrinkOrder:
    def __init__(self):
        self.drinks = [] # initialize empty list called "drinks"
    
    def addBeverage(self, beverage):
        self.drinks.append(beverage) # appends Beverage to drinks list
    
    def getTotalOrder(self):
        total_price = 0.0 # will be used to calculate price
        drinks_str = 'Order Items:\n' # Beginning of string that should be returned
        for drink in self.drinks:
            total_price += drink.price
            drinks_str += '* ' + drink.getInfo() + '\n'
        total_price = f'{total_price:.2f}'
        drinks_str += 'Total Price: $' + total_price
        return drinks_str