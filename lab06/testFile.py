from Apartment import Apartment
from lab06 import mergesort, ensureSortedAscending, getBestApartment, getWorstApartment, getAffordableApartments

def test_Apartment():
    a1 = Apartment(1000, 400, "excellent")

    assert a1.getRent() == 1000
    assert a1.getMetersFromUCSB() == 400
    assert a1.getCondition() == "excellent"
    assert a1.getApartmentDetails() == "(Apartment) Rent: $1000, Distance From UCSB: 400m, Condition: excellent"

    a2 = Apartment(1100, 400, "excellent")
    a3 = Apartment(1000, 300, "excellent")
    a4 = Apartment(1000, 400, "average")
    a5 = Apartment(1000, 400, "excellent")

    assert a2.getApartmentDetails() == "(Apartment) Rent: $1100, Distance From UCSB: 400m, Condition: excellent"

    assert a1 < a2
    assert a3 < a1
    assert a1 < a4

    assert a1 == a5
    assert not a1 == a4

    assert a2 > a1
    assert a4 > a3
    assert a4 > a1

def test_mergeSort():
    a1 = Apartment(1500, 1000, "excellent")
    a2 = Apartment(1400, 1500, "excellent")
    a3 = Apartment(1200, 800, "average")
    a4 = Apartment(1500, 800, "average")
    a5 = Apartment(1500, 500, "bad")
    a6 = Apartment(1700, 1100, "excellent")
    a7 = Apartment(1500, 1000, "average")
    a8 = Apartment(1200, 600, "bad")
    a9 = Apartment(1200, 600, "average")
    ap1 = [a1, a2, a3, a4, a5, a6, a7, a8, a9]

    assert ensureSortedAscending(ap1) == False

    assert getBestApartment(ap1) == "(Apartment) Rent: $1200, Distance From UCSB: 600m, Condition: average"
    assert getBestApartment(ap1) == a9.getApartmentDetails()

    assert getWorstApartment(ap1) == a6.getApartmentDetails()

    assert getAffordableApartments(ap1, 1400) == a9.getApartmentDetails() + "\n" + a8.getApartmentDetails() + "\n" + a3.getApartmentDetails() + "\n" + a2.getApartmentDetails()
    assert getAffordableApartments(ap1, 1000) == ''

    mergesort(ap1)
    assert ap1 == [a9, a8, a3, a2, a5, a4, a1, a7, a6]
    assert ensureSortedAscending(ap1) == True

    # test the return of an empty list in ensureSortedAscending
    assert ensureSortedAscending([]) == True

def test_identicalApartments():
    a1 = Apartment(1, 1, "bad")
    ap1 = [a1, a1, a1, a1]
    assert getBestApartment(ap1) == "(Apartment) Rent: $1, Distance From UCSB: 1m, Condition: bad"
    assert getWorstApartment(ap1) == "(Apartment) Rent: $1, Distance From UCSB: 1m, Condition: bad"
    assert ensureSortedAscending(ap1) == True
    mergesort(ap1)
    assert ensureSortedAscending(ap1) == True