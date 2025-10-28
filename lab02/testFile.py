from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder

def test_Beverage():
    b1 = Beverage(1, 2.0) 
    assert b1.ounces == 1 # Tests that the constructor correctly sets attribute "ounces"
    assert b1.price == 2.0 # Tests that the constructor correctly sets attribute "price"

def test_updateOunces():
    b1 = Beverage(5, 6.0)
    b1.updateOunces(3)
    assert b1.ounces == 3 # Tests that updateOunces correctly changes attribute "ounces"

def test_updatePrice():
    b1 = Beverage(8, 9.0)
    b1.updatePrice(4.0)
    assert b1.price == 4.0 # Tests that updatePrice correctly changes attribute "price"

def test_getOunces():
    b1 = Beverage(3, 4.5)
    assert b1.getOunces() == b1.ounces # checks that getOunces method returns attribute "ounces"
    assert b1.getOunces() == 3 # checks that getOunces method returns the correct value

def test_getPrice():
    b1 = Beverage(8, 4.0)
    assert b1.getPrice() == b1.price # checks that getOunces method returns attribute "price"
    assert b1.getPrice() == 4.0 # checks that getPrice method returns the correct value

def test_getInfo():
    b1 = Beverage(2, 4.2323)
    assert b1.getInfo() == '2 oz, $4.23' # checks that getInfo converts price float to 2 decimal places

    b2 = Beverage(1, 1.9)
    assert b2.getInfo() == '1 oz, $1.90' # Also checks getInfo converts float to 2 decimal places

    b3 = Beverage(12312, 12312.0)
    assert b3.getInfo() == '12312 oz, $12312.00' # Checks that big integers are correctly converted as well

def test_Coffee():
    c1 = Coffee(3, 3.0, 'Espresso')
    assert c1.ounces == 3 # Checks that base class constructor still works
    assert c1.price == 3.0 # Checks that base class constructor still works
    assert c1.style == 'Espresso' # Checks Coffee constructor for attribute "style"
    assert c1.getInfo() == 'Espresso Coffee, 3 oz, $3.00' # Checks that Coffee getInfo method overrides Beverage getInfo method
    assert c1.getInfo() != 'Espresso Coffee, 3 oz, $3.00\n' # Checks that there is no newline at the end of the returned string

def test_FruitJuice():
    f1 = FruitJuice(4, 4.0, ['Strawberry', 'Lemon', 'Blueberry', 'Pineapple'])
    assert f1.ounces == 4 # Check that base constructor still works
    assert f1.price == 4.0 # Check that base constructor still works
    assert f1.fruits == ['Strawberry', 'Lemon', 'Blueberry', 'Pineapple'] # Check constructor functions properly for attribute "fruits"
    assert f1.getInfo() == 'Strawberry/Lemon/Blueberry/Pineapple Juice, 4 oz, $4.00' # make sure it follows correct output
    assert f1.getInfo() != 'Strawberry/Lemon/Blueberry/Pineapple Juice, 4 oz, $4.00\n' # make sure there's no newline

def test_addBeverage():
    b1 = Beverage(1, 2.0)
    order1 = DrinkOrder()
    assert order1.addBeverage(b1) == None # Should not return anything, only job is to append beverages to list

def test_getTotalOrder():
    b1 = Beverage(3, 4.0)
    c1 = Coffee(3, 3.0, 'Espresso')
    order1 = DrinkOrder()
    order1.addBeverage(b1)
    assert order1.getTotalOrder() == 'Order Items:\n* 3 oz, $4.00\nTotal Price: $4.00' # Check returned string has the desired format

    order1.addBeverage(c1)
    assert order1.getTotalOrder() == 'Order Items:\n* 3 oz, $4.00\n* Espresso Coffee, 3 oz, $3.00\nTotal Price: $7.00' # Check that after using addBeverage that getTotalOrder still works in the desired format

    order2 = DrinkOrder()
    assert order2.getTotalOrder() == 'Order Items:\nTotal Price: $0.00' # Check that a DrinkOrder class with no Beverage classes added returns the correct output