# Lab00, CS 9, Arden Chen

def areElementsInList(list1, list2):
    ''' This function takes two lists as its parameters (list1 and
        list2). Return True if each element in list1 exists in list2.
        Return False otherwise. If list1 contains no elements, True is
        returned.
    '''
    for element in list1: # Run loop for every element in list1
        if element in list2:
            pass
        else:
            return False # Stop loop and return false if any element in list1 not in list2

    return True # Return True if all elements in list1 in list2

assert areElementsInList(["one",2], [0,"one",2,"three"]) == True
assert areElementsInList([],[1,2,3,4]) == True
assert areElementsInList([1,2,3],[1,2]) == False
assert areElementsInList([1,2,3],[3,2,1]) == True

def alternateCase(s):
    ''' This function takes a string parameter (s) and returns a new
        string that flips the case of each alpha character in s.
    '''
    swapped_string = ""
    for char in s:
        if char.islower(): # Checks if the character is lower case
            swapped_string += char.upper()
        elif char.isupper(): # Checks if the character is upper case
            swapped_string += char.lower()
        else:
            swapped_string += char # If upper or lower case doesn't apply just adds it back
    return swapped_string

assert alternateCase("") == ""
assert alternateCase("This is a Sentence") == "tHIS IS A sENTENCE"
assert alternateCase("CS9") == "cs9"
assert alternateCase("9.95") == "9.95"

def getCharacterCount(s):
    ''' This function takes a string parameter (s) and returns a dictionary
        type where each key in the dictionary is a unique upper-case character
        in s and its associated value is the number of occurences the unique
        character exists in s. Note that the unique characters should be case
        insensitive ("a" and "A" are considered the same and should be stored as
        "A" in the dictionary). Non alpha characters (including whitespaces)
        and their occurences should also be stored in the dictionary.
    '''
    convert_to_upper = s.upper() # Convert all lowercase to uppercase for dict
    string_values_dict= {} # Create empty dictionary to update with new keys
    for char in convert_to_upper:
        if char not in string_values_dict:
            string_values_dict.update({char: 1}) # Add new key with value 1 if it is a character not in the dict already
        elif char in string_values_dict:
            string_values_dict[char] += 1 # If key already exists, add 1
    return string_values_dict

x = getCharacterCount("This is a Sentence")
assert x.get("S") == 3
assert x.get("P") == None
assert x.get("I") == 2
assert x.get(" ") == 3

y = getCharacterCount("Pi is Approximately 3.14159")
assert y.get("1") == 2
assert y.get("A") == 2
assert y.get("P") == 3
assert y.get(".") == 1
assert y.get(4) == None
