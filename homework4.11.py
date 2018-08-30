pizzas = ['pizzahut', 'burgerking', 'mcdonald']
for pizza in pizzas:
	print(pizza.title())
print('*'*80)

friendPizzas = pizzas[:]

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza.title())

print("My friend's favorite pizzas are:")
for pizza in friendPizzas:
	print(pizza.title())

print(pizza)
