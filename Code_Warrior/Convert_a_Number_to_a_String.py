def number_to_string1(num):
    return list([str(digit) for digit in str(num)])
print(number_to_string1(-123))

def number_to_string2(num):
    return '{}'.format(num)
print(number_to_string2(-100))

def number_to_string3(num):
    return f'{num}'
print(number_to_string3(23))

def number_to_string4(num):
    return str(num)
print(type(number_to_string4(4.5)))

def number_to_string5(num):
    digits = []
    while num > 0:
        digits.append(str(num % 10))
        num //= 10
    digits.reverse()
    result = ''.join(digits)
    return result
print(number_to_string5(345678))

"""The condition while num >= 0 will result in an infinite loop when num is zero, 
    as it will keep appending '0' to the list digits. 
    To handle zero properly and also to correct any issues with the negative numbers, 
    the function should check if num is zero at the beginning and handle it separately"""
   
def number_to_string6(num):
    if num == 0:
        return '0'
    if num < 0:
        neg = '-'
        num = abs(num)
    
    digits = []
    while num > 0:
        digits.append(str(num % 10))
        num //= 10
    digits.reverse()
    result = neg + ''.join(digits)
    return result
print(number_to_string6(-10))
print(number_to_string6(0))
print(type(number_to_string6(-10)))

# def number_to_string6(num):
#     digits = []
#     while num > 0:
#         digits.append()      #for digit in num
#     return [str(digits)]
# print number_to_string6(321)
            
# print(number_to_string6(123))
