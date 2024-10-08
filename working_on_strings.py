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

# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    text = text.lower()
    dic = {}
    counter = 0
    for el in text:
        if el not in dic:
            dic[el] = 1
        elif el in dic:
            dic[el] += 1
    
    for key, value in dic.items():
        if value > 1:
            counter += 1
        
    return counter


#Get the middle character
#You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. 
#If the word's length is even, return the middle 2 characters.

def get_middle(s):
    return s[(len(s)-1)//2:(len(s)+2)//2]


# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# For example, the score of abad is 8 (1 + 2 + 1 + 4).
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

    def high(x):
    letters = list(map(chr, range(ord('a'), ord('z')+1)))
    values = list(range(1,27))
    dictionary = dict(zip(letters,values))
    words = x.split()
    word_value = {}
    for word in words:
        if word not in word_value:
            word_value[word] = 0
            for letter in word:
                if letter in dictionary:
                    if word not in word_value:
                        word_value[word] =0
                    word_value[word] += dictionary[letter]
                    
    return max(word_value,key=word_value.get)

# Can you find the needle in the haystack?
# Write a function findNeedle() that takes an array full of junk but containing one "needle"
# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle.

def find_needle(haystack):
    x = haystack.index("needle")
    for word in haystack:
        if word == "needle":
            return f"found the needle at position {x}"

# All of the animals are having a feast! Each animal is bringing one dish. There is just one rule: the dish must start and end with the same letters as the animal's name. 
# For example, the great blue heron is bringing garlic naan and the chickadee is bringing chocolate cake.
# Write a function feast that takes the animal's name and dish as arguments and returns true or false to indicate whether the beast is allowed to bring the dish to the feast.
# Assume that beast and dish are always lowercase strings, and that each has at least two letters. beast and dish may contain hyphens and spaces, 
# but these will not appear at the beginning or end of the string. They will not contain numerals.

def feast(beast, dish):
    return beast[0]==dish[0] and dish[-1]==beast[-1]


#You need to write regex that will validate a password to make sure it meets the following criteria:

# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a digit
# only contains alphanumeric characters (note that '_' is not alphanumeric)

regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$'

##ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
    # animal_crackers('Levelheaded Llama') --> True
    # animal_crackers('Crazy Kangaroo') --> False

    # (split + index)

def animal_crackers(text):
    words = text.lower().split()
    return words[0][0] == words[1][0]

Task 2: Palindrome Checker

# Write a Python function called is_palindrome that takes a string as input and returns True if the string 
# is a palindrome (reads the same forwards and backwards), and False otherwise. Use this function to check 
# if the following strings are palindromes:
# * "radar"
# * "python"
# * "level"

def palindrome_checker(word):
  return word == word[::-1]

# MASTER YODA: Given a sentence, return a sentence with the words reversed

#     master_yoda('I am home') --> 'home am I'
#     master_yoda('We are ready') --> 'ready are We'
    
# Note: The .join() method may be useful here. The .join() method allows you to 
# join together strings in a list with some connector string.

def master_yoda(text):
    reversed_text = text.split()[::-1]
    return " ".join(reversed_text).capitalize()

# Write a method (or function, depending on the language) that converts a string to camelCase, that is, all words must have their first letter capitalized and spaces must be removed.

# Examples (input --> output):
# "hello case" --> "HelloCase"
# "camel case word" --> "CamelCaseWord"

def camel_case(s):
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    camel_case_string = ''.join(capitalized_words)
    return camel_case_string

def camel_case(string):
    return string.title().replace(" ", "")

# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').
# Create a function which translates a given DNA string into RNA.
# For example:
# "GCAT"  =>  "GCAU"

def DNAtoRNA(dna):
    return dna.replace('T', 'U')


# This time no story, no theory. The examples below show you how to write function accum:
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(st):
    result = [char.upper() + char.lower() * i for i, char in enumerate(st)]
    return '-'.join(result)

# Write a function that checks if a given string (case insensitive) is a palindrome.
# A palindrome is a word, number, phrase, or other sequence of symbols that reads the 
# same backwards as forwards, such as madam or racecar.

def is_palindrome(s):
    return True if s.lower()[::-1] == s.lower() else False


# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F

def abbrev_name(name):
    ns = name.split()
    return f"{ns[0][0].capitalize()}.{ns[1][0].capitalize()}"


# Oh no! I've lost my glasses, but paradoxically, I need glasses to find my glasses!
# Please help me out by showing me the index in the list which contains my glasses. They look like two capital Os, with at least one dash in between!
# This means that both O--O and O------------O are valid glasses, but not O----#--O for example!
# Search thoroughly, you might find my glasses in places such as 'dustO-Odust'

import re
def find_glasses(lst):
    pattern = r'O-+O'
    for index, word in enumerate(lst):
        if re.search(pattern, word):
            return index

# Task: Write a function "coffee" that accepts a string as a parameter and returns that string with every instance of coffee in all caps.
# Input: string. The word "coffee" may occur more than once. It may have some capital letters or already be in all-caps. There may be punctuation in the string too. It will not be part of another word like "Coffeeburger", which isn't a word anyway.
# Output: string with all instances of coffee in all-caps:

import re
def coffee(sentence):
    pattern = re.compile(r"coffee",re.IGNORECASE)
    return pattern.sub("COFFEE", sentence)

# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

import re
def domain_name(url):
    pattern = r"^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n?]+)"
    domain = re.findall(pattern, url)
    if domain:
        domain_parts = domain[0].split(".")
        if len(domain_parts) > 2:
            return domain_parts[-3]
        else:
            return domain_parts[-2]

#Alternative 

def domain_name(url):
    url = url.replace('www.','')
    url = url.replace('https://','')
    url = url.replace('http://','')
    
    return url[0:url.find('.')]