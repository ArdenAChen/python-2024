from Tea import Tea
from CustomTea import CustomTea
from SpecialtyTea import SpecialtyTea
from TeaOrder import TeaOrder
from OrderQueue import OrderQueue
from OrderQueue import QueueEmptyException

def test_tea():
    t = Tea("S")
    assert t.price == 0.0
    assert t.size == "S"
    assert t.getPrice() == 0.0
    assert t.getSize() == "S"
    t.setPrice(2.0)
    t.setSize("M")
    assert t.getPrice() == 2.0
    assert t.getSize() == "M"

def test_customTeaInitAndGetter():
    ct = CustomTea("S", "Black")
    assert ct.getPrice() == 10.0
    assert ct.getSize() == "S"
    assert ct.flavors == []
    assert ct.getBase() == "Black"
    ct.setSize("M")
    assert ct.getSize() == "M"
    assert ct.getPrice() == 10.0
    ct.setPrice(15.0)
    assert ct.getPrice() == 15.0
    ct.setBase("Green")
    assert ct.getBase() == "Green"

def test_customTeaPrice():
    ct = CustomTea("S", "Green")
    assert ct.getPrice() == 10.0
    ct.addFlavor("a")
    assert ct.flavors == ['a']
    assert ct.getPrice() == 10.25
    ct.addFlavor("b")
    assert ct.flavors == ['a', 'b']
    assert ct.getPrice() == 10.5

    ct1 = CustomTea("M", "Green")
    assert ct1.getPrice() == 15.0
    ct1.addFlavor("a")
    assert ct1.getPrice() == 15.5

    ct2 = CustomTea("L", "Green")
    assert ct2.getPrice() == 20.0
    ct2.addFlavor("a")
    assert ct2.getPrice() == 20.75

def test_customTeaDetails():
    ct = CustomTea("S", "Green")
    assert ct.getTeaDetails() == "CUSTOM TEA\nSize: S\nBase: Green\nFlavors:\nPrice: $10.00\n"
    ct1 = CustomTea("M", "Matcha")
    ct1.addFlavor("Strawberry")
    ct1.addFlavor("Milk")
    assert ct1.getTeaDetails() == "CUSTOM TEA\nSize: M\nBase: Matcha\nFlavors:\n\t+ Strawberry\n\t+ Milk\nPrice: $16.00\n"

def test_specialtyTea():
    st = SpecialtyTea("S", "Twizzy Tea")
    assert st.getSize() == "S"
    assert st.getPrice() == 12.0
    assert st.name == "Twizzy Tea"
    st1 = SpecialtyTea("M", "Bizzy Tea")
    assert st1.getPrice() == 16.0
    st2 = SpecialtyTea("L", "Busy Tea")
    assert st2.getPrice() == 20.0

    assert st.getTeaDetails() == "SPECIALTY TEA\nSize: S\nName: Twizzy Tea\nPrice: $12.00\n"

def test_teaOrder():
    to = TeaOrder(50)
    assert to.distance == 50
    assert to.teas == []

    ct = CustomTea("S", "Green")
    ct.addFlavor("Sprite")
    ct.addFlavor("Mud")
    st = SpecialtyTea("M", "Twizzy Tea")
    to.addTea(ct)
    assert to.teas == [ct]
    to.addTea(st)
    assert to.teas == [ct, st]
    assert to.getOrderDescription() == "******\nShipping Distance: 50 miles\nCUSTOM TEA\nSize: S\nBase: Green\nFlavors:\n\t+ Sprite\n\t+ Mud\nPrice: $10.50\n\n----\nSPECIALTY TEA\nSize: M\nName: Twizzy Tea\nPrice: $16.00\n\n----\nTOTAL ORDER PRICE: $26.50\n******\n"

def test_OrderQueue():
    oq = OrderQueue()
    assert oq.maxHeap == [0]
    assert oq.currentSize == 0

    ct = CustomTea("S", "Green")
    ct.addFlavor("Sprite")
    st = SpecialtyTea("M", "Twizzy Tea")

    to = TeaOrder(1)
    to.addTea(ct)
    to.addTea(st)
    to1 = TeaOrder(7)
    to1.addTea(st)
    to2 = TeaOrder(5)
    to3 = TeaOrder(3)
    to4 = TeaOrder(9)
    to4.addTea(ct)
    to5 = TeaOrder(8)

    oq.addOrder(to)
    oq.addOrder(to1)
    oq.addOrder(to2)
    oq.addOrder(to3)
    oq.addOrder(to4)
    oq.addOrder(to5)

    assert oq.processNextOrder() == to4.getOrderDescription()
    assert oq.processNextOrder() == to5.getOrderDescription()
    assert oq.processNextOrder() == to1.getOrderDescription()
    assert oq.processNextOrder() == to2.getOrderDescription()
    assert oq.processNextOrder() == to3.getOrderDescription()
    assert oq.processNextOrder() == to.getOrderDescription()

    # test it removes in same order no matter what order the items were added in
    oq.addOrder(to5)
    oq.addOrder(to2)
    oq.addOrder(to)
    oq.addOrder(to4)
    oq.addOrder(to1)
    oq.addOrder(to3)

    assert oq.processNextOrder() == to4.getOrderDescription()
    assert oq.processNextOrder() == to5.getOrderDescription()
    assert oq.processNextOrder() == to1.getOrderDescription()
    assert oq.processNextOrder() == to2.getOrderDescription()
    assert oq.processNextOrder() == to3.getOrderDescription()
    assert oq.processNextOrder() == to.getOrderDescription()