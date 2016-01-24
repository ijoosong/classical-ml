
# listFunctions.py
# Contains basic list manipulation functions
# J. Hassler Thurston
# 26 November 2013 (Adapted from Mathematica code written in 2010/2011)
# Python 2.7.6

# returns a running sum of the elements in ls


def cumulativeSum(ls):
    total = 0
    answer = []
    for i in ls:
        total += i
        answer.append(total)
    return answer

# returns a running sum of the elements in ls, starting with 0


def cumulativeSumZero(ls):
    total = 0
    answer = [0]
    for i in ls:
        total += i
        answer.append(total)
    return answer