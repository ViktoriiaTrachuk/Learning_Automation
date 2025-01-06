while True:
    try:
        num1 = int(input("take integer: "))
        break
    except ValueError:
        print("Not a number")

while True:
    try:
        num2 = int(input("take another integer: "))
        break
    except ValueError:
        print("Not a number too")



num2 = int(input('take another integer: '))
result = "num1" if num1 > num2 else num2