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


# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.

# Don't forget the space after the closing parentheses!

def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

    def find_outlier(integers):
    lst_even = []
    lst_odd = []
    
    for n in integers:
        if n % 2 == 0:
            lst_even.append(n)
        else:
            lst_odd.append(n)
    
    if len(lst_even) > len(lst_odd):
        return lst_odd[0]
    else:
        return lst_even[0]