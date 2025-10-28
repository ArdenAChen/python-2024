class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return f'{self.items}'

d = Deque()
d.addFront(1)
d.addFront(2)
d.addRear(3)
d.addRear(4)
d.addFront(5)
d.addRear(6)
d.removeFront()
d.addFront(7)
d.removeRear()
d.addRear(8)

print(d)

[843127]