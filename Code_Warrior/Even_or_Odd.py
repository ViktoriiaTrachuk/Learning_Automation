#https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python
#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

#option 1
def even_or_odd(number):
    if number % 2 == 0:
        print(f" {number} is Even")
    else:
        print(f"{number} is Odd")
even_or_odd(10)
even_or_odd(3)
even_or_odd(-2)

