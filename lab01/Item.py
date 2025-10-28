class Item:
    def __init__(self, upc=None, category=None, name=None, price=None):
        self.upc = upc
        self.category = category
        self.name = name
        self.price = price
        if self.category != None:
            self.category = category.upper()
        if self.name != None:
            self.name = name.upper()
    def setUpc(self, upc):
        self.upc = upc
    def setCategory(self, category):
        self.category = category.upper()
    def setName(self, name):
        self.name = name.upper()
    def setPrice(self, price):
        self.price = price
    def toString(self):
        item_str = f'UPC: {self.upc}, Category: {self.category}, Name: {self.name}, Price: ${self.price:.2f}'
        return item_str
