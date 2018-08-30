favoriteNumber = {
    'Jason' : '3360',
    'Faker' : '1000',
    'Emiya' : '222',
    'Bob' : '3425',
    }
for name in favoriteNumber.keys():
    print(name.title())
    
print('-' * 80)

print("Jason's favorite number is: ")
print(favoriteNumber ['Jason'].title())
print("Faker's favorite number is: ")
print(favoriteNumber ['Faker'].title())
print("Emiya's favorite number is: ")
print(favoriteNumber ['Emiya'].title())
print("Bob's favorite number is: ")
print(favoriteNumber ['Bob'].title())
