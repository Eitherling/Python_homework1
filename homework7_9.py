# -*- coding:utf-8 -*- 

sandwich_orders = ['Babiq', 'pastrami', 'tuna', 'pastrami', 'cip', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I made ' + sandwich + ' for you.')
    finished_sandwiches.append(sandwich)

print("\nI have made these:")

for sandwich in finished_sandwiches:
    print(sandwich.title())

# pastrami ย๔อ๊มหฃบ

sandwich_orders = ['Babiq', 'pastrami', 'tuna', 'pastrami', 'cip', 'pastrami']
print("\n--- The pastrami has been sold out. ---")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("The new sandwich list is:")
print(sandwich_orders)
