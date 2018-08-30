available_toppings = ('mushrooms','olives','green peppers','pepperoni', 
'pineapple','extra cheese')

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print('Sorry, we really dont have the topping ----' + \
        requested_topping + ' you want, you can try others.')
        
print('\nFinished making your pizza.')

print('*' * 80)

print('I am a programmer\
and will be a programmer')
