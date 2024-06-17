# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# [1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
# [1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
# [] --> []

# You can assume that all values are integers. Do not mutate the input array.

def invert_1(lst):
    new_lst = []
    for num in lst:
        new_lst.append(num * -1)
    return new_lst
    pass

def ivert_2(lst):
    return [-el for el in lst]

    
# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

def disemvowel(string_):
    vowels = ("e","i","o","u","a")
    result = [letter for letter in string_ if letter.lower() not in vowels] 
    string_ = ''.join(result) 
    return string_


# In this Kata we are passing a number (n) into a function.
# Your code will determine if the number passed is even (or not).
# The function needs to return either a true or false.
# Numbers may be positive or negative, integers or floats.
# Floats with decimal part non equal to zero are considered UNeven for this kata.

def is_even(n): 
    if n % 2 ==0:
        return True
    else:
        return False
    pass


# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

def find_it(seq):
    dic = {}
    for dig in seq:
        if dig in dic:
            dic[dig] += 1
        else:
            dic[dig] = 1
            
    for key, value in dic.items():
        if value % 2 != 0:
            return key