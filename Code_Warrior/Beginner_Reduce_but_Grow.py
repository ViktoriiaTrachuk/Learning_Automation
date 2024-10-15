#Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
#[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
arr = [1, 2, 3] #,[16, [4, 1, 1, 1, 4]],[64, [2, 2, 2, 2, 2, 2]]]
def grow(arr):
    res = 1
    for i in arr:
        res *= i
    return res
print(grow(arr))

import math 
def grow2(arr):
    return math.prod(arr)
print(grow2(arr))


from math import prod
def grow3(arr):
    return prod(arr) 
print(grow3(arr)) 


