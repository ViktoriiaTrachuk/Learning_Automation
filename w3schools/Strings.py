a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print('Yes')

age = 36
txt = f"My age is {age}"
print (txt)

#Python String Formatting
txt1 = f"The price is 49 dollars"
price = 59
txt2 = f"The price is {price} dollars"
txt3 = f"The price is {price:.2f} dollars"
txt4 = f"the price is {41:.2f} dollars"
print(txt1, txt2, txt3, txt4) 

#Perform Operations in F-Strings
oper = f"the price is {20*3:.2f} dollars"
print(oper)

price = 59
tax = 0.25
txt = f"The price is {price + price*tax:.2f} dollars"
print (txt)

price = 59
txt = f"It is very {'expensive' if price >50 else 'cheap'"
print(txt)
print(f"It is very {'expensive' if price >50 else 'cheap'"))

#Execute Functions in F-Strings
fruit = "apples"
txt = f"I love {fruit.upper()}"
print txt

def myconverter(x):
  return x * 0.3048
txt = f"The plane is flying at a {myconverter(30000)} meters altitude"
print(txt)

#other modifiers that can be used to format values

#Use a comma as a thousand separator:
price 59000
txt = f"The price is {price:,} dollars"
print txt

#to format strings with the format() method:
price = 33
txt = "The price is {} dollars"
print(txt.format(price))

quantity = 2
itemno = 354
price = 30
my_order = "I need {} pieces of item number {} for {:.2f} dollars."
#myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars." - to use index numbers
print(my_order.format(quantity, itemno, price))

