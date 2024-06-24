def number_to_string1(num):
    return [str(digit) for digit in str(num)]
print(number_to_string1(123))

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
    return digits

print(number_to_string5(12345))

# def number_to_string6(num):
#     digits = []
#     while num > 0:
#         digits.append()      #for digit in num
#     return [str(digits)]
# print number_to_string6(321)
            
# print(number_to_string6(123))
