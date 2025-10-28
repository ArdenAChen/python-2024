class MovieCollectionNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setData(self, newData):
        self.data = newData
    
    def setNext(self, newNode):
        self.next = newNode