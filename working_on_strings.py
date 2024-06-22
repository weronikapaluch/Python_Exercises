# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"


def reverse_words(text):
    words = text.split(" ")
    reversed_words = [word[::-1] for word in words]
    result = " ".join(reversed_words)
    return result


# Make a program that filters a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

def friend(x): 
    friend = []
    for name in x: 
        if len(name) == 4:
            friend.append(name) 
    return friend

#OR

def friend(x):
    return [name for name in x if len(name) == 4]


# Given a string, remove any characters that are unique from the string.

# Example:

# input: "abccdefee"

# output: "cceee"

def only_duplicates(st):
    counter = {}

    for el in st:
        if el in counter:
            counter[el] += 1
        else:
            counter[el] = 1
    
    return ''.join([el for el in st if counter[el] > 1])