from Event import Event
from CourseCatalogNode import CourseCatalogNode
from CourseCatalog import CourseCatalog

def test_Event():
    e = Event("MWF", (1200, 1250), "ilp")
    assert e.day == "MWF"
    assert e.time == (1200, 1250)
    assert e.location == "ILP"

    e1 = e
    e2 = Event("MW", (1200, 1250), "ILP")
    e3 = Event("WF", (1300, 1350), "GIRVETZ")
    assert e1 == e
    assert e != e2
    assert e != e3

    assert str(e) == "MWF 12:00 - 12:50, ILP"
    assert str(e2) == "MW 12:00 - 12:50, ILP"

def test_CourseCatalogNode():
    lecture = Event("TR", (1100, 1150), "NORTH HALL")
    s1 = Event("W", (1500, 1550), "HSSB")
    s2 = Event("W", (1600, 1650), "HSSB")
    sections = [s1, s2]
    ccn = CourseCatalogNode("engl", 10, "study of fortnite", lecture, sections)
    assert ccn.department == "ENGL"
    assert ccn.courseId == 10
    assert ccn.courseName == "STUDY OF FORTNITE"
    assert ccn.lecture == Event("TR", (1100, 1150), "NORTH HALL")
    assert ccn.sections == [Event("W", (1500, 1550), "HSSB"), Event("W", (1600, 1650), "HSSB")]
    assert ccn.left == None
    assert ccn.right == None
    assert ccn.parent == None
    assert str(ccn) == "ENGL 10: STUDY OF FORTNITE\n * Lecture: TR 11:00 - 11:50, NORTH HALL\n + Section: W 15:00 - 15:50, HSSB\n + Section: W 16:00 - 16:50, HSSB\n"

def test_CourseCatalog():
    # test constructor
    cc = CourseCatalog()
    assert cc.root == None
    assert cc.size == 0

    lecture = Event("TR", (1100, 1150), "NORTH HALL")
    s1 = Event("W", (1500, 1550), "HSSB")
    s2 = Event("W", (1600, 1650), "HSSB")
    sections = [s1, s2]
    ccn = CourseCatalogNode("engl", 10, "study of fortnite", lecture, sections)

    # test addCourse
    assert cc.addCourse("engl", 10, "study of fortnite", lecture, sections) == True
    assert cc.addCourse("engl", 10, "study of pubg", lecture, sections) == False # Check that it returns False if there's a repeat
    assert cc.size == 1
    assert cc.root.department == ccn.department
    assert cc.root.courseId == ccn.courseId
    assert cc.root.courseName == ccn.courseName
    assert cc.root.left == None
    assert cc.root.right == None
    assert cc.root.parent == None

    # test addSection
    s3 = Event("W", (1700, 1750), "HSSB")
    assert cc.addSection("cmpsc", 200, s3) == False
    assert cc.addSection("engl", 10, s3) == True
    assert cc.root.sections == [s1, s2, s3]
    assert str(cc.root) == "ENGL 10: STUDY OF FORTNITE\n * Lecture: TR 11:00 - 11:50, NORTH HALL\n + Section: W 15:00 - 15:50, HSSB\n + Section: W 16:00 - 16:50, HSSB\n + Section: W 17:00 - 17:50, HSSB\n"

    # test binary search tree holds up
    lecture2 = Event("MW", (1000, 1050), "PHELPS HALL")
    s4 = Event("R", (1300, 1350), "PHELPS HALL")
    s5 = Event("R", (1900, 1950), "PHELPS HALL")
    sections2 = [s4, s5]
    cc.addCourse("art", 101, "studying music: yeat", lecture2, sections2)
    cc.addCourse("pstat", 120, "torture", lecture2, sections2)
    cc.addCourse("engl", 100, "random english class", lecture2, sections2)
    cc.addCourse("engl", 2, "lower english", lecture2, sections2)
    assert cc.root.left.department == "ART" # Make sure it goes to left if name is lesser value
    assert cc.root.right.department == "PSTAT" # Make sure it goes to right if name is right value
    assert cc.root.right.parent.department == "ENGL"
    assert cc.root.left.parent.department == "ENGL"
    assert cc.root.right.left.department == "ENGL" # ENGL 110 should go to the left of the right subtree
    assert cc.root.right.left.courseId == 100
    assert cc.root.left.right.courseId == 2 # Ensure ENGL 2 should be in left subtree as right ref of art

    # test inOrder traversal
    inOrderNode1 = str(CourseCatalogNode("art", 101, "studying music: yeat", lecture2, sections2))
    inOrderNode2 = str(CourseCatalogNode("ENGL", 2, "lower english", lecture2, sections2))
    inOrderNode3 = str(ccn)
    inOrderNode4 = str(CourseCatalogNode("ENGL", 100, "random english class", lecture2, sections2))
    inOrderNode5 = str(CourseCatalogNode("PSTAT", 120, "torture", lecture2, sections2))

    assert cc.inOrder() == f'{inOrderNode1}{inOrderNode2}{inOrderNode3}{inOrderNode4}{inOrderNode5}'

    # test preOrder traversal follows correct algorithm
    assert cc.preOrder() == f'{inOrderNode3}{inOrderNode1}{inOrderNode2}{inOrderNode5}{inOrderNode4}'

    # test postOrder traversal follows correct algorithm
    assert cc.postOrder() == f'{inOrderNode2}{inOrderNode1}{inOrderNode4}{inOrderNode5}{inOrderNode3}'

    # test getAttendableSections
    assert cc.getAttendableSections("art", 101, "M", (500, 2300)) == '' # no sections available because no sections on Monday
    assert cc.getAttendableSections("art", 101, "R", (500, 700)) == '' # no sections b/c not in available time
    assert cc.getAttendableSections("art", 101, "R", (1300, 2000)) == f'{str(s4)}\n{str(s5)}\n' # tests both sections appear
    assert cc.getAttendableSections("art", 101, "R", (1300, 1500)) == f'{str(s4)}\n' # only s4 should show up

    # test countCoursesByDepartment
    assert cc.countCoursesByDepartment() == {"ART": 1, "ENGL": 3, "PSTAT": 1}
    cc.addCourse("CMPSC", 9, "Intermediate Python", lecture2, sections2)
    assert cc.countCoursesByDepartment() == {"ART": 1, "CMPSC": 1, "ENGL": 3, "PSTAT": 1}
    cc.addCourse("PSTAT", 10, "Programming in R", lecture2, sections2)
    assert cc.countCoursesByDepartment() == {"ART": 1, "CMPSC": 1, "ENGL": 3, "PSTAT": 2}

def test_removeSection():
    cc = CourseCatalog()
    lecture = Event("TR", (1100, 1150), "NORTH HALL")
    s1 = Event("W", (1500, 1550), "HSSB")
    s2 = Event("W", (1600, 1650), "HSSB")
    s3 = Event("W", (1700, 1750), "HSSB")
    s4 = Event("W", (1500, 1550), "HSSB")
    sections = [s1, s2]
    cc.addCourse("engl", 10, "study of fortnite", lecture, sections)
    assert cc.removeSection("engl", 200, s1) == False
    assert cc.removeSection("engl", 10, s4) == True
    assert s1 not in cc.root.sections
    assert cc.root.sections == [s2] # ensure that the right section was removed
    assert cc.removeSection("engl", 10, s3) == False # still returns False if section does not exist in section list

def test_removeCourseLeaf():
    cc = CourseCatalog()
    lecture = Event("TR", (1100, 1150), "NORTH HALL")
    s1 = Event("W", (1500, 1550), "HSSB")
    s2 = Event("W", (1600, 1650), "HSSB")
    sections = [s1, s2]
    # Test empty BST returns false
    assert cc.removeCourse("cmpsc", 200) == False

    # Test removing root when it's the only node in the BST
    cc.addCourse("engl", 10, "study of fortnite", lecture, sections)
    assert cc.removeCourse("engl", 10) == True
    assert cc.size == 0
    assert cc.root == None
    assert cc.get("engl", 10) == False
    assert cc.inOrder() == ""

    cc.addCourse("engl", 10, "study of fortnite", lecture, sections)
    cc.addCourse("cmpsc", 9, "cs", lecture, sections)
    cc.addCourse("engl", 101, "study of overwatch", lecture, sections)
    assert cc.removeCourse("engl", 101) == True
    assert cc.get("engl", 101) == False
    assert cc.size == 2
    assert cc.root != None

    assert cc.removeCourse("cmpsc", 9) == True
    assert cc.get("cmpsc", 9) == False
    assert cc.size == 1
    assert cc.root != None
    assert cc.root.parent == None

def test_removeCourseOneChild():
    cc = CourseCatalog()
    lecture = Event("TR", (1100, 1150), "NORTH HALL")
    s1 = Event("W", (1500, 1550), "HSSB")
    s2 = Event("W", (1600, 1650), "HSSB")
    sections = [s1, s2]

    cc.addCourse("engl", 10, "study of fortnite", lecture, sections)
    cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)
    cc.addCourse("cmpsc", 8, "introduction to python", lecture, sections)

    # Test non-root, is left child, has left child
    assert cc.removeCourse("cmpsc", 9) == True
    assert cc.get("cmpsc", 9) == False
    assert cc.root.left.courseId == 8 # Make sure that the new left child reference to the root is cs8
    assert cc.root.left.department == "CMPSC"

    # Test non-root, is left child, has right child
    cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)
    assert cc.removeCourse("cmpsc", 8) == True
    assert cc.get("cmpsc", 8) == False
    assert cc.root.left.courseId == 9
    assert cc.root.left.department == "CMPSC"

    # Test non-root, is right child, has left child
    cc.addCourse("history", 5, "stories", lecture, sections)
    cc.addCourse("pstat", 8, "introduction to R", lecture, sections)
    assert cc.removeCourse("history", 5) == True
    assert cc.get("history", 5) == False
    assert cc.root.right.courseId == 8
    assert cc.root.right.department == "PSTAT"

    # Test non-root, is right child, has right child
    cc.addCourse("pstat", 10, "introduction to R", lecture, sections)
    assert cc.removeCourse("pstat", 8) == True
    assert cc.root.right.courseId == 10

    # Test root, has left child
    cc1 = CourseCatalog()
    cc1.addCourse("engl", 10, "study of fortnite", lecture, sections)
    cc1.addCourse("cmpsc", 9, "intermediate python", lecture, sections)
    assert cc1.removeCourse("engl", 10) == True
    assert cc1.root.department == "CMPSC"
    assert cc1.root.courseId == 9
    assert cc1.root.left == None
    assert cc1.root.right == None

    # Test root, has right child
    cc1.addCourse("pstat", 8, "proofs", lecture, sections)
    assert cc1.removeCourse("cmpsc", 9) == True
    assert cc1.root.department == "PSTAT"
    assert cc1.root.courseId == 8
    assert cc1.root.left == None
    assert cc1.root.right == None

def test_removeCourseTwoChildren():
    cc = CourseCatalog()
    lecture = Event("TR", (1100, 1150), "NORTH HALL")
    s1 = Event("W", (1500, 1550), "HSSB")
    s2 = Event("W", (1600, 1650), "HSSB")
    sections = [s1, s2]
    cc.addCourse("engl", 10, "lit stuff", lecture, sections)
    cc.addCourse("cmpsc", 9, "int python", lecture, sections)
    cc.addCourse("pstat", 8, "proofs", lecture, sections)
    assert cc.removeCourse("engl", 10) == True
    assert cc.get("cmpsc", 9) == True # Ensure we have the correct references maintained
    assert cc.get("engl", 10) == False
    assert cc.root.department == "PSTAT"
    assert cc.root.courseId == 8

    cc.addCourse("art", 1, "yeat", lecture, sections)
    cc.addCourse("data", 15, "random", lecture, sections)
    assert cc.removeCourse("cmpsc", 9) == True
    assert cc.get("cmpsc", 9) == False
    assert cc.root.left.department == "DATA"
    assert cc.root.parent == None

def test_random():
    cc = CourseCatalog()
    lecture = Event("TR", (1100, 1150), "NORTH HALL")
    s1 = Event("W", (1500, 1550), "HSSB")
    s2 = Event("W", (1600, 1650), "HSSB")
    sections = [s1, s2]
    def makeNode(department, courseId):
        cc.addCourse(department, courseId, "a", lecture, sections)
        return True
    makeNode("a", 1)
    makeNode("b", 2)
    makeNode("c", 3)
    makeNode("d", 4)
    makeNode("e", 5)
    makeNode("f", 6)
    makeNode("g", 7)
    makeNode("h", 8)
    assert cc.get("h", 8) == True
    assert cc._get("g", 7, cc.root).right == cc._get("h", 8, cc.root)
    assert cc.removeCourse("h", 8) == True
    assert cc._get("g", 7, cc.root).right == None
    assert cc.removeCourse("g", 7) == True
    assert cc._get("f", 6, cc.root).right == None
    assert cc.removeCourse("f", 6) == True
    assert cc.removeCourse("e", 5) == True
    assert cc.removeCourse("d", 4) == True
    assert cc.removeCourse("c", 3) == True
    assert cc.removeCourse("b", 2) == True
    assert cc.size == 1
    assert cc.removeCourse("a", 1) == True
    assert cc.size == 0