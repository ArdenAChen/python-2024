from lab03 import integerDivision, collectEvenInts, countVowels, reverseString, removeSubString

def test_integerDivision():
    assert integerDivision(6, 2) == 3
    assert integerDivision(2, 2) == 1
    assert integerDivision(0, 3) == 0
    assert integerDivision(5, 12) == 0
    assert integerDivision(15, 4) == 3

def test_collectEvenInts():
    assert collectEvenInts([2, 4, 6, 8]) == [2, 4, 6, 8]
    assert collectEvenInts([]) == []
    assert collectEvenInts([1, 3, 5, 7, 9]) == []
    assert collectEvenInts([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8]
    assert collectEvenInts([12, 5, 9, 4, 5, 2, 8, 101]) == [12, 4, 2, 8]

def test_countVowels():
    assert countVowels('') == 0
    assert countVowels('aaaa') == 4
    assert countVowels('why') == 0
    assert countVowels('A  A') == 2
    assert countVowels('!829fn?') == 0

def test_reverseString():
    assert reverseString('') == ''
    assert reverseString('abcd') == 'dcba'
    assert reverseString('aaaa') == 'aaaa'
    assert reverseString('qwertyuiopasdfghjklzxcvbnm') == 'mnbvcxzlkjhgfdsapoiuytrewq'
    assert reverseString('Answer') == 'rewsnA'

def test_removeSubString():
    assert removeSubString('', '') == ''
    assert removeSubString('luh', 'f') == 'luh'
    assert removeSubString('aLaLaL', 'L') == 'aaa'
    assert removeSubString('aaAaaaA4t', 'aA') == 'aaa4t'
    assert removeSubString('00230023003200323', '23') == '00000032003'