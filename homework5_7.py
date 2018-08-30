favoriteFruit = ['apple', 'banana', 'cherry',]

for i in range(0,3):
    print('Please input a fruit:')
    fruit = input()
    
    if fruit in favoriteFruit:
        print('You really like ' + fruit + '.')
    else:
        print("You don't like that.")
