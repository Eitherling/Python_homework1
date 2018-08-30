prompt = '\nIf you could visit one place in the world, where would you go?'
prompt += '(enter "quit" to quit)'

place_active = True
favorite_places = []

while place_active:
    place = input(prompt)
    if  place.lower() == 'quit':
        place_active = False
    else:
        favorite_places.append(place)

print("These places you wanna go:")
print(favorite_places)    

