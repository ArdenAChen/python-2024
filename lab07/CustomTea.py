from Tea import Tea

class CustomTea(Tea):
    def __init__(self, size, base):
        super().__init__(size)
        self.base = base
        self.flavors = []

        if self.size == "S":
            self.price = 10.0
        elif self.size == "M":
            self.price = 15.0
        elif self.size == "L":
            self.price = 20.0
    
    def setBase(self, base):
        self.base = base
    
    def getBase(self):
        return self.base
    
    def addFlavor(self, flavor):
        self.flavors.append(flavor)
        if self.size == "S":
            self.price += 0.25
        elif self.size == "M":
            self.price += 0.5
        elif self.size == "L":
            self.price += 0.75
    
    def getTeaDetails(self):
        customTeaStr = ""
        customTeaStr += f"CUSTOM TEA\nSize: {self.size}\nBase: {self.base}\nFlavors:\n"
        for flavor in self.flavors:
            customTeaStr += f"\t+ {flavor}\n"
        customTeaStr += f"Price: ${self.price:.2f}\n"
        return customTeaStr