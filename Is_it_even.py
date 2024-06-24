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

# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.
def find_short(s):
    return min(len(x) for x in s.split())


# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"

def high_and_low(numbers):
    lst_numbers = numbers.split()
    lst_numbers = [int(n) for n in lst_numbers]
    max_num = max(lst_numbers)
    min_num = min(lst_numbers)
    return f"{max_num} {min_num}"


#Write function bmi that calculates body mass index (bmi = weight / height2).
def bmi(weight, height):
    bmi = weight / (height**2)
    if bmi <= 18.5: 
        return "Underweight"
    elif bmi <= 25.0: 
        return "Normal"
    elif bmi <= 30.0: 
        return "Overweight"
    elif bmi > 30: 
        return "Obese"