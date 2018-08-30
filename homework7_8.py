sandwich_orders = ['Babiq', 'tuna', 'cip']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I made ' + sandwich + ' for you.')
    finished_sandwiches.append(sandwich)

print("\nI have made these:")

for sandwich in finished_sandwiches:
    print(sandwich.title())

