print('Please input your age:')

inputage = input()
age = int(inputage)

if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are learning to walk.")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are a adult.")
elif age >= 65:
    print("You are a oldfolk.")
