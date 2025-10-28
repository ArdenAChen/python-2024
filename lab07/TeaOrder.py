from Tea import Tea
from CustomTea import CustomTea
from SpecialtyTea import SpecialtyTea

class TeaOrder:
    def __init__(self, distance):
        self.teas = []
        self.distance = distance
    
    def addTea(self, tea):
        self.teas.append(tea)
    
    def getOrderDescription(self):
        orderPrice = 0

        for tea in self.teas:
            orderPrice += tea.getPrice()

        orderStr = f"******\nShipping Distance: {self.distance} miles\n"
        for tea in self.teas:
            orderStr += tea.getTeaDetails()
            orderStr += "\n"
            orderStr += "----\n"
        
        orderStr += f"TOTAL ORDER PRICE: ${orderPrice:.2f}\n******\n"

        return orderStr