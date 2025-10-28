def integerDivision(n, k):
    if n < k:
        return 0 # base case, returns 0 if k is bigger than n
    
    if n >= k:
        return 1 + integerDivision(n-k, k) # when n >= k, adds 1 to return value, calls integerDivision again
    
def collectEvenInts(listOfInt):
    if listOfInt == []:
        return [] # base case when the list is empty. Returns an empty list
    
    if listOfInt[0] % 2 == 0: # when first index in list is even
        return [listOfInt[0]] + collectEvenInts(listOfInt[1:]) # returns list containing 1st index, then calls function w/o first index
    else:
        return collectEvenInts(listOfInt[1:]) # calls function on next index, calls function w/o first index
    
def countVowels(someString):
    vowel_list = ['a', 'e', 'i', 'o', 'u']

    if someString == '':
        return 0 # base case when the string is empty. Returns 0
    
    if someString.lower()[0] in vowel_list: # code below runs when first letter in string is vowel
        return 1 + countVowels(someString[1:]) # adds 1 to return then calls function w/o first letter
    else:
        return countVowels(someString[1:]) # doesn't add to return then calls function w/o first letter
    
def reverseString(s):
    if s == '':
        return '' # base case when string is empty returns empty string
    
    return s[-1] + reverseString(s[:-1]) # returns the last letter in string then calls function w/o last letter in string

def removeSubString(s, sub):
    if s == '':
        return '' # base case when string is empty, returns empty string
    
    if s[:len(sub)] == sub: # checks if start of string is the same as sub
        return removeSubString(s[len(sub):], sub) # calls function w/ string without start
    else:
        return s[0] + removeSubString(s[1:], sub) # returns first letter of string then calls function w/o first letter of string