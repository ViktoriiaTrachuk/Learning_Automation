# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

#Examples:

#solution('abc', 'bc') # returns true
#solution('abc', 'd') # returns false

def solution1(text, ending):
    return text[-len(ending):] == ending if len(ending) <= len(text) else False
    # your code here...
    pass
print(solution1('hello', 'lo'))

def solution2(text, ending):
    return text.endswith(ending)   
    # your code here...
    pass

print(solution2('hello', 'lo'))

def solution3(text, ending):
    return ending == text[-len(ending):]
print(solution3('sleep', 'eep'))

def solution4(text, ending):
    return ending == text[-len(text):]
print(solution4('red', 'dress'))