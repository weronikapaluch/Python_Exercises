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