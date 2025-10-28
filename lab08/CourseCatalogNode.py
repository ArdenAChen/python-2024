from Event import Event

class CourseCatalogNode:
    def __init__(self, department, courseId, courseName, lecture, sections):
        self.department = department.upper()
        self.courseId = courseId
        self.courseName = courseName.upper()
        self.lecture = lecture
        self.sections = sections
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return_str =  f"{self.department} {self.courseId}: {self.courseName}\n * Lecture: {self.lecture}\n"
        for item in self.sections:
            return_str += f" + Section: {item}\n"
        return return_str
    
    # Helper methods for CourseCatalogNode
    def hasLeftChild(self):
        return self.left
    
    def hasRightChild(self):
        return self.right
    
    def isLeftChild(self):
        return self.parent and self.parent.left == self
    
    def isRightChild(self):
        return self.parent and self.parent.right == self
    
    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not (self.right or self.left)
    
    def hasAnyChildren(self):
        return self.right or self.left
    
    def hasBothChildren(self):
        return self.right and self.left
    
    def replaceNodeData(self, department, courseId, courseName, lecture, sections, lc, rc):
        self.department = department
        self.courseId = courseId
        self.courseName = courseName
        self.lecture = lecture
        self.sections = sections
        self.left = lc
        self.right = rc
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self
    
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.left
        return current

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.right.findMin()
        return succ
    
    def spliceOut(self): # used to delete the successor
        if self.isLeaf(): # Case 1 (node is a leaf, set parent's left or right child reference to None)
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.hasAnyChildren(): # case 2 (not leaf node, should only have right child for BST removal)
            if self.hasRightChild():
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent