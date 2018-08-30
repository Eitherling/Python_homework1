prompt = "\nPlease enter a ingredient of pizza:"
prompt += "\n(Enter quit to exit the program\\n)"

active = True

while active :
    ingredient = input(prompt)
    if ingredient.lower() == 'quit':
        active = False
    else:
        print(ingredient.title() + " has been added to pizza.")
