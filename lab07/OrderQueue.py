from Tea import Tea
from CustomTea import CustomTea
from SpecialtyTea import SpecialtyTea
from TeaOrder import TeaOrder

class QueueEmptyException(Exception):
    pass

class OrderQueue:
    def __init__(self):
        self.maxHeap = [0]
        self.currentSize = 0
    
    def addOrder(self, teaOrder):
        self.maxHeap.append(teaOrder)
        self.currentSize += 1
        i = self.currentSize # percUp function done in addOrder function
        while i // 2 > 0:
            if self.maxHeap[i].distance > self.maxHeap[i // 2].distance:
                tmp = self.maxHeap[i // 2]
                self.maxHeap[i // 2] = self.maxHeap[i]
                self.maxHeap[i] = tmp
            i = i // 2
    
    def maxChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.maxHeap[i * 2].distance > self.maxHeap[i * 2 + 1].distance:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.maxHeap[i].distance < self.maxHeap[mc].distance:
                tmp = self.maxHeap[i]
                self.maxHeap[i] = self.maxHeap[mc]
                self.maxHeap[mc] = tmp
            i = mc

    def processNextOrder(self):
        if self.currentSize == 0: # Raise QueueEmptyException when queue is empty
            raise QueueEmptyException()

        retval = self.maxHeap[1].getOrderDescription() # return variable for object removed
        self.maxHeap[1] = self.maxHeap[self.currentSize]
        self.currentSize -= 1
        self.maxHeap.pop()
        self.percDown(1)
        return retval