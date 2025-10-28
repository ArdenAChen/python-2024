from Tea import Tea

class SpecialtyTea(Tea):
    def __init__(self, size, name):
        super().__init__(size)
        self.name = name

        if self.size == "S":
            self.price = 12.0
        elif self.size == "M":
            self.price = 16.0
        elif self.size == "L":
            self.price = 20.0
        
    def getTeaDetails(self):
        return f"SPECIALTY TEA\nSize: {self.size}\nName: {self.name}\nPrice: ${self.price:.2f}\n"
