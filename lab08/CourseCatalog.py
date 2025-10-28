from Event import Event
from CourseCatalogNode import CourseCatalogNode

class CourseCatalog:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def _get(self, department, courseId, currentNode):
        department = department.upper()
        if not currentNode:
            return None
        if department < currentNode.department:
            return self._get(department, courseId, currentNode.left)
        elif department > currentNode.department:
            return self._get(department, courseId, currentNode.right)
        else:
            if courseId < currentNode.courseId:
                return self._get(department, courseId, currentNode.left)
            elif courseId > currentNode.courseId:
                return self._get(department, courseId, currentNode.right)
            else:
                return currentNode # returns object once it finds a matching object
    
    def get(self, department, courseId):
        department = department.upper()
        if self.root:
            return self._get(department, courseId, self.root) is not None # return True if an object is returned by _get
        return False # return False if no object can be returned by _get method

    def _addCourse(self, department, courseId, courseName, lecture, sections, currentNode):
        if (department, courseId) < (currentNode.department, currentNode.courseId):
            # Go to the left subtree
            if currentNode.hasLeftChild():
                self._addCourse(department, courseId, courseName, lecture, sections, currentNode.left)
            else:
                currentNode.left = CourseCatalogNode(department, courseId, courseName, lecture, sections)
                currentNode.left.parent = currentNode
        elif (department, courseId) > (currentNode.department, currentNode.courseId):
            # Go to the right subtree
            if currentNode.hasRightChild():
                self._addCourse(department, courseId, courseName, lecture, sections, currentNode.right)
            else:
                currentNode.right = CourseCatalogNode(department, courseId, courseName, lecture, sections)
                currentNode.right.parent = currentNode
    
    def addCourse(self, department, courseId, courseName, lecture, sections):
        department = department.upper()
        if self.get(department, courseId):
            return False
        if self.root:
            self._addCourse(department, courseId, courseName, lecture, sections, self.root)
        else:
            self.root = CourseCatalogNode(department, courseId, courseName, lecture, sections)
        self.size += 1
        return True
    
    def addSection(self, department, courseId, section):
        department = department.upper()
        courseNode = self._get(department, courseId, self.root)
        if not courseNode:
            return False
        else:
            courseNode.sections.append(section)
            return True
    
    def _inOrder(self, node):
        ret = ""
        if node:
            if node.hasLeftChild():
                ret += self._inOrder(node.left)
            ret += str(node)
            if node.hasRightChild():
                ret += self._inOrder(node.right)
        return ret

    def inOrder(self):
        ret = ""
        if self.root:
            ret = self._inOrder(self.root)
        return ret
    
    def _preOrder(self, node):
        ret = ""
        if node:
            ret += str(node)
            if node.hasLeftChild():
                ret += self._preOrder(node.left)
            if node.hasRightChild():
                ret += self._preOrder(node.right)
        return ret

    def preOrder(self):
        ret = ""
        if self.root:
            ret = self._preOrder(self.root)
        return ret

    def _postOrder(self, node):
        ret = ""
        if node:
            if node.hasLeftChild():
                ret += self._postOrder(node.left)
            if node.hasRightChild():
                ret += self._postOrder(node.right)
            ret += str(node)
        return ret

    def postOrder(self):
        ret = ""
        if self.root:
            ret = self._postOrder(self.root)
        return ret

    def getAttendableSections(self, department, courseId, availableDay, availableTime):
        department = department.upper()
        availableDay = availableDay.upper()
        courseNode = self._get(department, courseId, self.root)
        ret = ""
        
        if not courseNode:
            return ret

        for section in courseNode.sections:
            if section.day == availableDay:
                if availableTime[0] <= section.time[0] and availableTime[1] >= section.time[1]:
                    ret += str(section) + "\n"
        return ret

    def _countCoursesByDepartment(self, node, department_count):
        if node:
            self._countCoursesByDepartment(node.left, department_count)
            if node.department in department_count:
                department_count[node.department] += 1
            else:
                department_count[node.department] = 1
            self._countCoursesByDepartment(node.right, department_count)

    def countCoursesByDepartment(self):
        department_count = {}
        if self.root:
            self._countCoursesByDepartment(self.root, department_count)
        return department_count
    
    def deleteCourse(self, currentNode): # helper method for delete method
        if currentNode.isLeaf(): # Case 1: Node to remove is a leaf
            if currentNode == currentNode.parent.left:
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None
        elif currentNode.hasBothChildren(): # Case 3: Node to remove has both children
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.department = succ.department
            currentNode.courseId = succ.courseId
            currentNode.courseName = succ.courseName
            currentNode.lecture = succ.lecture
            currentNode.sections = succ.sections
        else: # Case 2: Node to remove has one child reference
            if currentNode.hasLeftChild(): # Node has left child
                if currentNode.isLeftChild():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.left = currentNode.left
                elif currentNode.isRightChild():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.right = currentNode.left
                else: # CurrentNode is the root
                    currentNode.replaceNodeData(currentNode.left.department, currentNode.left.courseId,
                                                currentNode.left.courseName, currentNode.left.lecture,
                                                currentNode.left.sections, currentNode.left.left,
                                                currentNode.left.right)
            else: # Node has right child
                if currentNode.isLeftChild():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.left = currentNode.right
                elif currentNode.isRightChild():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.right = currentNode.right
                else: # currentNode is the root
                    currentNode.replaceNodeData(currentNode.right.department, currentNode.right.courseId,
                                                currentNode.right.courseName, currentNode.right.lecture,
                                                currentNode.right.sections, currentNode.right.left,
                                                currentNode.right.right)

    def removeCourse(self, department, courseId):
        department = department.upper()
        nodeToRemove = self._get(department, courseId, self.root)
        if not nodeToRemove:
            return False
        elif self.root and self.root.isLeaf() and self.root.department == department and self.root.courseId == courseId:
            self.root = None
            self.size -= 1
            return True
        else:
            self.deleteCourse(nodeToRemove)
            self.size -= 1
            return True
                
    def removeSection(self, department, courseId, section):
        department = department.upper()
        courseNode = self._get(department, courseId, self.root)
        if not courseNode:
            return False
        else:
            if section in courseNode.sections:
                courseNode.sections.remove(section)
                return True
            else: # section not found
                return False