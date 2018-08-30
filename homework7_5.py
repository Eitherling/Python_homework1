prompt = "\nPlease enter your age:"

age = input(prompt)
age = int(age)

if age <= 3 and age >= 0:
    price = 0
elif age > 3 and age <= 12:
    price = 10
elif age > 12:
    price = 15

if price ==0:
    print("You are free, child. Welcome!")
elif price > 0:
    print("The price of your ticket is " + str(price) +" dollars.")
