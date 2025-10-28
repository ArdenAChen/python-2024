from Apartment import Apartment

def mergesort(apartmentList):
    # if false, do nothing
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2 # keep track of middle index

        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]

        # recursively sort the lefthalf, then righthalf
        mergesort(lefthalf)
        mergesort(righthalf)

        # merge step, merge two sorted sublists (left/right) half into apartmentList
        li = 0 # lefthalf index
        ri = 0 # righthalf index
        ai = 0 # apartmentList index

        while li < len(lefthalf) and ri < len(righthalf):
            if lefthalf[li] < righthalf[ri]:
                apartmentList[ai] = lefthalf[li]
                li += 1
            else:
                apartmentList[ai] = righthalf[ri]
                ri += 1
            ai += 1
        
        while li < len(lefthalf): # Put any remaining lefthalf elements if they exist into apartmentList
            apartmentList[ai] = lefthalf[li]
            li += 1
            ai += 1
        
        while ri < len(righthalf): # Put any remainging righthalf elements if they exist into apartmentList
            apartmentList[ai] = righthalf[ri]
            ri += 1
            ai += 1

def ensureSortedAscending(apartmentList):
    for i in range(len(apartmentList) - 1): # iterates over list, checks if value at index i > value at index i + 1
        if apartmentList[i] > apartmentList[i + 1]:
            return False # Returns False if any value is greater than the index ahead, otherwise returns True
    return True

def getBestApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[0].getApartmentDetails()

def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[-1].getApartmentDetails()

def getAffordableApartments(apartmentList, budget):
    affordableList = [] # empty list to store all apartments that meet budget requirements

    for i in apartmentList:
        if i.rent <= budget:
            affordableList.append(i)

    if len(affordableList) == 0:
        return ''
    
    mergesort(affordableList)

    affordableStr = ''
    for j in affordableList:
        affordableStr += j.getApartmentDetails() + "\n"
    
    return affordableStr.strip() # strip removes last newline